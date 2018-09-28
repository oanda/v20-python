import ujson as json
from v20.base_entity import BaseEntity
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import spec_properties



class ClientPrice(BaseEntity):
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
    _properties = spec_properties.pricing_ClientPrice

    def __init__(self, **kwargs):
        """
        Create a new ClientPrice instance
        """
        super(ClientPrice, self).__init__()
 
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
        # quote currency into a quantity of the Account's home currency. When
        # the includeHomeConversions is present in the pricing request
        # (regardless of its value), this field will not be present.
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
        Instantiate a new ClientPrice from a dict (generally from loading a
        JSON response). The data used to instantiate the ClientPrice is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

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

        return ClientPrice(**data)


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


class HomeConversions(BaseEntity):
    """
    HomeConversions represents the factors to use to convert quantities of a
    given currency into the Account's home currency. The conversion factor
    depends on the scenario the conversion is required for.
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
    _properties = spec_properties.pricing_HomeConversions

    def __init__(self, **kwargs):
        """
        Create a new HomeConversions instance
        """
        super(HomeConversions, self).__init__()
 
        #
        # The currency to be converted into the home currency.
        #
        self.currency = kwargs.get("currency")
 
        #
        # The factor used to convert any gains for an Account in the specified
        # currency into the Account's home currency. This would include
        # positive realized P/L and positive financing amounts. Conversion is
        # performed by multiplying the positive P/L by the conversion factor.
        #
        self.accountGain = kwargs.get("accountGain")
 
        #
        # The string representation of a decimal number.
        #
        self.accountLoss = kwargs.get("accountLoss")
 
        #
        # The factor used to convert a Position or Trade Value in the specified
        # currency into the Account's home currency. Conversion is performed by
        # multiplying the Position or Trade Value by the conversion factor.
        #
        self.positionValue = kwargs.get("positionValue")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new HomeConversions from a dict (generally from loading a
        JSON response). The data used to instantiate the HomeConversions is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('accountGain') is not None:
            data['accountGain'] = ctx.convert_decimal_number(
                data.get('accountGain')
            )

        if data.get('accountLoss') is not None:
            data['accountLoss'] = ctx.convert_decimal_number(
                data.get('accountLoss')
            )

        if data.get('positionValue') is not None:
            data['positionValue'] = ctx.convert_decimal_number(
                data.get('positionValue')
            )

        return HomeConversions(**data)


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

    ClientPrice = ClientPrice
    QuoteHomeConversionFactors = QuoteHomeConversionFactors
    HomeConversions = HomeConversions
    PricingHeartbeat = PricingHeartbeat

    def __init__(self, ctx):
        self.ctx = ctx


    def base_prices(
        self,
        **kwargs
    ):
        """
        Get pricing information for a specified instrument. Accounts are not
        associated in any way with this endpoint.

        Args:
            time:
                The time at which the desired price for each instrument is in
                effect. The current price for each instrument is returned if no
                time is provided.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/pricing'
        )

        request.set_param(
            'time',
            kwargs.get('time')
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
                    self.ctx.pricing_common.Price.from_dict(d, self.ctx)
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


    def get_price_range(
        self,
        instrument,
        **kwargs
    ):
        """
        Get pricing information for a specified range of prices. Accounts are
        not associated in any way with this endpoint.

        Args:
            instrument:
                Name of the Instrument
            fromTime:
                The start of the time range to fetch prices for.
            toTime:
                The end of the time range to fetch prices for. The current time
                is used if this parameter is not provided.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/pricing/range'
        )

        request.set_path_param(
            'instrument',
            instrument
        )

        request.set_param(
            'from',
            kwargs.get('fromTime')
        )

        request.set_param(
            'to',
            kwargs.get('toTime')
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
                    self.ctx.pricing_common.Price.from_dict(d, self.ctx)
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
                Date/Time filter to apply to the response. Only prices and home
                conversions (if requested) with a time later than this filter
                (i.e. the price has changed after the since time) will be
                provided, and are filtered independently.
            includeUnitsAvailable:
                Flag that enables the inclusion of the unitsAvailable field in
                the returned Price objects.
            includeHomeConversions:
                Flag that enables the inclusion of the homeConversions field in
                the returned response. An entry will be returned for each
                currency in the set of all base and quote currencies present in
                the requested instruments list.

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

        request.set_param(
            'includeHomeConversions',
            kwargs.get('includeHomeConversions')
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
                    self.ctx.pricing.ClientPrice.from_dict(d, self.ctx)
                    for d in jbody.get('prices')
                ]

            if jbody.get('homeConversions') is not None:
                parsed_body['homeConversions'] = [
                    self.ctx.pricing.HomeConversions.from_dict(d, self.ctx)
                    for d in jbody.get('homeConversions')
                ]

            if jbody.get('time') is not None:
                parsed_body['time'] = \
                    jbody.get('time')

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
                        "pricing.ClientPrice",
                        self.ctx.pricing.ClientPrice.from_dict(j, self.ctx)
                    )
                elif type == "HEARTBEAT":
                    return (
                        "pricing.PricingHeartbeat",
                        self.ctx.pricing.PricingHeartbeat.from_dict(j, self.ctx)
                    )

                return (
                    "pricing.ClientPrice",
                    self.ctx.pricing.ClientPrice.from_dict(j, self.ctx)
                )

                
        request.set_line_parser(
            Parser(self.ctx)
        )

        response = self.ctx.request(request)


        return response


    def candles(
        self,
        instrument,
        **kwargs
    ):
        """
        Fetch candlestick data for an instrument.

        Args:
            instrument:
                Name of the Instrument
            price:
                The Price component(s) to get candlestick data for. Can contain
                any combination of the characters "M" (midpoint candles) "B"
                (bid candles) and "A" (ask candles).
            granularity:
                The granularity of the candlesticks to fetch
            count:
                The number of candlesticks to return in the response. Count
                should not be specified if both the start and end parameters
                are provided, as the time range combined with the granularity
                will determine the number of candlesticks to return.
            fromTime:
                The start of the time range to fetch candlesticks for.
            toTime:
                The end of the time range to fetch candlesticks for.
            smooth:
                A flag that controls whether the candlestick is "smoothed" or
                not.  A smoothed candlestick uses the previous candle's close
                price as its open price, while an unsmoothed candlestick uses
                the first price from its time range as its open price.
            includeFirst:
                A flag that controls whether the candlestick that is covered by
                the from time should be included in the results. This flag
                enables clients to use the timestamp of the last completed
                candlestick received to poll for future candlesticks but avoid
                receiving the previous candlestick repeatedly.
            dailyAlignment:
                The hour of the day (in the specified timezone) to use for
                granularities that have daily alignments.
            alignmentTimezone:
                The timezone to use for the dailyAlignment parameter.
                Candlesticks with daily alignment will be aligned to the
                dailyAlignment hour within the alignmentTimezone.  Note that
                the returned times will still be represented in UTC.
            weeklyAlignment:
                The day of the week used for granularities that have weekly
                alignment.
            units:
                The number of units used to calculate the volume-weighted
                average bid and ask prices in the returned candles.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/accounts/{accountID}/instruments/{instrument}/candles'
        )

        request.set_path_param(
            'instrument',
            instrument
        )

        request.set_param(
            'price',
            kwargs.get('price')
        )

        request.set_param(
            'granularity',
            kwargs.get('granularity')
        )

        request.set_param(
            'count',
            kwargs.get('count')
        )

        request.set_param(
            'from',
            kwargs.get('fromTime')
        )

        request.set_param(
            'to',
            kwargs.get('toTime')
        )

        request.set_param(
            'smooth',
            kwargs.get('smooth')
        )

        request.set_param(
            'includeFirst',
            kwargs.get('includeFirst')
        )

        request.set_param(
            'dailyAlignment',
            kwargs.get('dailyAlignment')
        )

        request.set_param(
            'alignmentTimezone',
            kwargs.get('alignmentTimezone')
        )

        request.set_param(
            'weeklyAlignment',
            kwargs.get('weeklyAlignment')
        )

        request.set_param(
            'units',
            kwargs.get('units')
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
            if jbody.get('instrument') is not None:
                parsed_body['instrument'] = \
                    jbody.get('instrument')

            if jbody.get('granularity') is not None:
                parsed_body['granularity'] = \
                    jbody.get('granularity')

            if jbody.get('candles') is not None:
                parsed_body['candles'] = [
                    self.ctx.instrument.Candlestick.from_dict(d, self.ctx)
                    for d in jbody.get('candles')
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

