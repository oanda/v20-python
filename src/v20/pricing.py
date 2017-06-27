import ujson as json
from v20.base_entity import BaseEntity
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import spec_properties



class Price(BaseEntity):
    """
    The specification of an Account-specific Price.
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
    _properties = spec_properties.pricing_Price

    def __init__(self, **kwargs):
        """
        Create a new Price instance
        """
        super(Price, self).__init__()
 
        #
        # The string "PRICE". Used to identify the a Price object when found in
        # a stream.
        #
        self.type = kwargs.get("type", "PRICE")
 
        #
        # The Price's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The date/time when the Price was created
        #
        self.time = kwargs.get("time")
 
        #
        # The status of the Price.
        #
        self.status = kwargs.get("status")
 
        #
        # Flag indicating if the Price is tradeable or not
        #
        self.tradeable = kwargs.get("tradeable")
 
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
        # The closeout bid Price. This Price is used when a bid is required to
        # closeout a Position (margin closeout or manual) yet there is no bid
        # liquidity. The closeout bid is never used to open a new position.
        #
        self.closeoutBid = kwargs.get("closeoutBid")
 
        #
        # The closeout ask Price. This Price is used when a ask is required to
        # closeout a Position (margin closeout or manual) yet there is no ask
        # liquidity. The closeout ask is never used to open a new position.
        #
        self.closeoutAsk = kwargs.get("closeoutAsk")
 
        #
        # The factors used to convert quantities of this price's Instrument's
        # quote currency into a quantity of the Account's home currency.
        #
        self.quoteHomeConversionFactors = kwargs.get("quoteHomeConversionFactors")
 
        #
        # Representation of how many units of an Instrument are available to be
        # traded by an Order depending on its postionFill option.
        #
        self.unitsAvailable = kwargs.get("unitsAvailable")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new Price from a dict (generally from loading a JSON
        response). The data used to instantiate the Price is a shallow copy of
        the dict passed in, with any complex child types instantiated
        appropriately.
        """

        data = data.copy()

        if data.get('bids') is not None:
            data['bids'] = [
                ctx.pricing.PriceBucket.from_dict(d, ctx)
                for d in data.get('bids')
            ]

        if data.get('asks') is not None:
            data['asks'] = [
                ctx.pricing.PriceBucket.from_dict(d, ctx)
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

        if data.get('quoteHomeConversionFactors') is not None:
            data['quoteHomeConversionFactors'] = \
                ctx.pricing.QuoteHomeConversionFactors.from_dict(
                    data['quoteHomeConversionFactors'], ctx
                )

        if data.get('unitsAvailable') is not None:
            data['unitsAvailable'] = \
                ctx.order.UnitsAvailable.from_dict(
                    data['unitsAvailable'], ctx
                )

        return Price(**data)


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
    _properties = spec_properties.pricing_PriceBucket

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


class QuoteHomeConversionFactors(BaseEntity):
    """
    QuoteHomeConversionFactors represents the factors that can be used used to
    convert quantities of a Price's Instrument's quote currency into the
    Account's home currency.
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
    _properties = spec_properties.pricing_QuoteHomeConversionFactors

    def __init__(self, **kwargs):
        """
        Create a new QuoteHomeConversionFactors instance
        """
        super(QuoteHomeConversionFactors, self).__init__()
 
        #
        # The factor used to convert a positive amount of the Price's
        # Instrument's quote currency into a positive amount of the Account's
        # home currency.  Conversion is performed by multiplying the quote
        # units by the conversion factor.
        #
        self.positiveUnits = kwargs.get("positiveUnits")
 
        #
        # The factor used to convert a negative amount of the Price's
        # Instrument's quote currency into a negative amount of the Account's
        # home currency.  Conversion is performed by multiplying the quote
        # units by the conversion factor.
        #
        self.negativeUnits = kwargs.get("negativeUnits")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new QuoteHomeConversionFactors from a dict (generally
        from loading a JSON response). The data used to instantiate the
        QuoteHomeConversionFactors is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('positiveUnits') is not None:
            data['positiveUnits'] = ctx.convert_decimal_number(
                data.get('positiveUnits')
            )

        if data.get('negativeUnits') is not None:
            data['negativeUnits'] = ctx.convert_decimal_number(
                data.get('negativeUnits')
            )

        return QuoteHomeConversionFactors(**data)


class ClientPrice(BaseEntity):
    """
    Client price for an Account.
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
    _properties = spec_properties.pricing_ClientPrice

    def __init__(self, **kwargs):
        """
        Create a new ClientPrice instance
        """
        super(ClientPrice, self).__init__()
 
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
        # The closeout bid Price. This Price is used when a bid is required to
        # closeout a Position (margin closeout or manual) yet there is no bid
        # liquidity. The closeout bid is never used to open a new position.
        #
        self.closeoutBid = kwargs.get("closeoutBid")
 
        #
        # The closeout ask Price. This Price is used when a ask is required to
        # closeout a Position (margin closeout or manual) yet there is no ask
        # liquidity. The closeout ask is never used to open a new position.
        #
        self.closeoutAsk = kwargs.get("closeoutAsk")
 
        #
        # The date/time when the Price was created.
        #
        self.timestamp = kwargs.get("timestamp")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new ClientPrice from a dict (generally from loading a
        JSON response). The data used to instantiate the ClientPrice is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('bids') is not None:
            data['bids'] = [
                ctx.pricing.PriceBucket.from_dict(d, ctx)
                for d in data.get('bids')
            ]

        if data.get('asks') is not None:
            data['asks'] = [
                ctx.pricing.PriceBucket.from_dict(d, ctx)
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

        return ClientPrice(**data)


class PricingHeartbeat(BaseEntity):
    """
    A PricingHeartbeat object is injected into the Pricing stream to ensure
    that the HTTP connection remains active.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Pricing Heartbeat {time}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = ""

    #
    # Property metadata for this object
    #
    _properties = spec_properties.pricing_PricingHeartbeat

    def __init__(self, **kwargs):
        """
        Create a new PricingHeartbeat instance
        """
        super(PricingHeartbeat, self).__init__()
 
        #
        # The string "HEARTBEAT"
        #
        self.type = kwargs.get("type", "HEARTBEAT")
 
        #
        # The date/time when the Heartbeat was created.
        #
        self.time = kwargs.get("time")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new PricingHeartbeat from a dict (generally from loading
        a JSON response). The data used to instantiate the PricingHeartbeat is
        a shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        return PricingHeartbeat(**data)


class EntitySpec(object):
    """
    The pricing.EntitySpec wraps the pricing module's type definitions
    and API methods so they can be easily accessed through an instance of a v20
    Context.
    """

    Price = Price
    PriceBucket = PriceBucket
    QuoteHomeConversionFactors = QuoteHomeConversionFactors
    ClientPrice = ClientPrice
    PricingHeartbeat = PricingHeartbeat

    def __init__(self, ctx):
        self.ctx = ctx


    def get(
        self,
        accountID,
        **kwargs
    ):
        """
        Get pricing information for a specified list of Instruments within an
        Account.

        Args:
            accountID:
                Account Identifier
            instruments:
                List of Instruments to get pricing for.
            since:
                Date/Time filter to apply to the returned prices. Only prices
                with a time later than this filter will be provided.
            includeUnitsAvailable:
                Flag that enables the inclusion of the unitsAvailable field in
                the returned Price objects.

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('prices') is not None:
                parsed_body['prices'] = [
                    self.ctx.pricing.Price.from_dict(d, self.ctx)
                    for d in jbody.get('prices')
                ]

        elif str(response.status) == "400":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        elif str(response.status) == "401":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        elif str(response.status) == "404":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        elif str(response.status) == "405":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        #
        # Unexpected response status
        #
        else:
            parsed_body = jbody

        response.body = parsed_body

        return response


    def stream(
        self,
        accountID,
        **kwargs
    ):
        """
        Get a stream of Account Prices starting from when the request is made.
        This pricing stream does not include every single price created for the
        Account, but instead will provide at most 4 prices per second (every
        250 milliseconds) for each instrument being requested. If more than one
        price is created for an instrument during the 250 millisecond window,
        only the price in effect at the end of the window is sent. This means
        that during periods of rapid price movement, subscribers to this stream
        will not be sent every price. Pricing windows for different connections
        to the price stream are not all aligned in the same way (i.e. they are
        not all aligned to the top of the second). This means that during
        periods of rapid price movement, different subscribers may observe
        different prices depending on their alignment.

        Args:
            accountID:
                Account Identifier
            instruments:
                List of Instruments to stream Prices for.
            snapshot:
                Flag that enables/disables the sending of a pricing snapshot
                when initially connecting to the stream.

        Returns:
            v20.response.Response containing the results from submitting the
            request
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
                j = json.loads(line.decode('utf-8'))

                type = j.get("type")

                if type is None:
                    return (
                        "pricing.Price",
                        self.ctx.pricing.Price.from_dict(j, self.ctx)
                    )
                elif type == "HEARTBEAT":
                    return (
                        "pricing.PricingHeartbeat",
                        self.ctx.pricing.PricingHeartbeat.from_dict(j, self.ctx)
                    )

                return (
                    "pricing.Price",
                    self.ctx.pricing.Price.from_dict(j, self.ctx)
                )

                
        request.set_line_parser(
            Parser(self.ctx)
        )

        response = self.ctx.request(request)


        return response

