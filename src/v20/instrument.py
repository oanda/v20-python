import ujson as json
from v20.base_entity import BaseEntity
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import spec_properties



class Candlestick(BaseEntity):
    """
    The Candlestick representation
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
    _properties = spec_properties.instrument_Candlestick

    def __init__(self, **kwargs):
        """
        Create a new Candlestick instance
        """
        super(Candlestick, self).__init__()
 
        #
        # The start time of the candlestick
        #
        self.time = kwargs.get("time")
 
        #
        # The candlestick data based on bids. Only provided if bid-based
        # candles were requested.
        #
        self.bid = kwargs.get("bid")
 
        #
        # The candlestick data based on asks. Only provided if ask-based
        # candles were requested.
        #
        self.ask = kwargs.get("ask")
 
        #
        # The candlestick data based on midpoints. Only provided if midpoint-
        # based candles were requested.
        #
        self.mid = kwargs.get("mid")
 
        #
        # The number of prices created during the time-range represented by the
        # candlestick.
        #
        self.volume = kwargs.get("volume")
 
        #
        # A flag indicating if the candlestick is complete. A complete
        # candlestick is one whose ending time is not in the future.
        #
        self.complete = kwargs.get("complete")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new Candlestick from a dict (generally from loading a
        JSON response). The data used to instantiate the Candlestick is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('bid') is not None:
            data['bid'] = \
                ctx.instrument.CandlestickData.from_dict(
                    data['bid'], ctx
                )

        if data.get('ask') is not None:
            data['ask'] = \
                ctx.instrument.CandlestickData.from_dict(
                    data['ask'], ctx
                )

        if data.get('mid') is not None:
            data['mid'] = \
                ctx.instrument.CandlestickData.from_dict(
                    data['mid'], ctx
                )

        return Candlestick(**data)


class CandlestickData(BaseEntity):
    """
    The price data (open, high, low, close) for the Candlestick representation.
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
    _properties = spec_properties.instrument_CandlestickData

    def __init__(self, **kwargs):
        """
        Create a new CandlestickData instance
        """
        super(CandlestickData, self).__init__()
 
        #
        # The first (open) price in the time-range represented by the
        # candlestick.
        #
        self.o = kwargs.get("o")
 
        #
        # The highest price in the time-range represented by the candlestick.
        #
        self.h = kwargs.get("h")
 
        #
        # The lowest price in the time-range represented by the candlestick.
        #
        self.l = kwargs.get("l")
 
        #
        # The last (closing) price in the time-range represented by the
        # candlestick.
        #
        self.c = kwargs.get("c")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new CandlestickData from a dict (generally from loading a
        JSON response). The data used to instantiate the CandlestickData is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('o') is not None:
            data['o'] = ctx.convert_decimal_number(
                data.get('o')
            )

        if data.get('h') is not None:
            data['h'] = ctx.convert_decimal_number(
                data.get('h')
            )

        if data.get('l') is not None:
            data['l'] = ctx.convert_decimal_number(
                data.get('l')
            )

        if data.get('c') is not None:
            data['c'] = ctx.convert_decimal_number(
                data.get('c')
            )

        return CandlestickData(**data)


class OrderBook(BaseEntity):
    """
    The representation of an instrument's order book at a point in time
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
    _properties = spec_properties.instrument_OrderBook

    def __init__(self, **kwargs):
        """
        Create a new OrderBook instance
        """
        super(OrderBook, self).__init__()
 
        #
        # The order book's instrument
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The time when the order book snapshot was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The price (midpoint) for the order book's instrument at the time of
        # the order book snapshot
        #
        self.price = kwargs.get("price")
 
        #
        # The price width for each bucket. Each bucket covers the price range
        # from the bucket's price to the bucket's price + bucketWidth.
        #
        self.bucketWidth = kwargs.get("bucketWidth")
 
        #
        # The partitioned order book, divided into buckets using a default
        # bucket width. These buckets are only provided for price ranges which
        # actually contain order or position data.
        #
        self.buckets = kwargs.get("buckets")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new OrderBook from a dict (generally from loading a JSON
        response). The data used to instantiate the OrderBook is a shallow copy
        of the dict passed in, with any complex child types instantiated
        appropriately.
        """

        data = data.copy()

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('bucketWidth') is not None:
            data['bucketWidth'] = ctx.convert_decimal_number(
                data.get('bucketWidth')
            )

        if data.get('buckets') is not None:
            data['buckets'] = [
                ctx.instrument.OrderBookBucket.from_dict(d, ctx)
                for d in data.get('buckets')
            ]

        return OrderBook(**data)


