import json
from v20.base_entity import BaseEntity
from v20.base_entity import Property
from v20.base_entity import EntityDict
from v20.request import Request



class Candlestick(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "time",
            "time",
            "The start time of the candlestick",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "bid",
            "bid",
            "The candlestick data based on bids. Only provided if bid-based candles were requested.",
            "object",
            "instrument.CandlestickData",
            False,
            None
        ),
        Property(
            "ask",
            "ask",
            "The candlestick data based on asks. Only provided if ask-based candles were requested.",
            "object",
            "instrument.CandlestickData",
            False,
            None
        ),
        Property(
            "mid",
            "mid",
            "The candlestick data based on midpoints. Only provided if midpoint-based candles were requested.",
            "object",
            "instrument.CandlestickData",
            False,
            None
        ),
        Property(
            "volume",
            "volume",
            "The number of prices created during the time-range represented by the candlestick.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "complete",
            "complete",
            "A flag indicating if the candlestick is complete. A complete candlestick is one whose ending time is not in the future.",
            "primitive",
            "boolean",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(Candlestick, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('bid') is not None:
            body['bid'] = \
                CandlestickData.from_dict(
                    data['bid']
                )

        if data.get('ask') is not None:
            body['ask'] = \
                CandlestickData.from_dict(
                    data['ask']
                )

        if data.get('mid') is not None:
            body['mid'] = \
                CandlestickData.from_dict(
                    data['mid']
                )

        if data.get('volume') is not None:
            body['volume'] = \
                data.get('volume')

        if data.get('complete') is not None:
            body['complete'] = \
                data.get('complete')

        self = Candlestick(**body)

        return self


class CandlestickData(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "o",
            "o",
            "The first (open) price in the time-range represented by the candlestick.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "h",
            "h",
            "The highest price in the time-range represented by the candlestick.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "l",
            "l",
            "The lowest price in the time-range represented by the candlestick.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "c",
            "c",
            "The last (closing) price in the time-range represented by the candlestick.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(CandlestickData, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('o') is not None:
            body['o'] = \
                data.get('o')

        if data.get('h') is not None:
            body['h'] = \
                data.get('h')

        if data.get('l') is not None:
            body['l'] = \
                data.get('l')

        if data.get('c') is not None:
            body['c'] = \
                data.get('c')

        self = CandlestickData(**body)

        return self

class EntitySpec(object):
    Candlestick = Candlestick
    CandlestickData = CandlestickData

    def __init__(self, ctx):
        self.ctx = ctx


    def candles(
        self,
        instrument,
        **kwargs
    ):
        """Get Candlesticks

        Fetch candlestick data for an instrument.

        Parameters
        ----------
        instrument : 
            Instrument to get candlestick data for
        price : string, optional
            The Price component(s) to get candlestick data for. Can contain any
            combination of the characters "M" (midpoint candles) "B" (bid
            candles) and "A" (ask candles).
        granularity : , optional
            The granularity of the candlesticks to fetch
        count : integer, optional
            The number of candlesticks to return in the reponse. Count should
            not be specified if both the start and end parameters are provided,
            as the time range combined with the graularity will determine the
            number of candlesticks to return.
        fromTime : , optional
            The start of the time range to fetch candlesticks for.
        toTime : , optional
            The end of the time range to fetch candlesticks for.
        smooth : boolean, optional
            A flag that controls whether the candlestick is "smoothed" or not.
            A smoothed candlestick uses the previous candle's close price as
            its open price, while an unsmoothed candlestick uses the first
            price from its time range as its open price.
        includeFirst : boolean, optional
            A flag that controls whether the candlestick that is covered by the
            from time should be included in the results. This flag enables
            clients to use the timestamp of the last completed candlestick
            received to poll for future candlesticks but avoid receiving the
            previous candlestick repeatedly.
        dailyAlignment : integer, optional
            The hour of the day (in the specified timezone) to use for
            granularities that have daily alignments.
        alignmentTimezone : string, optional
            The timezone to use for the dailyAlignment parameter. Candlesticks
            with daily alignment will be aligned to the dailyAlignment hour
            within the alignmentTimezone.
        weeklyAlignment : , optional
            The day of the week used for granularities that have weekly
            alignment.
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

        if str(response.status) == "200":
            if jbody.get('instrument') is not None:
                parsed_body['instrument'] = \
                    jbody.get('instrument')

            if jbody.get('granularity') is not None:
                parsed_body['granularity'] = \
                    jbody.get('granularity')

            if jbody.get('candles') is not None:
                parsed_body['candles'] = [
                    Candlestick.from_dict(d)
                    for d in jbody.get('candles')
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

