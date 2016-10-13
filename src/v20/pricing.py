import json
from v20.base_entity import BaseEntity
from v20.base_entity import Property
from v20.base_entity import EntityDict
from v20.request import Request



class Price(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "instrument",
            "instrument",
            "The Price's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            False,
            None
        ),
        Property(
            "time",
            "time",
            "The date/time when the Price was created",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "status",
            "status",
            "The status of the Price.",
            "primitive",
            "pricing.PriceStatus",
            False,
            None
        ),
        Property(
            "bids",
            "bids",
            "The list of prices and liquidity available on the Instrument's bid side. It is possible for this list to be empty if there is no bid liquidity currently available for the Instrument in the Account.",
            "array_object",
            "PriceBucket",
            False,
            None
        ),
        Property(
            "asks",
            "asks",
            "The list of prices and liquidity available on the Instrument's ask side. It is possible for this list to be empty if there is no ask liquidity currently available for the Instrument in the Account.",
            "array_object",
            "PriceBucket",
            False,
            None
        ),
        Property(
            "closeoutBid",
            "closeoutBid",
            "The closeout bid Price. This Price is used when a bid is required to closeout a Position (margin closeout or manual) yet there is no bid liquidity. The closeout bid is never used to open a new position.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "closeoutAsk",
            "closeoutAsk",
            "The closeout ask Price. This Price is used when a ask is required to closeout a Position (margin closeout or manual) yet there is no ask liquidity. The closeout ask is never used to open a new position.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "quoteHomeConversionFactors",
            "quoteHomeConversionFactors",
            "The factors used to convert quantities of this price's Instrument's quote currency into a quantity of the Account's home currency.",
            "object",
            "pricing.QuoteHomeConversionFactors",
            False,
            None
        ),
        Property(
            "unitsAvailable",
            "unitsAvailable",
            "Representation of many units of an Instrument are available to be traded for both long and short Orders.",
            "object",
            "pricing.UnitsAvailable",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(Price, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('status') is not None:
            body['status'] = \
                data.get('status')

        if data.get('bids') is not None:
            body['bids'] = [
                PriceBucket.from_dict(d)
                for d in data.get('bids')
            ]

        if data.get('asks') is not None:
            body['asks'] = [
                PriceBucket.from_dict(d)
                for d in data.get('asks')
            ]

        if data.get('closeoutBid') is not None:
            body['closeoutBid'] = \
                data.get('closeoutBid')

        if data.get('closeoutAsk') is not None:
            body['closeoutAsk'] = \
                data.get('closeoutAsk')

        if data.get('quoteHomeConversionFactors') is not None:
            body['quoteHomeConversionFactors'] = \
                QuoteHomeConversionFactors.from_dict(
                    data['quoteHomeConversionFactors']
                )

        if data.get('unitsAvailable') is not None:
            body['unitsAvailable'] = \
                UnitsAvailable.from_dict(
                    data['unitsAvailable']
                )

        self = Price(**body)

        return self


class PriceBucket(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "price",
            "price",
            "The Price offered by the PriceBucket",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "liquidity",
            "liquidity",
            "The amount of liquidity offered by the PriceBucket",
            "primitive",
            "integer",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(PriceBucket, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('liquidity') is not None:
            body['liquidity'] = \
                data.get('liquidity')

        self = PriceBucket(**body)

        return self


class UnitsAvailable(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "long",
            "long",
            "The units available breakdown for long Orders.",
            "object",
            "pricing.UnitsAvailableDetails",
            False,
            None
        ),
        Property(
            "short",
            "short",
            "The units available breakdown for short Orders.",
            "object",
            "pricing.UnitsAvailableDetails",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(UnitsAvailable, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('long') is not None:
            body['long'] = \
                UnitsAvailableDetails.from_dict(
                    data['long']
                )

        if data.get('short') is not None:
            body['short'] = \
                UnitsAvailableDetails.from_dict(
                    data['short']
                )

        self = UnitsAvailable(**body)

        return self


class UnitsAvailableDetails(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "default",
            "default",
            "The number of units that are available to be traded using an Order with a positionFill option of \"DEFAULT\". For an Account with hedging enabled, this value will be the same as the \"OPEN_ONLY\" value. For an Account without hedging enabled, this value will be the same as the \"REDUCE_FIRST\" value.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "reduceFirst",
            "reduceFirst",
            "The number of units that may are available to be traded with an Order with a positionFill option of \"REDUCE_FIRST\".",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "reduceOnly",
            "reduceOnly",
            "The number of units that may are available to be traded with an Order with a positionFill option of \"REDUCE_ONLY\".",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "openOnly",
            "openOnly",
            "The number of units that may are available to be traded with an Order with a positionFill option of \"OPEN_ONLY\".",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(UnitsAvailableDetails, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('default') is not None:
            body['default'] = \
                data.get('default')

        if data.get('reduceFirst') is not None:
            body['reduceFirst'] = \
                data.get('reduceFirst')

        if data.get('reduceOnly') is not None:
            body['reduceOnly'] = \
                data.get('reduceOnly')

        if data.get('openOnly') is not None:
            body['openOnly'] = \
                data.get('openOnly')

        self = UnitsAvailableDetails(**body)

        return self


class QuoteHomeConversionFactors(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "positiveUnits",
            "positiveUnits",
            "The factor used to convert a positive amount of the Price's Instrument's quote currency into a positive amount of the Account's home currency.  Conversion is performed by multiplying the quote units by the conversion factor.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "negativeUnits",
            "negativeUnits",
            "The factor used to convert a negative amount of the Price's Instrument's quote currency into a negative amount of the Account's home currency.  Conversion is performed by multiplying the quote units by the conversion factor.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(QuoteHomeConversionFactors, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('positiveUnits') is not None:
            body['positiveUnits'] = \
                data.get('positiveUnits')

        if data.get('negativeUnits') is not None:
            body['negativeUnits'] = \
                data.get('negativeUnits')

        self = QuoteHomeConversionFactors(**body)

        return self


class Heartbeat(BaseEntity):
    _summary_format = "Pricing Heartbeat {time}"
    _name_format = ""

    _properties = [
        Property(
            "type",
            "type",
            "The string \"HEARTBEAT\"",
            "primitive",
            "string",
            False,
            "HEARTBEAT"
        ),
        Property(
            "time",
            "time",
            "The date/time when the Heartbeat was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(Heartbeat, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        self = Heartbeat(**body)

        return self

class EntitySpec(object):
    Price = Price
    PriceBucket = PriceBucket
    UnitsAvailable = UnitsAvailable
    UnitsAvailableDetails = UnitsAvailableDetails
    QuoteHomeConversionFactors = QuoteHomeConversionFactors
    Heartbeat = Heartbeat

    def __init__(self, ctx):
        self.ctx = ctx


    def get(
        self,
        accountID,
        **kwargs
    ):
        """Current Prices

        Get pricing information for a specified list of Instruments within an
        Account.

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch current Prices for.
        instruments : array, optional
            List of Instruments to get pricing for.
        since : , optional
            Date/Time filter to apply to the returned prices. Only prices with
            a time later than this filter will be provided.
        includeUnitsAvailable : , optional
            Flag that enables the inclusion of the unitsAvailable field in the
            returned Price objects.
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/pricing'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_param(
            'instruments',
            kwargs.get('instruments')
        )

        request.set_param(
            'since',
            kwargs.get('since')
        )

        request.set_param(
            'includeUnitsAvailable',
            kwargs.get('includeUnitsAvailable')
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('prices') is not None:
                parsed_body['prices'] = [
                    Price.from_dict(d)
                    for d in jbody.get('prices')
                ]


        if str(response.status) == "400":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')


        if str(response.status) == "401":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')


        if str(response.status) == "404":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')


        if str(response.status) == "405":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')


        response.body = parsed_body

        return response


    def stream(
        self,
        accountID,
        **kwargs
    ):
        """Price Stream

        Get a stream of Prices for an Account starting from when the request is
        made.

        Parameters
        ----------
        accountID : 
            ID of the Account to stream Prices for.
        instruments : array, optional
            List of Instruments to stream Prices for.
        snapshot : , optional
            Flag that enables/disables the sending of a pricing snapshot when
            initially connecting to the stream.
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/pricing/stream'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_param(
            'instruments',
            kwargs.get('instruments')
        )

        request.set_param(
            'snapshot',
            kwargs.get('snapshot')
        )

        request.set_stream(True)

        class Parser():
            def __init__(self, ctx):
                self.ctx = ctx

            def __call__(self, line):
                j = json.loads(line)

                type = j.get("type")

                if type is None:
                    return (
                        "pricing.Price",
                        self.ctx.pricing.Price.from_dict(j)
                    )
                elif type == "HEARTBEAT":
                    return (
                        "pricing.Heartbeat",
                        self.ctx.pricing.Heartbeat.from_dict(j)
                    )

                return (
                    "pricing.Price",
                    self.ctx.pricing.Price.from_dict(j)
                )

                
        request.set_line_parser(
            Parser(self.ctx)
        )

        response = self.ctx.request(request)


        return response

