import ujson as json
from v20.base_entity import BaseEntity
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import spec_properties



class PriceBucket(BaseEntity):
    """
    A Price Bucket represents a price available for an amount of liquidity
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
    _properties = spec_properties.pricing_common_PriceBucket

    def __init__(self, **kwargs):
        """
        Create a new PriceBucket instance
        """
        super(PriceBucket, self).__init__()
 
        #
        # The Price offered by the PriceBucket
        #
        self.price = kwargs.get("price")
 
        #
        # The amount of liquidity offered by the PriceBucket
        #
        self.liquidity = kwargs.get("liquidity")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new PriceBucket from a dict (generally from loading a
        JSON response). The data used to instantiate the PriceBucket is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        return PriceBucket(**data)


class Price(BaseEntity):
    """
    The Price representation
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
    _properties = spec_properties.pricing_common_Price

    def __init__(self, **kwargs):
        """
        Create a new Price instance
        """
        super(Price, self).__init__()
 
        #
        # The Price's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # Flag indicating if the Price is tradeable or not
        #
        self.tradeable = kwargs.get("tradeable")
 
        #
        # The date/time when the Price was created.
        #
        self.timestamp = kwargs.get("timestamp")
 
        #
        # The base bid price as calculated by pricing.
        #
        self.baseBid = kwargs.get("baseBid")
 
        #
        # The base ask price as calculated by pricing.
        #
        self.baseAsk = kwargs.get("baseAsk")
 
        #
        # The list of prices and liquidity available on the Instrument's bid
        # side. It is possible for this list to be empty if there is no bid
        # liquidity currently available for the Instrument in the Account.
        #
        self.bids = kwargs.get("bids")
 
        #
        # The list of prices and liquidity available on the Instrument's ask
        # side. It is possible for this list to be empty if there is no ask
        # liquidity currently available for the Instrument in the Account.
        #
        self.asks = kwargs.get("asks")
 
        #
        # The closeout bid price. This price is used when a bid is required to
        # closeout a Position (margin closeout or manual) yet there is no bid
        # liquidity. The closeout bid is never used to open a new position.
        #
        self.closeoutBid = kwargs.get("closeoutBid")
 
        #
        # The closeout ask price. This price is used when an ask is required to
        # closeout a Position (margin closeout or manual) yet there is no ask
        # liquidity. The closeout ask is never used to open a new position.
        #
        self.closeoutAsk = kwargs.get("closeoutAsk")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new Price from a dict (generally from loading a JSON
        response). The data used to instantiate the Price is a shallow copy of
        the dict passed in, with any complex child types instantiated
        appropriately.
        """

        data = data.copy()

        if data.get('baseBid') is not None:
            data['baseBid'] = ctx.convert_decimal_number(
                data.get('baseBid')
            )

        if data.get('baseAsk') is not None:
            data['baseAsk'] = ctx.convert_decimal_number(
                data.get('baseAsk')
            )

        if data.get('bids') is not None:
            data['bids'] = [
                ctx.pricing_common.PriceBucket.from_dict(d, ctx)
                for d in data.get('bids')
            ]

        if data.get('asks') is not None:
            data['asks'] = [
                ctx.pricing_common.PriceBucket.from_dict(d, ctx)
                for d in data.get('asks')
            ]

        if data.get('closeoutBid') is not None:
            data['closeoutBid'] = ctx.convert_decimal_number(
                data.get('closeoutBid')
            )

        if data.get('closeoutAsk') is not None:
            data['closeoutAsk'] = ctx.convert_decimal_number(
                data.get('closeoutAsk')
            )

        return Price(**data)


class EntitySpec(object):
    """
    The pricing_common.EntitySpec wraps the pricing_common module's type definitions
    and API methods so they can be easily accessed through an instance of a v20
    Context.
    """

    PriceBucket = PriceBucket
    Price = Price

    def __init__(self, ctx):
        self.ctx = ctx

