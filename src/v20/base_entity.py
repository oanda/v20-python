import ujson as json
import re
import yaml
from collections import OrderedDict


def represent_odict(dump, tag, mapping, flow_style=None):
    """
    Like BaseRepresenter.represent_mapping, but does not issue the sort().
    """
    value = []
    node = yaml.MappingNode(tag, value, flow_style=flow_style)
    if dump.alias_key is not None:
        dump.represented_objects[dump.alias_key] = node
    best_style = True
    if hasattr(mapping, 'items'):
        mapping = mapping.items()
    for item_key, item_value in mapping:
        node_key = dump.represent_data(item_key)
        node_value = dump.represent_data(item_value)
        if not (isinstance(node_key, yaml.ScalarNode) and not node_key.style):
            best_style = False
        if not (isinstance(node_value, yaml.ScalarNode) and not node_value.style):
            best_style = False
        value.append((node_key, node_value))
    if flow_style is None:
        if dump.default_flow_style is not None:
            node.flow_style = dump.default_flow_style
        else:
            node.flow_style = best_style
    return node


class Property(object):
    def __init__(
        self,
        name,
        displayName,
        description,
        typeClass,
        typeName,
        required,
        default
    ):
        self.name = name
        self.displayName = displayName
        self.description = description
        self.typeClass = typeClass
        self.typeName = typeName
        self.required = required
        self.default = default


class Field(Property):
    def __init__(self, property, value):
        super(Field, self).__init__(
            property.name,
            property.displayName,
            property.description,
            property.typeClass,
            property.typeName,
            property.required,
            property.default
        )

        self.value = value

    def __str__(self):
        if self.typeClass.startswith("array"):
            return "{} = [{}]".format(
                self.displayName, len(self.value)
            )

        if self.typeClass.startswith("object"):
            v = str(self.value)
            v = v.strip()
            v = "{ " + ", ".join(v.split("\n")) + " }"

            return "{} = {}".format(
                self.displayName, v
            )

        return "{} = {}".format(
            self.displayName,
            self.value
        )

    def value_ordered_dict(self, verbose):
        if self.typeClass == "array_object":
            return [ x.ordered_dict(verbose) for x in self.value ]

        if self.typeClass == "object":
            return self.value.ordered_dict(verbose)

        return self.value

class EntityDict(object):
    def __init__(self):
        self.dict = {}

    def __len__(self):
        return len(self.dict)

    def prop_dict_value(self, value):
        if hasattr(value, 'dict'):
            return value.dict()
        return value

    def set(self, key, value):
        if isinstance(value, list):
            self.dict[key] = [self.prop_dict_value(v) for v in value]
        else:
            self.dict[key] = self.prop_dict_value(value)


class BaseEntity(object):
    _properties = []

    def __init__(self):
        pass

    def fields(self):
        for prop in self._properties:
            value = getattr(self, prop.name)
            if value is not None:
                yield Field(prop, value)

    def name(self):
        name_string = self._name_format

        for m in re.findall(r'{[^}]+}', name_string):
            key = m[1:-1]
            value = getattr(self, key)
            if value is not None:
                name_string = name_string.replace(m, str(value))

        return name_string

    def summary(self):
        summary_string = self._summary_format

        for m in re.findall(r'{[^}]+}', summary_string):
            key = m[1:-1]
            value = getattr(self, key)
            if value is not None:
                summary_string = summary_string.replace(m, str(value))

        return summary_string

    def title(self):
        name = self.name()
        summary  = self.summary()

        title_string = name

        if len(name) > 0 and len(summary) > 0:
            title_string += ": "

        title_string += summary

        return title_string

    def fields_str(self):
        s = ""

        for field in self.fields():
            s += str(field) + "\n"

        return s

    def __str__(self):
        return self.yaml(False)

    def ordered_dict(self, verbose):
        d = OrderedDict()

        for field in self.fields():
            key = field.name

            if verbose:
                key = field.displayName

            d[key] = field.value_ordered_dict(
                verbose
            )

        return d


    def yaml(self, verbose=False):
        yaml.SafeDumper.add_representer(
            OrderedDict,
            lambda dumper, value: represent_odict(
                dumper, u'tag:yaml.org,2002:map', value
            )
        )

        return yaml.safe_dump(
            self.ordered_dict(verbose=verbose),
            default_flow_style=False,
            indent=2
        ).strip()


    def dict(self):
        spec = EntityDict()
        for field in self.fields():
            if field.typeName == "primitives.DecimalNumber" or \
               field.typeName == "primitives.AccountUnits" or \
               field.typeName == "pricing.PriceValue":
                spec.set(field.name, str(field.value))
            else:
                spec.set(field.name, field.value)
        return spec.dict


    def json(self):
        return json.dumps(self.dict())


    def diff(self, other):
        for property in self._properties:
            self_value = getattr(self, property.name)
            other_value = getattr(other, property.name)

            if self_value is None:
                continue

            assert \
                other_value is not None, \
                "Did not expected {}.{} to be unset".format(
                    self.__class__.__name__,
                    property.name
                )

            if property.typeClass == "primitive":
                assert \
                    self_value == other_value, \
                    "Expected value for {}.{} is {}, got {}".format(
                        self.__class__.__name__,
                        property.name,
                        self_value,
                        other_value
                    )
            elif property.typeClass == "object":
                self_value.diff(other_value)

        return True
