import json
import re


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
        if value is None:
            return

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
                name_string = name_string.replace(m, value)

        return name_string

    def summary(self):
        summary_string = self._summary_format

        for m in re.findall(r'{[^}]+}', summary_string):
            key = m[1:-1]
            value = getattr(self, key)
            if value is not None:
                summary_string = summary_string.replace(m, value)

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
        s = ""

        title = self.title()

        if len(title) > 0:
            s += title + "\n"
            s += len(title) * "=" + "\n"
            s += "\n"

        s += self.fields_str()

        return s

    def dict(self):
        entity = EntityDict()
        for field in self.fields():
            entity.set(field.name, field.value)
        return entity.dict

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
