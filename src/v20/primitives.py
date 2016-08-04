import json
from v20.base_entity import BaseEntity
from v20.base_entity import Property
from v20.base_entity import EntityDict
from v20.request import Request



class Instrument(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "name",
            "name",
            "The name of the Instrument",
            "primitive",
            "primitives.InstrumentName",
            False,
            None
        ),
        Property(
            "type",
            "type",
            "The type of the Instrument",
            "primitive",
            "primitives.InstrumentType",
            False,
            None
        ),
        Property(
            "displayName",
            "displayName",
            "The display name of the Instrument",
            "primitive",
            "string",
            False,
            None
        ),
        Property(
            "pipLocation",
            "pipLocation",
            "The location of the \"pip\" for this instrument. The decimal position of the pip in this Instrument's price can be found at 10 ^ pipLocation (e.g. -4 pipLocation results in a decimal pip position of 10 ^ -4 = 0.0001).",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "displayPrecision",
            "displayPrecision",
            "The number of decimal places that should be used to display prices for this instrument. (e.g. a displayPrecision of 5 would result in a price of \"1\" being displayed as \"1.00000\")",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "tradeUnitsPrecision",
            "tradeUnitsPrecision",
            "The amount of decimal places that may be provided when specifying the number of units traded for this instrument.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "minimumTradeSize",
            "minimumTradeSize",
            "The smallest number of units allowed to be traded for this instrument.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "maximumTrailingStopDistance",
            "maximumTrailingStopDistance",
            "The maximum trailing stop distance allowed for a trailing stop loss created for this instrument. Specified in price units.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "minimumTrailingStopDistance",
            "minimumTrailingStopDistance",
            "The minimum trailing stop distance allowed for a trailing stop loss created for this instrument. Specified in price units.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "maximumPositionSize",
            "maximumPositionSize",
            "The maximum position size allowed for this instrument. Specified in units.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "maximumOrderUnits",
            "maximumOrderUnits",
            "The maximum units allowed for an Order placed for this instrument. Specified in units.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "marginRate",
            "marginRate",
            "The margin rate for this instrument.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(Instrument, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('name') is not None:
            body['name'] = \
                data.get('name')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('displayName') is not None:
            body['displayName'] = \
                data.get('displayName')

        if data.get('pipLocation') is not None:
            body['pipLocation'] = \
                data.get('pipLocation')

        if data.get('displayPrecision') is not None:
            body['displayPrecision'] = \
                data.get('displayPrecision')

        if data.get('tradeUnitsPrecision') is not None:
            body['tradeUnitsPrecision'] = \
                data.get('tradeUnitsPrecision')

        if data.get('minimumTradeSize') is not None:
            body['minimumTradeSize'] = \
                data.get('minimumTradeSize')

        if data.get('maximumTrailingStopDistance') is not None:
            body['maximumTrailingStopDistance'] = \
                data.get('maximumTrailingStopDistance')

        if data.get('minimumTrailingStopDistance') is not None:
            body['minimumTrailingStopDistance'] = \
                data.get('minimumTrailingStopDistance')

        if data.get('maximumPositionSize') is not None:
            body['maximumPositionSize'] = \
                data.get('maximumPositionSize')

        if data.get('maximumOrderUnits') is not None:
            body['maximumOrderUnits'] = \
                data.get('maximumOrderUnits')

        if data.get('marginRate') is not None:
            body['marginRate'] = \
                data.get('marginRate')

        self = Instrument(**body)

        return self

class EntitySpec(object):
    Instrument = Instrument

    def __init__(self, ctx):
        self.ctx = ctx