class OrderBookBucket(BaseEntity):
    """
    The order book data for a partition of the instrument's prices.
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
    _properties = spec_properties.instrument_OrderBookBucket

    def __init__(self, **kwargs):
        """
        Create a new OrderBookBucket instance
        """
        super(OrderBookBucket, self).__init__()
 
        #
        # The lowest price (inclusive) covered by the bucket. The bucket covers
        # the price range from the price to price + the order book's
        # bucketWidth.
        #
        self.price = kwargs.get("price")
 
        #
        # The percentage of the total number of orders represented by the long
        # orders found in this bucket.
        #
        self.longCountPercent = kwargs.get("longCountPercent")
 
        #
        # The percentage of the total number of orders represented by the short
        # orders found in this bucket.
        #
        self.shortCountPercent = kwargs.get("shortCountPercent")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new OrderBookBucket from a dict (generally from loading a
        JSON response). The data used to instantiate the OrderBookBucket is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('longCountPercent') is not None:
            data['longCountPercent'] = ctx.convert_decimal_number(
                data.get('longCountPercent')
            )

        if data.get('shortCountPercent') is not None:
            data['shortCountPercent'] = ctx.convert_decimal_number(
                data.get('shortCountPercent')
            )

        return OrderBookBucket(**data)


class PositionBook(BaseEntity):
    """
    The representation of an instrument's position book at a point in time
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
    _properties = spec_properties.instrument_PositionBook

    def __init__(self, **kwargs):
        """
        Create a new PositionBook instance
        """
        super(PositionBook, self).__init__()
 
        #
        # The position book's instrument
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The time when the position book snapshot was created
        #
        self.time = kwargs.get("time")
 
        #
        # The price (midpoint) for the position book's instrument at the time
        # of the position book snapshot
        #
        self.price = kwargs.get("price")
 
        #
        # The price width for each bucket. Each bucket covers the price range
        # from the bucket's price to the bucket's price + bucketWidth.
        #
        self.bucketWidth = kwargs.get("bucketWidth")
 
        #
        # The partitioned position book, divided into buckets using a default
        # bucket width. These buckets are only provided for price ranges which
        # actually contain order or position data.
        #
        self.buckets = kwargs.get("buckets")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new PositionBook from a dict (generally from loading a
        JSON response). The data used to instantiate the PositionBook is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('bucketWidth') is not None:
            data['bucketWidth'] = ctx.convert_decimal_number(
                data.get('bucketWidth')
            )

        if data.get('buckets') is not None:
            data['buckets'] = [
                ctx.instrument.PositionBookBucket.from_dict(d, ctx)
                for d in data.get('buckets')
            ]

        return PositionBook(**data)


class PositionBookBucket(BaseEntity):
    """
    The position book data for a partition of the instrument's prices.
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
    _properties = spec_properties.instrument_PositionBookBucket

    def __init__(self, **kwargs):
        """
        Create a new PositionBookBucket instance
        """
        super(PositionBookBucket, self).__init__()
 
        #
        # The lowest price (inclusive) covered by the bucket. The bucket covers
        # the price range from the price to price + the position book's
        # bucketWidth.
        #
        self.price = kwargs.get("price")
 
        #
        # The percentage of the total number of positions represented by the
        # long positions found in this bucket.
        #
        self.longCountPercent = kwargs.get("longCountPercent")
 
        #
        # The percentage of the total number of positions represented by the
        # short positions found in this bucket.
        #
        self.shortCountPercent = kwargs.get("shortCountPercent")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new PositionBookBucket from a dict (generally from
        loading a JSON response). The data used to instantiate the
        PositionBookBucket is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('longCountPercent') is not None:
            data['longCountPercent'] = ctx.convert_decimal_number(
                data.get('longCountPercent')
            )

        if data.get('shortCountPercent') is not None:
            data['shortCountPercent'] = ctx.convert_decimal_number(
                data.get('shortCountPercent')
            )

        return PositionBookBucket(**data)


class EntitySpec(object):
    """
    The instrument.EntitySpec wraps the instrument module's type definitions
    and API methods so they can be easily accessed through an instance of a v20
    Context.
    """

    Candlestick = Candlestick
    CandlestickData = CandlestickData
    OrderBook = OrderBook
    OrderBookBucket = OrderBookBucket
    PositionBook = PositionBook
    PositionBookBucket = PositionBookBucket

    def __init__(self, ctx):
        self.ctx = ctx


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
                The number of candlesticks to return in the reponse. Count
                should not be specified if both the start and end parameters
                are provided, as the time range combined with the graularity
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

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/instruments/{instrument}/candles'
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


    def price(
        self,
        instrument,
        **kwargs
    ):
        """
        Fetch a price for an instrument. Accounts are not associated in any way
        with this endpoint.

        Args:
            instrument:
                Name of the Instrument
            time:
                The time at which the desired price is in effect. The current
                price is returned if no time is provided.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/instruments/{instrument}/price'
        )

        request.set_path_param(
            'instrument',
            instrument
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
            if jbody.get('price') is not None:
                parsed_body['price'] = \
                    self.ctx.pricing_common.Price.from_dict(
                        jbody['price'],
                        self.ctx
                    )

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


    def prices(
        self,
        instrument,
        **kwargs
    ):
        """
        Fetch a range of prices for an instrument. Accounts are not associated
        in any way with this endpoint.

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
            '/v3/instruments/{instrument}/price/range'
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


    def order_book(
        self,
        instrument,
        **kwargs
    ):
        """
        Fetch an order book for an instrument.

        Args:
            instrument:
                Name of the Instrument
            time:
                The time of the snapshot to fetch. If not specified, then the
                most recent snapshot is fetched.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/instruments/{instrument}/orderBook'
        )

        request.set_path_param(
            'instrument',
            instrument
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
            if jbody.get('orderBook') is not None:
                parsed_body['orderBook'] = \
                    self.ctx.instrument.OrderBook.from_dict(
                        jbody['orderBook'],
                        self.ctx
                    )

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


    def position_book(
        self,
        instrument,
        **kwargs
    ):
        """
        Fetch a position book for an instrument.

        Args:
            instrument:
                Name of the Instrument
            time:
                The time of the snapshot to fetch. If not specified, then the
                most recent snapshot is fetched.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/instruments/{instrument}/positionBook'
        )

        request.set_path_param(
            'instrument',
            instrument
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
            if jbody.get('positionBook') is not None:
                parsed_body['positionBook'] = \
                    self.ctx.instrument.PositionBook.from_dict(
                        jbody['positionBook'],
                        self.ctx
                    )

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

