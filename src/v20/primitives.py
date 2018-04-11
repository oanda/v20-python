import ujson as json
from v20.base_entity import BaseEntity
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import spec_properties



class Instrument(BaseEntity):
    """
    Full specification of an Instrument.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = ""

    #
    # Format string used when generating a name for this object
    #
    _name_format = ""

    #
    # Property metadata for this object
    #
    _properties = spec_properties.primitives_Instrument

    def __init__(self, **kwargs):
        """
        Create a new Instrument instance
        """
        super(Instrument, self).__init__()
 
        #
        # The name of the Instrument
        #
        self.name = kwargs.get("name")
 
        #
        # The type of the Instrument
        #
        self.type = kwargs.get("type")
 
        #
        # The display name of the Instrument
        #
        self.displayName = kwargs.get("displayName")
 
        #
        # The location of the "pip" for this instrument. The decimal position
        # of the pip in this Instrument's price can be found at 10 ^
        # pipLocation (e.g. -4 pipLocation results in a decimal pip position of
        # 10 ^ -4 = 0.0001).
        #
        self.pipLocation = kwargs.get("pipLocation")
 
        #
        # The number of decimal places that should be used to display prices
        # for this instrument. (e.g. a displayPrecision of 5 would result in a
        # price of "1" being displayed as "1.00000")
        #
        self.displayPrecision = kwargs.get("displayPrecision")
 
        #
        # The amount of decimal places that may be provided when specifying the
        # number of units traded for this instrument.
        #
        self.tradeUnitsPrecision = kwargs.get("tradeUnitsPrecision")
 
        #
        # The smallest number of units allowed to be traded for this
        # instrument.
        #
        self.minimumTradeSize = kwargs.get("minimumTradeSize")
 
        #
        # The maximum trailing stop distance allowed for a trailing stop loss
        # created for this instrument. Specified in price units.
        #
        self.maximumTrailingStopDistance = kwargs.get("maximumTrailingStopDistance")
 
        #
        # The minimum trailing stop distance allowed for a trailing stop loss
        # created for this instrument. Specified in price units.
        #
        self.minimumTrailingStopDistance = kwargs.get("minimumTrailingStopDistance")
 
        #
        # The maximum position size allowed for this instrument. Specified in
        # units.
        #
        self.maximumPositionSize = kwargs.get("maximumPositionSize")
 
        #
        # The maximum units allowed for an Order placed for this instrument.
        # Specified in units.
        #
        self.maximumOrderUnits = kwargs.get("maximumOrderUnits")
 
        #
        # The margin rate for this instrument.
        #
        self.marginRate = kwargs.get("marginRate")
 
        #
        # The commission structure for this instrument.
        #
        self.commission = kwargs.get("commission")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new Instrument from a dict (generally from loading a JSON
        response). The data used to instantiate the Instrument is a shallow
        copy of the dict passed in, with any complex child types instantiated
        appropriately.
        """

        data = data.copy()

        if data.get('minimumTradeSize') is not None:
            data['minimumTradeSize'] = ctx.convert_decimal_number(
                data.get('minimumTradeSize')
            )

        if data.get('maximumTrailingStopDistance') is not None:
            data['maximumTrailingStopDistance'] = ctx.convert_decimal_number(
                data.get('maximumTrailingStopDistance')
            )

        if data.get('minimumTrailingStopDistance') is not None:
            data['minimumTrailingStopDistance'] = ctx.convert_decimal_number(
                data.get('minimumTrailingStopDistance')
            )

        if data.get('maximumPositionSize') is not None:
            data['maximumPositionSize'] = ctx.convert_decimal_number(
                data.get('maximumPositionSize')
            )

        if data.get('maximumOrderUnits') is not None:
            data['maximumOrderUnits'] = ctx.convert_decimal_number(
                data.get('maximumOrderUnits')
            )

        if data.get('marginRate') is not None:
            data['marginRate'] = ctx.convert_decimal_number(
                data.get('marginRate')
            )

        if data.get('commission') is not None:
            data['commission'] = \
                ctx.primitives.InstrumentCommission.from_dict(
                    data['commission'], ctx
                )

        return Instrument(**data)


