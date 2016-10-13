import json
from v20.base_entity import BaseEntity
from v20.base_entity import Property
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import transaction



class OrderIdentifier(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "orderID",
            "orderID",
            "The OANDA-assigned Order ID",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "clientOrderID",
            "clientOrderID",
            "The client-provided client Order ID",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(OrderIdentifier, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('orderID') is not None:
            body['orderID'] = \
                data.get('orderID')

        if data.get('clientOrderID') is not None:
            body['clientOrderID'] = \
                data.get('clientOrderID')

        self = OrderIdentifier(**body)

        return self


class DynamicOrderState(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "id",
            "Order ID",
            "The Order's ID.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "trailingStopValue",
            "Trailing Stop Value",
            "The Order's calculated trailing stop value.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "triggerDistance",
            "Trigger Distance",
            "The distance between the Trailing Stop Loss Order's trailingStopValue and the current Market Price. This represents the distance (in price units) of the Order from a triggering price. If the distance could not be determined, this value will not be set.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "isTriggerDistanceExact",
            "Trigger Distance Is Exact",
            "True if an exact trigger distance could be calculated. If false, it means the provided trigger distance is a best estimate. If the distance could not be determined, this value will not be set.",
            "primitive",
            "bool",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(DynamicOrderState, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('trailingStopValue') is not None:
            body['trailingStopValue'] = \
                data.get('trailingStopValue')

        if data.get('triggerDistance') is not None:
            body['triggerDistance'] = \
                data.get('triggerDistance')

        if data.get('isTriggerDistanceExact') is not None:
            body['isTriggerDistanceExact'] = \
                data.get('isTriggerDistanceExact')

        self = DynamicOrderState(**body)

        return self


class Order(BaseEntity):
    _summary_format = ""
    _name_format = "Order {id}"

    _properties = [
        Property(
            "id",
            "Order ID",
            "The Order's identifier, unique within the Order's Account.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "createTime",
            "Create Time",
            "The time when the Order was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "state",
            "State",
            "The current state of the Order.",
            "primitive",
            "order.OrderState",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(Order, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):
        type = data.get("type")

        if type == "MARKET":
            return MarketOrder.from_dict(data)
        if type == "LIMIT":
            return LimitOrder.from_dict(data)
        if type == "STOP":
            return StopOrder.from_dict(data)
        if type == "MARKET_IF_TOUCHED":
            return MarketIfTouchedOrder.from_dict(data)
        if type == "TAKE_PROFIT":
            return TakeProfitOrder.from_dict(data)
        if type == "STOP_LOSS":
            return StopLossOrder.from_dict(data)
        if type == "TRAILING_STOP_LOSS":
            return TrailingStopLossOrder.from_dict(data)

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('createTime') is not None:
            body['createTime'] = \
                data.get('createTime')

        if data.get('state') is not None:
            body['state'] = \
                data.get('state')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        self = Order(**body)

        return self


class MarketOrder(BaseEntity):
    _summary_format = "{units} units of {instrument}"
    _name_format = "Market Order {id}"

    _properties = [
        Property(
            "id",
            "Order ID",
            "The Order's identifier, unique within the Order's Account.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "createTime",
            "Create Time",
            "The time when the Order was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "state",
            "State",
            "The current state of the Order.",
            "primitive",
            "order.OrderState",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The type of the Order. Always set to \"MARKET\" for Market Orders.",
            "primitive",
            "order.OrderType",
            False,
            "MARKET"
        ),
        Property(
            "instrument",
            "Instrument",
            "The Market Order's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            True,
            None
        ),
        Property(
            "units",
            "Amount",
            "The quantity requested to be filled by the Market Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.",
            "primitive",
            "primitives.DecimalNumber",
            True,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the Market Order. Restricted to FOK or IOC for a MarketOrder.",
            "primitive",
            "order.TimeInForce",
            True,
            "FOK"
        ),
        Property(
            "priceBound",
            "Price Bound",
            "The worst price that the client is willing to have the Market Order filled at.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "positionFill",
            "Position Fill",
            "Specification of how Positions in the Account are modified when the Order is filled.",
            "primitive",
            "order.OrderPositionFill",
            True,
            "DEFAULT"
        ),
        Property(
            "tradeClose",
            "Trade Close Details",
            "Details of the Trade requested to be closed, only provided when the Market Order is being used to explicitly close a Trade.",
            "object",
            "transaction.MarketOrderTradeClose",
            False,
            None
        ),
        Property(
            "longPositionCloseout",
            "Long Position Close Details",
            "Details of the long Position requested to be closed out, only provided when a Market Order is being used to explicitly closeout a long Position.",
            "object",
            "transaction.MarketOrderPositionCloseout",
            False,
            None
        ),
        Property(
            "shortPositionCloseout",
            "Short Position Close Details",
            "Details of the short Position requested to be closed out, only provided when a Market Order is being used to explicitly closeout a short Position.",
            "object",
            "transaction.MarketOrderPositionCloseout",
            False,
            None
        ),
        Property(
            "marginCloseout",
            "Margin Closeout Details",
            "Details of the Margin Closeout that this Market Order was created for",
            "object",
            "transaction.MarketOrderMarginCloseout",
            False,
            None
        ),
        Property(
            "delayedTradeClose",
            "Delayed Trade Close Details",
            "Details of the delayed Trade close that this Market Order was created for",
            "object",
            "transaction.MarketOrderDelayedTradeClose",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "fillingTransactionID",
            "Filling Transaction ID",
            "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "filledTime",
            "Filled Time",
            "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "tradeOpenedID",
            "Trade Opened ID",
            "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeReducedID",
            "Trade Reduced ID",
            "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeClosedIDs",
            "Trade Closed IDs",
            "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
            "array_primitive",
            "TradeID",
            False,
            None
        ),
        Property(
            "cancellingTransactionID",
            "Cancelling Transction ID",
            "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "cancelledTime",
            "Cancelled Time",
            "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarketOrder, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('createTime') is not None:
            body['createTime'] = \
                data.get('createTime')

        if data.get('state') is not None:
            body['state'] = \
                data.get('state')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('priceBound') is not None:
            body['priceBound'] = \
                data.get('priceBound')

        if data.get('positionFill') is not None:
            body['positionFill'] = \
                data.get('positionFill')

        if data.get('tradeClose') is not None:
            body['tradeClose'] = \
                transaction.MarketOrderTradeClose.from_dict(
                    data['tradeClose']
                )

        if data.get('longPositionCloseout') is not None:
            body['longPositionCloseout'] = \
                transaction.MarketOrderPositionCloseout.from_dict(
                    data['longPositionCloseout']
                )

        if data.get('shortPositionCloseout') is not None:
            body['shortPositionCloseout'] = \
                transaction.MarketOrderPositionCloseout.from_dict(
                    data['shortPositionCloseout']
                )

        if data.get('marginCloseout') is not None:
            body['marginCloseout'] = \
                transaction.MarketOrderMarginCloseout.from_dict(
                    data['marginCloseout']
                )

        if data.get('delayedTradeClose') is not None:
            body['delayedTradeClose'] = \
                transaction.MarketOrderDelayedTradeClose.from_dict(
                    data['delayedTradeClose']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        if data.get('fillingTransactionID') is not None:
            body['fillingTransactionID'] = \
                data.get('fillingTransactionID')

        if data.get('filledTime') is not None:
            body['filledTime'] = \
                data.get('filledTime')

        if data.get('tradeOpenedID') is not None:
            body['tradeOpenedID'] = \
                data.get('tradeOpenedID')

        if data.get('tradeReducedID') is not None:
            body['tradeReducedID'] = \
                data.get('tradeReducedID')

        if data.get('tradeClosedIDs') is not None:
            body['tradeClosedIDs'] = \
                data.get('tradeClosedIDs')

        if data.get('cancellingTransactionID') is not None:
            body['cancellingTransactionID'] = \
                data.get('cancellingTransactionID')

        if data.get('cancelledTime') is not None:
            body['cancelledTime'] = \
                data.get('cancelledTime')

        self = MarketOrder(**body)

        return self


class LimitOrder(BaseEntity):
    _summary_format = "{units} units of {instrument} @ {price}"
    _name_format = "Limit Order {id}"

    _properties = [
        Property(
            "id",
            "Order ID",
            "The Order's identifier, unique within the Order's Account.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "createTime",
            "Create Time",
            "The time when the Order was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "state",
            "State",
            "The current state of the Order.",
            "primitive",
            "order.OrderState",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The type of the Order. Always set to \"LIMIT\" for Limit Orders.",
            "primitive",
            "order.OrderType",
            False,
            "LIMIT"
        ),
        Property(
            "instrument",
            "Instrument",
            "The Limit Order's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            True,
            None
        ),
        Property(
            "units",
            "Amount",
            "The quantity requested to be filled by the Limit Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.",
            "primitive",
            "primitives.DecimalNumber",
            True,
            None
        ),
        Property(
            "price",
            "Price",
            "The price threshold specified for the Limit Order. The Limit Order will only be filled by a market price that is equal to or better than this price.",
            "primitive",
            "pricing.PriceValue",
            True,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the Limit Order.",
            "primitive",
            "order.TimeInForce",
            True,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date/time when the Limit Order will be cancelled if its timeInForce is \"GTD\".",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "positionFill",
            "Position Fill",
            "Specification of how Positions in the Account are modified when the Order is filled.",
            "primitive",
            "order.OrderPositionFill",
            True,
            "DEFAULT"
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "fillingTransactionID",
            "Filling Transaction ID",
            "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "filledTime",
            "Filled Time",
            "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "tradeOpenedID",
            "Trade Opened ID",
            "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeReducedID",
            "Trade Reduced ID",
            "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeClosedIDs",
            "Trade Closed IDs",
            "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
            "array_primitive",
            "TradeID",
            False,
            None
        ),
        Property(
            "cancellingTransactionID",
            "Cancelling Transction ID",
            "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "cancelledTime",
            "Cancelled Time",
            "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "replacesOrderID",
            "Replaces Order ID",
            "The ID of the Order that was replaced by this Order (only provided if this Order was created as part of a cancel/replace).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "replacedByOrderID",
            "Replaced by Order ID",
            "The ID of the Order that replaced this Order (only provided if this Order was cancelled as part of a cancel/replace).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(LimitOrder, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('createTime') is not None:
            body['createTime'] = \
                data.get('createTime')

        if data.get('state') is not None:
            body['state'] = \
                data.get('state')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('gtdTime') is not None:
            body['gtdTime'] = \
                data.get('gtdTime')

        if data.get('positionFill') is not None:
            body['positionFill'] = \
                data.get('positionFill')

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        if data.get('fillingTransactionID') is not None:
            body['fillingTransactionID'] = \
                data.get('fillingTransactionID')

        if data.get('filledTime') is not None:
            body['filledTime'] = \
                data.get('filledTime')

        if data.get('tradeOpenedID') is not None:
            body['tradeOpenedID'] = \
                data.get('tradeOpenedID')

        if data.get('tradeReducedID') is not None:
            body['tradeReducedID'] = \
                data.get('tradeReducedID')

        if data.get('tradeClosedIDs') is not None:
            body['tradeClosedIDs'] = \
                data.get('tradeClosedIDs')

        if data.get('cancellingTransactionID') is not None:
            body['cancellingTransactionID'] = \
                data.get('cancellingTransactionID')

        if data.get('cancelledTime') is not None:
            body['cancelledTime'] = \
                data.get('cancelledTime')

        if data.get('replacesOrderID') is not None:
            body['replacesOrderID'] = \
                data.get('replacesOrderID')

        if data.get('replacedByOrderID') is not None:
            body['replacedByOrderID'] = \
                data.get('replacedByOrderID')

        self = LimitOrder(**body)

        return self


class StopOrder(BaseEntity):
    _summary_format = "{units} units of {instrument} @ {price}"
    _name_format = "Stop Order {id}"

    _properties = [
        Property(
            "id",
            "Order ID",
            "The Order's identifier, unique within the Order's Account.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "createTime",
            "Create Time",
            "The time when the Order was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "state",
            "State",
            "The current state of the Order.",
            "primitive",
            "order.OrderState",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The type of the Order. Always set to \"STOP\" for Stop Orders.",
            "primitive",
            "order.OrderType",
            False,
            "STOP"
        ),
        Property(
            "instrument",
            "Instrument",
            "The Stop Order's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            True,
            None
        ),
        Property(
            "units",
            "Amount",
            "The quantity requested to be filled by the Stop Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.",
            "primitive",
            "primitives.DecimalNumber",
            True,
            None
        ),
        Property(
            "price",
            "Price",
            "The price threshold specified for the Stop Order. The Stop Order will only be filled by a market price that is equal to or worse than this price.",
            "primitive",
            "pricing.PriceValue",
            True,
            None
        ),
        Property(
            "priceBound",
            "Price Bound",
            "The worst market price that may be used to fill this Stop Order. If the market gaps and crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the Stop Order.",
            "primitive",
            "order.TimeInForce",
            True,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date/time when the Stop Order will be cancelled if its timeInForce is \"GTD\".",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "positionFill",
            "Position Fill",
            "Specification of how Positions in the Account are modified when the Order is filled.",
            "primitive",
            "order.OrderPositionFill",
            True,
            "DEFAULT"
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "fillingTransactionID",
            "Filling Transaction ID",
            "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "filledTime",
            "Filled Time",
            "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "tradeOpenedID",
            "Trade Opened ID",
            "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeReducedID",
            "Trade Reduced ID",
            "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeClosedIDs",
            "Trade Closed IDs",
            "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
            "array_primitive",
            "TradeID",
            False,
            None
        ),
        Property(
            "cancellingTransactionID",
            "Cancelling Transction ID",
            "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "cancelledTime",
            "Cancelled Time",
            "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "replacesOrderID",
            "Replaces Order ID",
            "The ID of the Order that was replaced by this Order (only provided if this Order was created as part of a cancel/replace).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "replacedByOrderID",
            "Replaced by Order ID",
            "The ID of the Order that replaced this Order (only provided if this Order was cancelled as part of a cancel/replace).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(StopOrder, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('createTime') is not None:
            body['createTime'] = \
                data.get('createTime')

        if data.get('state') is not None:
            body['state'] = \
                data.get('state')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('priceBound') is not None:
            body['priceBound'] = \
                data.get('priceBound')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('gtdTime') is not None:
            body['gtdTime'] = \
                data.get('gtdTime')

        if data.get('positionFill') is not None:
            body['positionFill'] = \
                data.get('positionFill')

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        if data.get('fillingTransactionID') is not None:
            body['fillingTransactionID'] = \
                data.get('fillingTransactionID')

        if data.get('filledTime') is not None:
            body['filledTime'] = \
                data.get('filledTime')

        if data.get('tradeOpenedID') is not None:
            body['tradeOpenedID'] = \
                data.get('tradeOpenedID')

        if data.get('tradeReducedID') is not None:
            body['tradeReducedID'] = \
                data.get('tradeReducedID')

        if data.get('tradeClosedIDs') is not None:
            body['tradeClosedIDs'] = \
                data.get('tradeClosedIDs')

        if data.get('cancellingTransactionID') is not None:
            body['cancellingTransactionID'] = \
                data.get('cancellingTransactionID')

        if data.get('cancelledTime') is not None:
            body['cancelledTime'] = \
                data.get('cancelledTime')

        if data.get('replacesOrderID') is not None:
            body['replacesOrderID'] = \
                data.get('replacesOrderID')

        if data.get('replacedByOrderID') is not None:
            body['replacedByOrderID'] = \
                data.get('replacedByOrderID')

        self = StopOrder(**body)

        return self


class MarketIfTouchedOrder(BaseEntity):
    _summary_format = "{units} units of {instrument} @ {price}"
    _name_format = "MIT Order {id}"

    _properties = [
        Property(
            "id",
            "Order ID",
            "The Order's identifier, unique within the Order's Account.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "createTime",
            "Create Time",
            "The time when the Order was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "state",
            "State",
            "The current state of the Order.",
            "primitive",
            "order.OrderState",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The type of the Order. Always set to \"MARKET_IF_TOUCHED\" for Market If Touched Orders.",
            "primitive",
            "order.OrderType",
            False,
            "MARKET_IF_TOUCHED"
        ),
        Property(
            "instrument",
            "Instrument",
            "The MarketIfTouched Order's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            True,
            None
        ),
        Property(
            "units",
            "Amount",
            "The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.",
            "primitive",
            "primitives.DecimalNumber",
            True,
            None
        ),
        Property(
            "price",
            "Price",
            "The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be filled by a market price that crosses this price from the direction of the market price at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's price and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.",
            "primitive",
            "pricing.PriceValue",
            True,
            None
        ),
        Property(
            "priceBound",
            "Price Value",
            "The worst market price that may be used to fill this MarketIfTouched Order.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the MarketIfTouched Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for MarketIfTouched Orders.",
            "primitive",
            "order.TimeInForce",
            True,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date/time when the MarketIfTouched Order will be cancelled if its timeInForce is \"GTD\".",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "positionFill",
            "Position Fill",
            "Specification of how Positions in the Account are modified when the Order is filled.",
            "primitive",
            "order.OrderPositionFill",
            True,
            "DEFAULT"
        ),
        Property(
            "initialMarketPrice",
            "Initial Market Price",
            "The Market price at the time when the MarketIfTouched Order was created.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "fillingTransactionID",
            "Filling Transaction ID",
            "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "filledTime",
            "Filled Time",
            "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "tradeOpenedID",
            "Trade Opened ID",
            "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeReducedID",
            "Trade Reduced ID",
            "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeClosedIDs",
            "Trade Closed IDs",
            "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
            "array_primitive",
            "TradeID",
            False,
            None
        ),
        Property(
            "cancellingTransactionID",
            "Cancelling Transction ID",
            "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "cancelledTime",
            "Cancelled Time",
            "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "replacesOrderID",
            "Replaces Order ID",
            "The ID of the Order that was replaced by this Order (only provided if this Order was created as part of a cancel/replace).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "replacedByOrderID",
            "Replaced by Order ID",
            "The ID of the Order that replaced this Order (only provided if this Order was cancelled as part of a cancel/replace).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarketIfTouchedOrder, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('createTime') is not None:
            body['createTime'] = \
                data.get('createTime')

        if data.get('state') is not None:
            body['state'] = \
                data.get('state')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('priceBound') is not None:
            body['priceBound'] = \
                data.get('priceBound')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('gtdTime') is not None:
            body['gtdTime'] = \
                data.get('gtdTime')

        if data.get('positionFill') is not None:
            body['positionFill'] = \
                data.get('positionFill')

        if data.get('initialMarketPrice') is not None:
            body['initialMarketPrice'] = \
                data.get('initialMarketPrice')

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        if data.get('fillingTransactionID') is not None:
            body['fillingTransactionID'] = \
                data.get('fillingTransactionID')

        if data.get('filledTime') is not None:
            body['filledTime'] = \
                data.get('filledTime')

        if data.get('tradeOpenedID') is not None:
            body['tradeOpenedID'] = \
                data.get('tradeOpenedID')

        if data.get('tradeReducedID') is not None:
            body['tradeReducedID'] = \
                data.get('tradeReducedID')

        if data.get('tradeClosedIDs') is not None:
            body['tradeClosedIDs'] = \
                data.get('tradeClosedIDs')

        if data.get('cancellingTransactionID') is not None:
            body['cancellingTransactionID'] = \
                data.get('cancellingTransactionID')

        if data.get('cancelledTime') is not None:
            body['cancelledTime'] = \
                data.get('cancelledTime')

        if data.get('replacesOrderID') is not None:
            body['replacesOrderID'] = \
                data.get('replacesOrderID')

        if data.get('replacedByOrderID') is not None:
            body['replacedByOrderID'] = \
                data.get('replacedByOrderID')

        self = MarketIfTouchedOrder(**body)

        return self


class TakeProfitOrder(BaseEntity):
    _summary_format = "Take Profit for Trade {tradeID} @ {price}"
    _name_format = "TP Order {id}"

    _properties = [
        Property(
            "id",
            "Order ID",
            "The Order's identifier, unique within the Order's Account.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "createTime",
            "Create Time",
            "The time when the Order was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "state",
            "State",
            "The current state of the Order.",
            "primitive",
            "order.OrderState",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The type of the Order. Always set to \"TAKE_PROFIT\" for Take Profit Orders.",
            "primitive",
            "order.OrderType",
            False,
            "TAKE_PROFIT"
        ),
        Property(
            "tradeID",
            "Trade ID",
            "The ID of the Trade to close when the price threshold is breached.",
            "primitive",
            "trade.TradeID",
            True,
            None
        ),
        Property(
            "clientTradeID",
            "Client Trade ID",
            "The client ID of the Trade to be closed when the price threshold is breached.",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
        Property(
            "price",
            "Price",
            "The price threshold specified for the TakeProfit Order. The associated Trade will be closed by a market price that is equal to or better than this threshold.",
            "primitive",
            "pricing.PriceValue",
            True,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the TakeProfit Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for TakeProfit Orders.",
            "primitive",
            "order.TimeInForce",
            True,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date/time when the TakeProfit Order will be cancelled if its timeInForce is \"GTD\".",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "fillingTransactionID",
            "Filling Transaction ID",
            "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "filledTime",
            "Filled Time",
            "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "tradeOpenedID",
            "Trade Opened ID",
            "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeReducedID",
            "Trade Reduced ID",
            "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeClosedIDs",
            "Trade Closed IDs",
            "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
            "array_primitive",
            "TradeID",
            False,
            None
        ),
        Property(
            "cancellingTransactionID",
            "Cancelling Transction ID",
            "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "cancelledTime",
            "Cancelled Time",
            "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "replacesOrderID",
            "Replaces Order ID",
            "The ID of the Order that was replaced by this Order (only provided if this Order was created as part of a cancel/replace).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "replacedByOrderID",
            "Replaced by Order ID",
            "The ID of the Order that replaced this Order (only provided if this Order was cancelled as part of a cancel/replace).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TakeProfitOrder, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('createTime') is not None:
            body['createTime'] = \
                data.get('createTime')

        if data.get('state') is not None:
            body['state'] = \
                data.get('state')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('clientTradeID') is not None:
            body['clientTradeID'] = \
                data.get('clientTradeID')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('gtdTime') is not None:
            body['gtdTime'] = \
                data.get('gtdTime')

        if data.get('fillingTransactionID') is not None:
            body['fillingTransactionID'] = \
                data.get('fillingTransactionID')

        if data.get('filledTime') is not None:
            body['filledTime'] = \
                data.get('filledTime')

        if data.get('tradeOpenedID') is not None:
            body['tradeOpenedID'] = \
                data.get('tradeOpenedID')

        if data.get('tradeReducedID') is not None:
            body['tradeReducedID'] = \
                data.get('tradeReducedID')

        if data.get('tradeClosedIDs') is not None:
            body['tradeClosedIDs'] = \
                data.get('tradeClosedIDs')

        if data.get('cancellingTransactionID') is not None:
            body['cancellingTransactionID'] = \
                data.get('cancellingTransactionID')

        if data.get('cancelledTime') is not None:
            body['cancelledTime'] = \
                data.get('cancelledTime')

        if data.get('replacesOrderID') is not None:
            body['replacesOrderID'] = \
                data.get('replacesOrderID')

        if data.get('replacedByOrderID') is not None:
            body['replacedByOrderID'] = \
                data.get('replacedByOrderID')

        self = TakeProfitOrder(**body)

        return self


class StopLossOrder(BaseEntity):
    _summary_format = "Stop Loss for Trade {tradeID} @ {price}"
    _name_format = "SL Order {id}"

    _properties = [
        Property(
            "id",
            "Order ID",
            "The Order's identifier, unique within the Order's Account.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "createTime",
            "Create Time",
            "The time when the Order was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "state",
            "State",
            "The current state of the Order.",
            "primitive",
            "order.OrderState",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The type of the Order. Always set to \"STOP_LOSS\" for Stop Loss Orders.",
            "primitive",
            "order.OrderType",
            False,
            "STOP_LOSS"
        ),
        Property(
            "tradeID",
            "Trade ID",
            "The ID of the Trade to close when the price threshold is breached.",
            "primitive",
            "trade.TradeID",
            True,
            None
        ),
        Property(
            "clientTradeID",
            "Client Trade ID",
            "The client ID of the Trade to be closed when the price threshold is breached.",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
        Property(
            "price",
            "Price",
            "The price threshold specified for the StopLoss Order. The associated Trade will be closed by a market price that is equal to or worse than this threshold.",
            "primitive",
            "pricing.PriceValue",
            True,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the StopLoss Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for StopLoss Orders.",
            "primitive",
            "order.TimeInForce",
            True,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date/time when the StopLoss Order will be cancelled if its timeInForce is \"GTD\".",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "fillingTransactionID",
            "Filling Transaction ID",
            "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "filledTime",
            "Filled Time",
            "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "tradeOpenedID",
            "Trade Opened ID",
            "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeReducedID",
            "Trade Reduced ID",
            "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeClosedIDs",
            "Trade Closed IDs",
            "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
            "array_primitive",
            "TradeID",
            False,
            None
        ),
        Property(
            "cancellingTransactionID",
            "Cancelling Transction ID",
            "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "cancelledTime",
            "Cancelled Time",
            "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "replacesOrderID",
            "Replaces Order ID",
            "The ID of the Order that was replaced by this Order (only provided if this Order was created as part of a cancel/replace).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "replacedByOrderID",
            "Replaced by Order ID",
            "The ID of the Order that replaced this Order (only provided if this Order was cancelled as part of a cancel/replace).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(StopLossOrder, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('createTime') is not None:
            body['createTime'] = \
                data.get('createTime')

        if data.get('state') is not None:
            body['state'] = \
                data.get('state')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('clientTradeID') is not None:
            body['clientTradeID'] = \
                data.get('clientTradeID')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('gtdTime') is not None:
            body['gtdTime'] = \
                data.get('gtdTime')

        if data.get('fillingTransactionID') is not None:
            body['fillingTransactionID'] = \
                data.get('fillingTransactionID')

        if data.get('filledTime') is not None:
            body['filledTime'] = \
                data.get('filledTime')

        if data.get('tradeOpenedID') is not None:
            body['tradeOpenedID'] = \
                data.get('tradeOpenedID')

        if data.get('tradeReducedID') is not None:
            body['tradeReducedID'] = \
                data.get('tradeReducedID')

        if data.get('tradeClosedIDs') is not None:
            body['tradeClosedIDs'] = \
                data.get('tradeClosedIDs')

        if data.get('cancellingTransactionID') is not None:
            body['cancellingTransactionID'] = \
                data.get('cancellingTransactionID')

        if data.get('cancelledTime') is not None:
            body['cancelledTime'] = \
                data.get('cancelledTime')

        if data.get('replacesOrderID') is not None:
            body['replacesOrderID'] = \
                data.get('replacesOrderID')

        if data.get('replacedByOrderID') is not None:
            body['replacedByOrderID'] = \
                data.get('replacedByOrderID')

        self = StopLossOrder(**body)

        return self


class TrailingStopLossOrder(BaseEntity):
    _summary_format = "Trailing Stop Loss for Trade {tradeID} @ {trailingStopValue}"
    _name_format = "TSL Order {id}"

    _properties = [
        Property(
            "id",
            "Order ID",
            "The Order's identifier, unique within the Order's Account.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "createTime",
            "Create Time",
            "The time when the Order was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "state",
            "State",
            "The current state of the Order.",
            "primitive",
            "order.OrderState",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The type of the Order. Always set to \"TRAILING_STOP_LOSS\" for Trailing Stop Loss Orders.",
            "primitive",
            "order.OrderType",
            False,
            "TRAILING_STOP_LOSS"
        ),
        Property(
            "tradeID",
            "Trade ID",
            "The ID of the Trade to close when the price threshold is breached.",
            "primitive",
            "trade.TradeID",
            True,
            None
        ),
        Property(
            "clientTradeID",
            "Client Trade ID",
            "The client ID of the Trade to be closed when the price threshold is breached.",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
        Property(
            "distance",
            "Price Distance",
            "The price distance specified for the TrailingStopLoss Order.",
            "primitive",
            "pricing.PriceValue",
            True,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the TrailingStopLoss Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for TrailingStopLoss Orders.",
            "primitive",
            "order.TimeInForce",
            True,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date/time when the StopLoss Order will be cancelled if its timeInForce is \"GTD\".",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "trailingStopValue",
            "Trailing Stop Loss Value",
            "The trigger price for the Trailing Stop Loss Order. The trailing stop value will trail (follow) the market price by the TSL order's configured \"distance\" as the market price moves in the winning direction. If the market price moves to a level that is equal to or worse than the trailing stop value, the order will be filled and the Trade will be closed.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "fillingTransactionID",
            "Filling Transaction ID",
            "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "filledTime",
            "Filled Time",
            "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "tradeOpenedID",
            "Trade Opened ID",
            "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeReducedID",
            "Trade Reduced ID",
            "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "tradeClosedIDs",
            "Trade Closed IDs",
            "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
            "array_primitive",
            "TradeID",
            False,
            None
        ),
        Property(
            "cancellingTransactionID",
            "Cancelling Transction ID",
            "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "cancelledTime",
            "Cancelled Time",
            "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "replacesOrderID",
            "Replaces Order ID",
            "The ID of the Order that was replaced by this Order (only provided if this Order was created as part of a cancel/replace).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "replacedByOrderID",
            "Replaced by Order ID",
            "The ID of the Order that replaced this Order (only provided if this Order was cancelled as part of a cancel/replace).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TrailingStopLossOrder, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('createTime') is not None:
            body['createTime'] = \
                data.get('createTime')

        if data.get('state') is not None:
            body['state'] = \
                data.get('state')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('clientTradeID') is not None:
            body['clientTradeID'] = \
                data.get('clientTradeID')

        if data.get('distance') is not None:
            body['distance'] = \
                data.get('distance')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('gtdTime') is not None:
            body['gtdTime'] = \
                data.get('gtdTime')

        if data.get('trailingStopValue') is not None:
            body['trailingStopValue'] = \
                data.get('trailingStopValue')

        if data.get('fillingTransactionID') is not None:
            body['fillingTransactionID'] = \
                data.get('fillingTransactionID')

        if data.get('filledTime') is not None:
            body['filledTime'] = \
                data.get('filledTime')

        if data.get('tradeOpenedID') is not None:
            body['tradeOpenedID'] = \
                data.get('tradeOpenedID')

        if data.get('tradeReducedID') is not None:
            body['tradeReducedID'] = \
                data.get('tradeReducedID')

        if data.get('tradeClosedIDs') is not None:
            body['tradeClosedIDs'] = \
                data.get('tradeClosedIDs')

        if data.get('cancellingTransactionID') is not None:
            body['cancellingTransactionID'] = \
                data.get('cancellingTransactionID')

        if data.get('cancelledTime') is not None:
            body['cancelledTime'] = \
                data.get('cancelledTime')

        if data.get('replacesOrderID') is not None:
            body['replacesOrderID'] = \
                data.get('replacesOrderID')

        if data.get('replacedByOrderID') is not None:
            body['replacedByOrderID'] = \
                data.get('replacedByOrderID')

        self = TrailingStopLossOrder(**body)

        return self


class OrderRequest(BaseEntity):
    _summary_format = ""
    _name_format = "OrderRequest"

    _properties = [
    ]

    def __init__(self, **kwargs):
        super(OrderRequest, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        self = OrderRequest(**body)

        return self


class MarketOrderRequest(BaseEntity):
    _summary_format = "{units} units of {instrument}"
    _name_format = "Market Order Request"

    _properties = [
        Property(
            "type",
            "Type",
            "The type of the Order to Create. Must be set to \"MARKET\" when creating a Market Order.",
            "primitive",
            "order.OrderType",
            False,
            "MARKET"
        ),
        Property(
            "instrument",
            "Instrument",
            "The Market Order's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            True,
            None
        ),
        Property(
            "units",
            "Amount",
            "The quantity requested to be filled by the Market Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.",
            "primitive",
            "primitives.DecimalNumber",
            True,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the Market Order. Restricted to FOK or IOC for a MarketOrder.",
            "primitive",
            "order.TimeInForce",
            True,
            "FOK"
        ),
        Property(
            "priceBound",
            "Price Bound",
            "The worst price that the client is willing to have the Market Order filled at.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "positionFill",
            "Position Fill",
            "Specification of how Positions in the Account are modified when the Order is filled.",
            "primitive",
            "order.OrderPositionFill",
            True,
            "DEFAULT"
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarketOrderRequest, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('priceBound') is not None:
            body['priceBound'] = \
                data.get('priceBound')

        if data.get('positionFill') is not None:
            body['positionFill'] = \
                data.get('positionFill')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        self = MarketOrderRequest(**body)

        return self


class LimitOrderRequest(BaseEntity):
    _summary_format = "{units} units of {instrument} @ {price}"
    _name_format = "Limit Order Request"

    _properties = [
        Property(
            "type",
            "Type",
            "The type of the Order to Create. Must be set to \"LIMIT\" when creating a Market Order.",
            "primitive",
            "order.OrderType",
            False,
            "LIMIT"
        ),
        Property(
            "instrument",
            "Instrument",
            "The Limit Order's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            True,
            None
        ),
        Property(
            "units",
            "Amount",
            "The quantity requested to be filled by the Limit Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.",
            "primitive",
            "primitives.DecimalNumber",
            True,
            None
        ),
        Property(
            "price",
            "Price",
            "The price threshold specified for the Limit Order. The Limit Order will only be filled by a market price that is equal to or better than this price.",
            "primitive",
            "pricing.PriceValue",
            True,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the Limit Order.",
            "primitive",
            "order.TimeInForce",
            True,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date/time when the Limit Order will be cancelled if its timeInForce is \"GTD\".",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "positionFill",
            "Position Fill",
            "Specification of how Positions in the Account are modified when the Order is filled.",
            "primitive",
            "order.OrderPositionFill",
            True,
            "DEFAULT"
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(LimitOrderRequest, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('gtdTime') is not None:
            body['gtdTime'] = \
                data.get('gtdTime')

        if data.get('positionFill') is not None:
            body['positionFill'] = \
                data.get('positionFill')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        self = LimitOrderRequest(**body)

        return self


class StopOrderRequest(BaseEntity):
    _summary_format = "{units} units of {instrument} @ {price}"
    _name_format = "Stop Order Request"

    _properties = [
        Property(
            "type",
            "Type",
            "The type of the Order to Create. Must be set to \"STOP\" when creating a Stop Order.",
            "primitive",
            "order.OrderType",
            False,
            "STOP"
        ),
        Property(
            "instrument",
            "Instrument",
            "The Stop Order's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            True,
            None
        ),
        Property(
            "units",
            "Amount",
            "The quantity requested to be filled by the Stop Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.",
            "primitive",
            "primitives.DecimalNumber",
            True,
            None
        ),
        Property(
            "price",
            "Price",
            "The price threshold specified for the Stop Order. The Stop Order will only be filled by a market price that is equal to or worse than this price.",
            "primitive",
            "pricing.PriceValue",
            True,
            None
        ),
        Property(
            "priceBound",
            "Price Bound",
            "The worst market price that may be used to fill this Stop Order. If the market gaps and crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the Stop Order.",
            "primitive",
            "order.TimeInForce",
            True,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date/time when the Stop Order will be cancelled if its timeInForce is \"GTD\".",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "positionFill",
            "Position Fill",
            "Specification of how Positions in the Account are modified when the Order is filled.",
            "primitive",
            "order.OrderPositionFill",
            True,
            "DEFAULT"
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(StopOrderRequest, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('priceBound') is not None:
            body['priceBound'] = \
                data.get('priceBound')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('gtdTime') is not None:
            body['gtdTime'] = \
                data.get('gtdTime')

        if data.get('positionFill') is not None:
            body['positionFill'] = \
                data.get('positionFill')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        self = StopOrderRequest(**body)

        return self


class MarketIfTouchedOrderRequest(BaseEntity):
    _summary_format = "{units} units of {instrument} @ {price}"
    _name_format = "MIT Order Request"

    _properties = [
        Property(
            "type",
            "Type",
            "The type of the Order to Create. Must be set to \"MARKET_IF_TOUCHED\" when creating a Market If Touched Order.",
            "primitive",
            "order.OrderType",
            False,
            "MARKET_IF_TOUCHED"
        ),
        Property(
            "instrument",
            "Instrument",
            "The MarketIfTouched Order's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            True,
            None
        ),
        Property(
            "units",
            "Amount",
            "The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.",
            "primitive",
            "primitives.DecimalNumber",
            True,
            None
        ),
        Property(
            "price",
            "Price",
            "The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be filled by a market price that crosses this price from the direction of the market price at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's price and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.",
            "primitive",
            "pricing.PriceValue",
            True,
            None
        ),
        Property(
            "priceBound",
            "Price Value",
            "The worst market price that may be used to fill this MarketIfTouched Order.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the MarketIfTouched Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for MarketIfTouched Orders.",
            "primitive",
            "order.TimeInForce",
            True,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date/time when the MarketIfTouched Order will be cancelled if its timeInForce is \"GTD\".",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "positionFill",
            "Position Fill",
            "Specification of how Positions in the Account are modified when the Order is filled.",
            "primitive",
            "order.OrderPositionFill",
            True,
            "DEFAULT"
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarketIfTouchedOrderRequest, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('priceBound') is not None:
            body['priceBound'] = \
                data.get('priceBound')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('gtdTime') is not None:
            body['gtdTime'] = \
                data.get('gtdTime')

        if data.get('positionFill') is not None:
            body['positionFill'] = \
                data.get('positionFill')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        self = MarketIfTouchedOrderRequest(**body)

        return self


class TakeProfitOrderRequest(BaseEntity):
    _summary_format = "Take Profit for Trade {tradeID} @ {price}"
    _name_format = "TP Order Request"

    _properties = [
        Property(
            "type",
            "Type",
            "The type of the Order to Create. Must be set to \"TAKE_PROFIT\" when creating a Take Profit Order.",
            "primitive",
            "order.OrderType",
            False,
            "TAKE_PROFIT"
        ),
        Property(
            "tradeID",
            "Trade ID",
            "The ID of the Trade to close when the price threshold is breached.",
            "primitive",
            "trade.TradeID",
            True,
            None
        ),
        Property(
            "clientTradeID",
            "Client Trade ID",
            "The client ID of the Trade to be closed when the price threshold is breached.",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
        Property(
            "price",
            "Price",
            "The price threshold specified for the TakeProfit Order. The associated Trade will be closed by a market price that is equal to or better than this threshold.",
            "primitive",
            "pricing.PriceValue",
            True,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the TakeProfit Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for TakeProfit Orders.",
            "primitive",
            "order.TimeInForce",
            True,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date/time when the TakeProfit Order will be cancelled if its timeInForce is \"GTD\".",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TakeProfitOrderRequest, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('clientTradeID') is not None:
            body['clientTradeID'] = \
                data.get('clientTradeID')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('gtdTime') is not None:
            body['gtdTime'] = \
                data.get('gtdTime')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        self = TakeProfitOrderRequest(**body)

        return self


class StopLossOrderRequest(BaseEntity):
    _summary_format = "Stop Loss for Trade {tradeID} @ {price}"
    _name_format = "SL Order Request"

    _properties = [
        Property(
            "type",
            "Type",
            "The type of the Order to Create. Must be set to \"STOP_LOSS\" when creating a Stop Loss Order.",
            "primitive",
            "order.OrderType",
            False,
            "STOP_LOSS"
        ),
        Property(
            "tradeID",
            "Trade ID",
            "The ID of the Trade to close when the price threshold is breached.",
            "primitive",
            "trade.TradeID",
            True,
            None
        ),
        Property(
            "clientTradeID",
            "Client Trade ID",
            "The client ID of the Trade to be closed when the price threshold is breached.",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
        Property(
            "price",
            "Price",
            "The price threshold specified for the StopLoss Order. The associated Trade will be closed by a market price that is equal to or worse than this threshold.",
            "primitive",
            "pricing.PriceValue",
            True,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the StopLoss Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for StopLoss Orders.",
            "primitive",
            "order.TimeInForce",
            True,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date/time when the StopLoss Order will be cancelled if its timeInForce is \"GTD\".",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(StopLossOrderRequest, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('clientTradeID') is not None:
            body['clientTradeID'] = \
                data.get('clientTradeID')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('gtdTime') is not None:
            body['gtdTime'] = \
                data.get('gtdTime')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        self = StopLossOrderRequest(**body)

        return self


class TrailingStopLossOrderRequest(BaseEntity):
    _summary_format = "Trailing Stop Loss for Trade {tradeID} @ {trailingStopValue}"
    _name_format = "TSL Order Request"

    _properties = [
        Property(
            "type",
            "Type",
            "The type of the Order to Create. Must be set to \"TRAILING_STOP_LOSS\" when creating a Trailng Stop Loss Order.",
            "primitive",
            "order.OrderType",
            False,
            "TRAILING_STOP_LOSS"
        ),
        Property(
            "tradeID",
            "Trade ID",
            "The ID of the Trade to close when the price threshold is breached.",
            "primitive",
            "trade.TradeID",
            True,
            None
        ),
        Property(
            "clientTradeID",
            "Client Trade ID",
            "The client ID of the Trade to be closed when the price threshold is breached.",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
        Property(
            "distance",
            "Price Distance",
            "The price distance specified for the TrailingStopLoss Order.",
            "primitive",
            "pricing.PriceValue",
            True,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time-in-force requested for the TrailingStopLoss Order. Restricted to \"GTC\", \"GFD\" and \"GTD\" for TrailingStopLoss Orders.",
            "primitive",
            "order.TimeInForce",
            True,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date/time when the StopLoss Order will be cancelled if its timeInForce is \"GTD\".",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TrailingStopLossOrderRequest, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('clientTradeID') is not None:
            body['clientTradeID'] = \
                data.get('clientTradeID')

        if data.get('distance') is not None:
            body['distance'] = \
                data.get('distance')

        if data.get('timeInForce') is not None:
            body['timeInForce'] = \
                data.get('timeInForce')

        if data.get('gtdTime') is not None:
            body['gtdTime'] = \
                data.get('gtdTime')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        self = TrailingStopLossOrderRequest(**body)

        return self

class EntitySpec(object):
    OrderIdentifier = OrderIdentifier
    DynamicOrderState = DynamicOrderState
    Order = Order
    MarketOrder = MarketOrder
    LimitOrder = LimitOrder
    StopOrder = StopOrder
    MarketIfTouchedOrder = MarketIfTouchedOrder
    TakeProfitOrder = TakeProfitOrder
    StopLossOrder = StopLossOrder
    TrailingStopLossOrder = TrailingStopLossOrder
    OrderRequest = OrderRequest
    MarketOrderRequest = MarketOrderRequest
    LimitOrderRequest = LimitOrderRequest
    StopOrderRequest = StopOrderRequest
    MarketIfTouchedOrderRequest = MarketIfTouchedOrderRequest
    TakeProfitOrderRequest = TakeProfitOrderRequest
    StopLossOrderRequest = StopLossOrderRequest
    TrailingStopLossOrderRequest = TrailingStopLossOrderRequest

    def __init__(self, ctx):
        self.ctx = ctx


    def create(
        self,
        accountID,
        **kwargs
    ):
        """Create Order

        Create an Order for an Account

        Parameters
        ----------
        accountID : 
            ID of the Account to create the Order for.
        order : None, optional
            Specification of the Order to create
        """


        request = Request(
            'POST',
            '/v3/accounts/{accountID}/orders'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        body = EntityDict()

        body.set('order', kwargs.get('order'))

        request.set_body_dict(body.dict)

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "201":
            if jbody.get('orderCreateTransaction') is not None:
                parsed_body['orderCreateTransaction'] = \
                    transaction.Transaction.from_dict(
                        jbody['orderCreateTransaction']
                    )

            if jbody.get('orderFillTransaction') is not None:
                parsed_body['orderFillTransaction'] = \
                    transaction.OrderFillTransaction.from_dict(
                        jbody['orderFillTransaction']
                    )

            if jbody.get('orderCancelTransaction') is not None:
                parsed_body['orderCancelTransaction'] = \
                    transaction.OrderCancelTransaction.from_dict(
                        jbody['orderCancelTransaction']
                    )

            if jbody.get('orderReissueTransaction') is not None:
                parsed_body['orderReissueTransaction'] = \
                    transaction.Transaction.from_dict(
                        jbody['orderReissueTransaction']
                    )

            if jbody.get('orderReissueRejectTransaction') is not None:
                parsed_body['orderReissueRejectTransaction'] = \
                    transaction.Transaction.from_dict(
                        jbody['orderReissueRejectTransaction']
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


        if str(response.status) == "400":
            if jbody.get('orderRejectTransaction') is not None:
                parsed_body['orderRejectTransaction'] = \
                    transaction.Transaction.from_dict(
                        jbody['orderRejectTransaction']
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

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


    def list(
        self,
        accountID,
        **kwargs
    ):
        """List Orders

        Get a list of Orders for an Account

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch Orders for
        ids : array, optional
            List of Order IDs to retrieve
        state : , optional
            The state to filter the requested Orders by
        instrument : , optional
            The instrument to filter the requested orders by
        count : integer, optional
            The maximum number of Orders to return
        beforeID : , optional
            The maximum Order ID to return. If not provided the most recent
            Orders in the Account are returned
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/orders'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_param(
            'ids',
            kwargs.get('ids')
        )

        request.set_param(
            'state',
            kwargs.get('state')
        )

        request.set_param(
            'instrument',
            kwargs.get('instrument')
        )

        request.set_param(
            'count',
            kwargs.get('count')
        )

        request.set_param(
            'beforeID',
            kwargs.get('beforeID')
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('orders') is not None:
                parsed_body['orders'] = [
                    Order.from_dict(d)
                    for d in jbody.get('orders')
                ]

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


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


    def list_pending(
        self,
        accountID,
        **kwargs
    ):
        """Pending Orders

        List all pending Orders in an Account

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch pending Orders for
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/pendingOrders'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('orders') is not None:
                parsed_body['orders'] = [
                    Order.from_dict(d)
                    for d in jbody.get('orders')
                ]

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


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


    def get(
        self,
        accountID,
        orderID,
        **kwargs
    ):
        """Get Order

        Get details for a single Order in an Account

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch an Order for
        orderID : 
            ID of the Order to fetch
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/orders/{orderID}'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'orderID',
            orderID
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('order') is not None:
                parsed_body['order'] = \
                    Order.from_dict(
                        jbody['order']
                    )

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


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


    def replace(
        self,
        accountID,
        orderID,
        **kwargs
    ):
        """Replace Order

        Replace an Order in an Account by simultaneously cancelling it and
        creating a replacement Order

        Parameters
        ----------
        accountID : 
            ID of the Account to cancel and replace the Order for.
        orderID : 
            ID of the Order to cancel.
        order : None, optional
            Specification of the replacing Order
        """


        request = Request(
            'PUT',
            '/v3/accounts/{accountID}/orders/{orderID}'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'orderID',
            orderID
        )

        body = EntityDict()

        body.set('order', kwargs.get('order'))

        request.set_body_dict(body.dict)

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "201":
            if jbody.get('orderCancelTransaction') is not None:
                parsed_body['orderCancelTransaction'] = \
                    transaction.OrderCancelTransaction.from_dict(
                        jbody['orderCancelTransaction']
                    )

            if jbody.get('orderCreateTransaction') is not None:
                parsed_body['orderCreateTransaction'] = \
                    transaction.Transaction.from_dict(
                        jbody['orderCreateTransaction']
                    )

            if jbody.get('orderFillTransaction') is not None:
                parsed_body['orderFillTransaction'] = \
                    transaction.OrderFillTransaction.from_dict(
                        jbody['orderFillTransaction']
                    )

            if jbody.get('orderReissueTransaction') is not None:
                parsed_body['orderReissueTransaction'] = \
                    transaction.Transaction.from_dict(
                        jbody['orderReissueTransaction']
                    )

            if jbody.get('orderReissueRejectTransaction') is not None:
                parsed_body['orderReissueRejectTransaction'] = \
                    transaction.Transaction.from_dict(
                        jbody['orderReissueRejectTransaction']
                    )

            if jbody.get('replacingOrderCancelTransaction') is not None:
                parsed_body['replacingOrderCancelTransaction'] = \
                    transaction.OrderCancelTransaction.from_dict(
                        jbody['replacingOrderCancelTransaction']
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


        if str(response.status) == "400":
            if jbody.get('orderRejectTransaction') is not None:
                parsed_body['orderRejectTransaction'] = \
                    transaction.Transaction.from_dict(
                        jbody['orderRejectTransaction']
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

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


    def cancel(
        self,
        accountID,
        orderID,
        **kwargs
    ):
        """Cancel Order

        Cancel a pending Order in an Account

        Parameters
        ----------
        accountID : 
            ID of the Account to cancel an Order in
        orderID : 
            ID of the Order cancel
        """


        request = Request(
            'PUT',
            '/v3/accounts/{accountID}/orders/{orderID}/cancel'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'orderID',
            orderID
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('orderCancelTransaction') is not None:
                parsed_body['orderCancelTransaction'] = \
                    transaction.OrderCancelTransaction.from_dict(
                        jbody['orderCancelTransaction']
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


        if str(response.status) == "401":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')


        if str(response.status) == "404":
            if jbody.get('orderCancelRejectTransaction') is not None:
                parsed_body['orderCancelRejectTransaction'] = \
                    transaction.OrderCancelRejectTransaction.from_dict(
                        jbody['orderCancelRejectTransaction']
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

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


    def set_client_extensions(
        self,
        accountID,
        orderID,
        **kwargs
    ):
        """Set Order Extensions

        Update the Client Extensions for an Order in an Account. Do not set,
        modify, or delete clientExtensions if your account is associated with
        MT4.

        Parameters
        ----------
        accountID : 
            ID of the Account whose Order Client Extensions are being modified
        orderID : 
            ID of the Order cancel
        clientExtensions : None, optional
            The Client Extensions to update for the Order. Do not set, modify,
            or delete clientExtensions if your account is associated with MT4.
        tradeClientExtensions : None, optional
            The Client Extensions to update for the Trade created when the
            Order is filled. Do not set, modify, or delete clientExtensions if
            your account is associated with MT4.
        """


        request = Request(
            'PUT',
            '/v3/accounts/{accountID}/orders/{orderID}/clientExtensions'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'orderID',
            orderID
        )

        body = EntityDict()

        body.set('clientExtensions', kwargs.get('clientExtensions'))

        body.set('tradeClientExtensions', kwargs.get('tradeClientExtensions'))

        request.set_body_dict(body.dict)

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('orderClientExtensionsModifyTransaction') is not None:
                parsed_body['orderClientExtensionsModifyTransaction'] = \
                    transaction.OrderClientExtensionsModifyTransaction.from_dict(
                        jbody['orderClientExtensionsModifyTransaction']
                    )

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


        if str(response.status) == "400":
            if jbody.get('orderClientExtensionsModifyRejectTransaction') is not None:
                parsed_body['orderClientExtensionsModifyRejectTransaction'] = \
                    transaction.OrderClientExtensionsModifyRejectTransaction.from_dict(
                        jbody['orderClientExtensionsModifyRejectTransaction']
                    )

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

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



    def market(self, accountID, **kwargs):
        return self.create(
            accountID,
            order=MarketOrderRequest(**kwargs)
        )

    def limit(self, accountID, **kwargs):
        return self.create(
            accountID,
            order=LimitOrderRequest(**kwargs)
        )

    def stop(self, accountID, **kwargs):
        return self.create(
            accountID,
            order=StopOrderRequest(**kwargs)
        )

    def market_if_touched(self, accountID, **kwargs):
        return self.create(
            accountID,
            order=MarketIfTouchedOrderRequest(**kwargs)
        )