class InstrumentCommission(BaseEntity):
    """
    An InstrumentCommission represents an instrument-specific commission
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = ""

    #
    # Format string used when generating a name for this object
    #
    _name_format = ""

    #
    # Property metadata for this object
    #
    _properties = spec_properties.primitives_InstrumentCommission

    def __init__(self, **kwargs):
        """
        Create a new InstrumentCommission instance
        """
        super(InstrumentCommission, self).__init__()
 
        #
        # The commission amount (in the Account's home currency) charged per
        # unitsTraded of the instrument
        #
        self.commission = kwargs.get("commission")
 
        #
        # The number of units traded that the commission amount is based on.
        #
        self.unitsTraded = kwargs.get("unitsTraded")
 
        #
        # The minimum commission amount (in the Account's home currency) that
        # is charged when an Order is filled for this instrument.
        #
        self.minimumCommission = kwargs.get("minimumCommission")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new InstrumentCommission from a dict (generally from
        loading a JSON response). The data used to instantiate the
        InstrumentCommission is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('commission') is not None:
            data['commission'] = ctx.convert_decimal_number(
                data.get('commission')
            )

        if data.get('unitsTraded') is not None:
            data['unitsTraded'] = ctx.convert_decimal_number(
                data.get('unitsTraded')
            )

        if data.get('minimumCommission') is not None:
            data['minimumCommission'] = ctx.convert_decimal_number(
                data.get('minimumCommission')
            )

        return InstrumentCommission(**data)


class GuaranteedStopLossOrderLevelRestriction(BaseEntity):
    """
    A GuaranteedStopLossOrderLevelRestriction represents the total position
    size that can exist within a given price window for Trades with guaranteed
    Stop Loss Orders attached for a specific Instrument.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = ""

    #
    # Format string used when generating a name for this object
    #
    _name_format = ""

    #
    # Property metadata for this object
    #
    _properties = spec_properties.primitives_GuaranteedStopLossOrderLevelRestriction

    def __init__(self, **kwargs):
        """
        Create a new GuaranteedStopLossOrderLevelRestriction instance
        """
        super(GuaranteedStopLossOrderLevelRestriction, self).__init__()
 
        #
        # Applies to Trades with a guaranteed Stop Loss Order attached for the
        # specified Instrument. This is the total allowed Trade volume that can
        # exist within the priceRange based on the trigger prices of the
        # guaranteed Stop Loss Orders.
        #
        self.volume = kwargs.get("volume")
 
        #
        # The price range the volume applies to. This value is in price units.
        #
        self.priceRange = kwargs.get("priceRange")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new GuaranteedStopLossOrderLevelRestriction from a dict
        (generally from loading a JSON response). The data used to instantiate
        the GuaranteedStopLossOrderLevelRestriction is a shallow copy of the
        dict passed in, with any complex child types instantiated
        appropriately.
        """

        data = data.copy()

        if data.get('volume') is not None:
            data['volume'] = ctx.convert_decimal_number(
                data.get('volume')
            )

        if data.get('priceRange') is not None:
            data['priceRange'] = ctx.convert_decimal_number(
                data.get('priceRange')
            )

        return GuaranteedStopLossOrderLevelRestriction(**data)


class EntitySpec(object):
    """
    The primitives.EntitySpec wraps the primitives module's type definitions
    and API methods so they can be easily accessed through an instance of a v20
    Context.
    """

    Instrument = Instrument
    InstrumentCommission = InstrumentCommission
    GuaranteedStopLossOrderLevelRestriction = GuaranteedStopLossOrderLevelRestriction

    def __init__(self, ctx):
        self.ctx = ctx

