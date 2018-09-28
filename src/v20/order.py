import ujson as json
from v20.base_entity import BaseEntity
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import spec_properties



class OrderIdentifier(BaseEntity):
    """
    An OrderIdentifier is used to refer to an Order, and contains both the
    OrderID and the ClientOrderID.
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
    _properties = spec_properties.order_OrderIdentifier

    def __init__(self, **kwargs):
        """
        Create a new OrderIdentifier instance
        """
        super(OrderIdentifier, self).__init__()
 
        #
        # The OANDA-assigned Order ID
        #
        self.orderID = kwargs.get("orderID")
 
        #
        # The client-provided client Order ID
        #
        self.clientOrderID = kwargs.get("clientOrderID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new OrderIdentifier from a dict (generally from loading a
        JSON response). The data used to instantiate the OrderIdentifier is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        return OrderIdentifier(**data)


class DynamicOrderState(BaseEntity):
    """
    The dynamic state of an Order. This is only relevant to TrailingStopLoss
    Orders, as no other Order type has dynamic state.
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
    _properties = spec_properties.order_DynamicOrderState

    def __init__(self, **kwargs):
        """
        Create a new DynamicOrderState instance
        """
        super(DynamicOrderState, self).__init__()
 
        #
        # The Order's ID.
        #
        self.id = kwargs.get("id")
 
        #
        # The Order's calculated trailing stop value.
        #
        self.trailingStopValue = kwargs.get("trailingStopValue")
 
        #
        # The distance between the Trailing Stop Loss Order's trailingStopValue
        # and the current Market Price. This represents the distance (in price
        # units) of the Order from a triggering price. If the distance could
        # not be determined, this value will not be set.
        #
        self.triggerDistance = kwargs.get("triggerDistance")
 
        #
        # True if an exact trigger distance could be calculated. If false, it
        # means the provided trigger distance is a best estimate. If the
        # distance could not be determined, this value will not be set.
        #
        self.isTriggerDistanceExact = kwargs.get("isTriggerDistanceExact")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new DynamicOrderState from a dict (generally from loading
        a JSON response). The data used to instantiate the DynamicOrderState is
        a shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('trailingStopValue') is not None:
            data['trailingStopValue'] = ctx.convert_decimal_number(
                data.get('trailingStopValue')
            )

        if data.get('triggerDistance') is not None:
            data['triggerDistance'] = ctx.convert_decimal_number(
                data.get('triggerDistance')
            )

        return DynamicOrderState(**data)


class Order(BaseEntity):
    """
    The base Order definition specifies the properties that are common to all
    Orders.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = ""

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Order {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_Order

    def __init__(self, **kwargs):
        """
        Create a new Order instance
        """
        super(Order, self).__init__()
 
        #
        # The Order's identifier, unique within the Order's Account.
        #
        self.id = kwargs.get("id")
 
        #
        # The time when the Order was created.
        #
        self.createTime = kwargs.get("createTime")
 
        #
        # The current state of the Order.
        #
        self.state = kwargs.get("state")
 
        #
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new Order from a dict (generally from loading a JSON
        response). The data used to instantiate the Order is a shallow copy of
        the dict passed in, with any complex child types instantiated
        appropriately.
        """

        type = data.get("type")

        if type == "TAKE_PROFIT":
            return TakeProfitOrder.from_dict(data, ctx)
        if type == "STOP_LOSS":
            return StopLossOrder.from_dict(data, ctx)
        if type == "TRAILING_STOP_LOSS":
            return TrailingStopLossOrder.from_dict(data, ctx)
        if type == "MARKET":
            return MarketOrder.from_dict(data, ctx)
        if type == "FIXED_PRICE":
            return FixedPriceOrder.from_dict(data, ctx)
        if type == "LIMIT":
            return LimitOrder.from_dict(data, ctx)
        if type == "STOP":
            return StopOrder.from_dict(data, ctx)
        if type == "MARKET_IF_TOUCHED":
            return MarketIfTouchedOrder.from_dict(data, ctx)

        data = data.copy()

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        return Order(**data)


class MarketOrder(BaseEntity):
    """
    A MarketOrder is an order that is filled immediately upon creation using
    the current market price.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "{units} units of {instrument}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Market Order {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_MarketOrder

    def __init__(self, **kwargs):
        """
        Create a new MarketOrder instance
        """
        super(MarketOrder, self).__init__()
 
        #
        # The Order's identifier, unique within the Order's Account.
        #
        self.id = kwargs.get("id")
 
        #
        # The time when the Order was created.
        #
        self.createTime = kwargs.get("createTime")
 
        #
        # The current state of the Order.
        #
        self.state = kwargs.get("state")
 
        #
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The type of the Order. Always set to "MARKET" for Market Orders.
        #
        self.type = kwargs.get("type", "MARKET")
 
        #
        # The Market Order's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The quantity requested to be filled by the Market Order. A posititive
        # number of units results in a long Order, and a negative number of
        # units results in a short Order.
        #
        self.units = kwargs.get("units")
 
        #
        # The time-in-force requested for the Market Order. Restricted to FOK
        # or IOC for a MarketOrder.
        #
        self.timeInForce = kwargs.get("timeInForce", "FOK")
 
        #
        # The worst price that the client is willing to have the Market Order
        # filled at.
        #
        self.priceBound = kwargs.get("priceBound")
 
        #
        # Specification of how Positions in the Account are modified when the
        # Order is filled.
        #
        self.positionFill = kwargs.get("positionFill", "DEFAULT")
 
        #
        # Details of the Trade requested to be closed, only provided when the
        # Market Order is being used to explicitly close a Trade.
        #
        self.tradeClose = kwargs.get("tradeClose")
 
        #
        # Details of the long Position requested to be closed out, only
        # provided when a Market Order is being used to explicitly closeout a
        # long Position.
        #
        self.longPositionCloseout = kwargs.get("longPositionCloseout")
 
        #
        # Details of the short Position requested to be closed out, only
        # provided when a Market Order is being used to explicitly closeout a
        # short Position.
        #
        self.shortPositionCloseout = kwargs.get("shortPositionCloseout")
 
        #
        # Details of the Margin Closeout that this Market Order was created for
        #
        self.marginCloseout = kwargs.get("marginCloseout")
 
        #
        # Details of the delayed Trade close that this Market Order was created
        # for
        #
        self.delayedTradeClose = kwargs.get("delayedTradeClose")
 
        #
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Take Profit, or when a Trade's
        # dependent Take Profit Order is modified directly through the Trade.
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # StopLossDetails specifies the details of a Stop Loss Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Stop Loss, or when a Trade's
        # dependent Stop Loss Order is modified directly through the Trade.
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an
        # Order is filled that opens a Trade requiring a Trailing Stop Loss, or
        # when a Trade's dependent Trailing Stop Loss Order is modified
        # directly through the Trade.
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")
 
        #
        # ID of the Transaction that filled this Order (only provided when the
        # Order's state is FILLED)
        #
        self.fillingTransactionID = kwargs.get("fillingTransactionID")
 
        #
        # Date/time when the Order was filled (only provided when the Order's
        # state is FILLED)
        #
        self.filledTime = kwargs.get("filledTime")
 
        #
        # Trade ID of Trade opened when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was opened as a result
        # of the fill)
        #
        self.tradeOpenedID = kwargs.get("tradeOpenedID")
 
        #
        # Trade ID of Trade reduced when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was reduced as a result
        # of the fill)
        #
        self.tradeReducedID = kwargs.get("tradeReducedID")
 
        #
        # Trade IDs of Trades closed when the Order was filled (only provided
        # when the Order's state is FILLED and one or more Trades were closed
        # as a result of the fill)
        #
        self.tradeClosedIDs = kwargs.get("tradeClosedIDs")
 
        #
        # ID of the Transaction that cancelled the Order (only provided when
        # the Order's state is CANCELLED)
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")
 
        #
        # Date/time when the Order was cancelled (only provided when the state
        # of the Order is CANCELLED)
        #
        self.cancelledTime = kwargs.get("cancelledTime")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarketOrder from a dict (generally from loading a
        JSON response). The data used to instantiate the MarketOrder is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('units') is not None:
            data['units'] = ctx.convert_decimal_number(
                data.get('units')
            )

        if data.get('priceBound') is not None:
            data['priceBound'] = ctx.convert_decimal_number(
                data.get('priceBound')
            )

        if data.get('tradeClose') is not None:
            data['tradeClose'] = \
                ctx.transaction.MarketOrderTradeClose.from_dict(
                    data['tradeClose'], ctx
                )

        if data.get('longPositionCloseout') is not None:
            data['longPositionCloseout'] = \
                ctx.transaction.MarketOrderPositionCloseout.from_dict(
                    data['longPositionCloseout'], ctx
                )

        if data.get('shortPositionCloseout') is not None:
            data['shortPositionCloseout'] = \
                ctx.transaction.MarketOrderPositionCloseout.from_dict(
                    data['shortPositionCloseout'], ctx
                )

        if data.get('marginCloseout') is not None:
            data['marginCloseout'] = \
                ctx.transaction.MarketOrderMarginCloseout.from_dict(
                    data['marginCloseout'], ctx
                )

        if data.get('delayedTradeClose') is not None:
            data['delayedTradeClose'] = \
                ctx.transaction.MarketOrderDelayedTradeClose.from_dict(
                    data['delayedTradeClose'], ctx
                )

        if data.get('takeProfitOnFill') is not None:
            data['takeProfitOnFill'] = \
                ctx.transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill'], ctx
                )

        if data.get('stopLossOnFill') is not None:
            data['stopLossOnFill'] = \
                ctx.transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill'], ctx
                )

        if data.get('trailingStopLossOnFill') is not None:
            data['trailingStopLossOnFill'] = \
                ctx.transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill'], ctx
                )

        if data.get('tradeClientExtensions') is not None:
            data['tradeClientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions'], ctx
                )


        return MarketOrder(**data)


class FixedPriceOrder(BaseEntity):
    """
    A FixedPriceOrder is an order that is filled immediately upon creation
    using a fixed price.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "{units} units of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Fixed Price Order {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_FixedPriceOrder

    def __init__(self, **kwargs):
        """
        Create a new FixedPriceOrder instance
        """
        super(FixedPriceOrder, self).__init__()
 
        #
        # The Order's identifier, unique within the Order's Account.
        #
        self.id = kwargs.get("id")
 
        #
        # The time when the Order was created.
        #
        self.createTime = kwargs.get("createTime")
 
        #
        # The current state of the Order.
        #
        self.state = kwargs.get("state")
 
        #
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The type of the Order. Always set to "FIXED_PRICE" for Fixed Price
        # Orders.
        #
        self.type = kwargs.get("type", "FIXED_PRICE")
 
        #
        # The Fixed Price Order's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The quantity requested to be filled by the Fixed Price Order. A
        # posititive number of units results in a long Order, and a negative
        # number of units results in a short Order.
        #
        self.units = kwargs.get("units")
 
        #
        # The price specified for the Fixed Price Order. This price is the
        # exact price that the Fixed Price Order will be filled at.
        #
        self.price = kwargs.get("price")
 
        #
        # Specification of how Positions in the Account are modified when the
        # Order is filled.
        #
        self.positionFill = kwargs.get("positionFill", "DEFAULT")
 
        #
        # The state that the trade resulting from the Fixed Price Order should
        # be set to.
        #
        self.tradeState = kwargs.get("tradeState")
 
        #
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Take Profit, or when a Trade's
        # dependent Take Profit Order is modified directly through the Trade.
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # StopLossDetails specifies the details of a Stop Loss Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Stop Loss, or when a Trade's
        # dependent Stop Loss Order is modified directly through the Trade.
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an
        # Order is filled that opens a Trade requiring a Trailing Stop Loss, or
        # when a Trade's dependent Trailing Stop Loss Order is modified
        # directly through the Trade.
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")
 
        #
        # ID of the Transaction that filled this Order (only provided when the
        # Order's state is FILLED)
        #
        self.fillingTransactionID = kwargs.get("fillingTransactionID")
 
        #
        # Date/time when the Order was filled (only provided when the Order's
        # state is FILLED)
        #
        self.filledTime = kwargs.get("filledTime")
 
        #
        # Trade ID of Trade opened when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was opened as a result
        # of the fill)
        #
        self.tradeOpenedID = kwargs.get("tradeOpenedID")
 
        #
        # Trade ID of Trade reduced when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was reduced as a result
        # of the fill)
        #
        self.tradeReducedID = kwargs.get("tradeReducedID")
 
        #
        # Trade IDs of Trades closed when the Order was filled (only provided
        # when the Order's state is FILLED and one or more Trades were closed
        # as a result of the fill)
        #
        self.tradeClosedIDs = kwargs.get("tradeClosedIDs")
 
        #
        # ID of the Transaction that cancelled the Order (only provided when
        # the Order's state is CANCELLED)
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")
 
        #
        # Date/time when the Order was cancelled (only provided when the state
        # of the Order is CANCELLED)
        #
        self.cancelledTime = kwargs.get("cancelledTime")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new FixedPriceOrder from a dict (generally from loading a
        JSON response). The data used to instantiate the FixedPriceOrder is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('units') is not None:
            data['units'] = ctx.convert_decimal_number(
                data.get('units')
            )

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('takeProfitOnFill') is not None:
            data['takeProfitOnFill'] = \
                ctx.transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill'], ctx
                )

        if data.get('stopLossOnFill') is not None:
            data['stopLossOnFill'] = \
                ctx.transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill'], ctx
                )

        if data.get('trailingStopLossOnFill') is not None:
            data['trailingStopLossOnFill'] = \
                ctx.transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill'], ctx
                )

        if data.get('tradeClientExtensions') is not None:
            data['tradeClientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions'], ctx
                )


        return FixedPriceOrder(**data)


class LimitOrder(BaseEntity):
    """
    A LimitOrder is an order that is created with a price threshold, and will
    only be filled by a price that is equal to or better than the threshold.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "{units} units of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Limit Order {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_LimitOrder

    def __init__(self, **kwargs):
        """
        Create a new LimitOrder instance
        """
        super(LimitOrder, self).__init__()
 
        #
        # The Order's identifier, unique within the Order's Account.
        #
        self.id = kwargs.get("id")
 
        #
        # The time when the Order was created.
        #
        self.createTime = kwargs.get("createTime")
 
        #
        # The current state of the Order.
        #
        self.state = kwargs.get("state")
 
        #
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The type of the Order. Always set to "LIMIT" for Limit Orders.
        #
        self.type = kwargs.get("type", "LIMIT")
 
        #
        # The Limit Order's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The quantity requested to be filled by the Limit Order. A posititive
        # number of units results in a long Order, and a negative number of
        # units results in a short Order.
        #
        self.units = kwargs.get("units")
 
        #
        # The price threshold specified for the Limit Order. The Limit Order
        # will only be filled by a market price that is equal to or better than
        # this price.
        #
        self.price = kwargs.get("price")
 
        #
        # The time-in-force requested for the Limit Order.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date/time when the Limit Order will be cancelled if its
        # timeInForce is "GTD".
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # Specification of how Positions in the Account are modified when the
        # Order is filled.
        #
        self.positionFill = kwargs.get("positionFill", "DEFAULT")
 
        #
        # Specification of which price component should be used when
        # determining if an Order should be triggered and filled. This allows
        # Orders to be triggered based on the bid, ask, mid, default (ask for
        # buy, bid for sell) or inverse (ask for sell, bid for buy) price
        # depending on the desired behaviour. Orders are always filled using
        # their default price component. This feature is only provided through
        # the REST API. Clients who choose to specify a non-default trigger
        # condition will not see it reflected in any of OANDA's proprietary or
        # partner trading platforms, their transaction history or their account
        # statements. OANDA platforms always assume that an Order's trigger
        # condition is set to the default value when indicating the distance
        # from an Order's trigger price, and will always provide the default
        # trigger condition when creating or modifying an Order. A special
        # restriction applies when creating a guaranteed Stop Loss Order. In
        # this case the TriggerCondition value must either be "DEFAULT", or the
        # "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order
        # for a long trade valid values are "DEFAULT" and "BID", and for short
        # trades "DEFAULT" and "ASK" are valid.
        #
        self.triggerCondition = kwargs.get("triggerCondition", "DEFAULT")
 
        #
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Take Profit, or when a Trade's
        # dependent Take Profit Order is modified directly through the Trade.
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # StopLossDetails specifies the details of a Stop Loss Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Stop Loss, or when a Trade's
        # dependent Stop Loss Order is modified directly through the Trade.
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an
        # Order is filled that opens a Trade requiring a Trailing Stop Loss, or
        # when a Trade's dependent Trailing Stop Loss Order is modified
        # directly through the Trade.
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")
 
        #
        # ID of the Transaction that filled this Order (only provided when the
        # Order's state is FILLED)
        #
        self.fillingTransactionID = kwargs.get("fillingTransactionID")
 
        #
        # Date/time when the Order was filled (only provided when the Order's
        # state is FILLED)
        #
        self.filledTime = kwargs.get("filledTime")
 
        #
        # Trade ID of Trade opened when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was opened as a result
        # of the fill)
        #
        self.tradeOpenedID = kwargs.get("tradeOpenedID")
 
        #
        # Trade ID of Trade reduced when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was reduced as a result
        # of the fill)
        #
        self.tradeReducedID = kwargs.get("tradeReducedID")
 
        #
        # Trade IDs of Trades closed when the Order was filled (only provided
        # when the Order's state is FILLED and one or more Trades were closed
        # as a result of the fill)
        #
        self.tradeClosedIDs = kwargs.get("tradeClosedIDs")
 
        #
        # ID of the Transaction that cancelled the Order (only provided when
        # the Order's state is CANCELLED)
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")
 
        #
        # Date/time when the Order was cancelled (only provided when the state
        # of the Order is CANCELLED)
        #
        self.cancelledTime = kwargs.get("cancelledTime")
 
        #
        # The ID of the Order that was replaced by this Order (only provided if
        # this Order was created as part of a cancel/replace).
        #
        self.replacesOrderID = kwargs.get("replacesOrderID")
 
        #
        # The ID of the Order that replaced this Order (only provided if this
        # Order was cancelled as part of a cancel/replace).
        #
        self.replacedByOrderID = kwargs.get("replacedByOrderID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new LimitOrder from a dict (generally from loading a JSON
        response). The data used to instantiate the LimitOrder is a shallow
        copy of the dict passed in, with any complex child types instantiated
        appropriately.
        """

        data = data.copy()

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('units') is not None:
            data['units'] = ctx.convert_decimal_number(
                data.get('units')
            )

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('takeProfitOnFill') is not None:
            data['takeProfitOnFill'] = \
                ctx.transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill'], ctx
                )

        if data.get('stopLossOnFill') is not None:
            data['stopLossOnFill'] = \
                ctx.transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill'], ctx
                )

        if data.get('trailingStopLossOnFill') is not None:
            data['trailingStopLossOnFill'] = \
                ctx.transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill'], ctx
                )

        if data.get('tradeClientExtensions') is not None:
            data['tradeClientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions'], ctx
                )


        return LimitOrder(**data)


class StopOrder(BaseEntity):
    """
    A StopOrder is an order that is created with a price threshold, and will
    only be filled by a price that is equal to or worse than the threshold.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "{units} units of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Stop Order {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_StopOrder

    def __init__(self, **kwargs):
        """
        Create a new StopOrder instance
        """
        super(StopOrder, self).__init__()
 
        #
        # The Order's identifier, unique within the Order's Account.
        #
        self.id = kwargs.get("id")
 
        #
        # The time when the Order was created.
        #
        self.createTime = kwargs.get("createTime")
 
        #
        # The current state of the Order.
        #
        self.state = kwargs.get("state")
 
        #
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The type of the Order. Always set to "STOP" for Stop Orders.
        #
        self.type = kwargs.get("type", "STOP")
 
        #
        # The Stop Order's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The quantity requested to be filled by the Stop Order. A posititive
        # number of units results in a long Order, and a negative number of
        # units results in a short Order.
        #
        self.units = kwargs.get("units")
 
        #
        # The price threshold specified for the Stop Order. The Stop Order will
        # only be filled by a market price that is equal to or worse than this
        # price.
        #
        self.price = kwargs.get("price")
 
        #
        # The worst market price that may be used to fill this Stop Order. If
        # the market gaps and crosses through both the price and the
        # priceBound, the Stop Order will be cancelled instead of being filled.
        #
        self.priceBound = kwargs.get("priceBound")
 
        #
        # The time-in-force requested for the Stop Order.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date/time when the Stop Order will be cancelled if its
        # timeInForce is "GTD".
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # Specification of how Positions in the Account are modified when the
        # Order is filled.
        #
        self.positionFill = kwargs.get("positionFill", "DEFAULT")
 
        #
        # Specification of which price component should be used when
        # determining if an Order should be triggered and filled. This allows
        # Orders to be triggered based on the bid, ask, mid, default (ask for
        # buy, bid for sell) or inverse (ask for sell, bid for buy) price
        # depending on the desired behaviour. Orders are always filled using
        # their default price component. This feature is only provided through
        # the REST API. Clients who choose to specify a non-default trigger
        # condition will not see it reflected in any of OANDA's proprietary or
        # partner trading platforms, their transaction history or their account
        # statements. OANDA platforms always assume that an Order's trigger
        # condition is set to the default value when indicating the distance
        # from an Order's trigger price, and will always provide the default
        # trigger condition when creating or modifying an Order. A special
        # restriction applies when creating a guaranteed Stop Loss Order. In
        # this case the TriggerCondition value must either be "DEFAULT", or the
        # "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order
        # for a long trade valid values are "DEFAULT" and "BID", and for short
        # trades "DEFAULT" and "ASK" are valid.
        #
        self.triggerCondition = kwargs.get("triggerCondition", "DEFAULT")
 
        #
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Take Profit, or when a Trade's
        # dependent Take Profit Order is modified directly through the Trade.
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # StopLossDetails specifies the details of a Stop Loss Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Stop Loss, or when a Trade's
        # dependent Stop Loss Order is modified directly through the Trade.
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an
        # Order is filled that opens a Trade requiring a Trailing Stop Loss, or
        # when a Trade's dependent Trailing Stop Loss Order is modified
        # directly through the Trade.
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")
 
        #
        # ID of the Transaction that filled this Order (only provided when the
        # Order's state is FILLED)
        #
        self.fillingTransactionID = kwargs.get("fillingTransactionID")
 
        #
        # Date/time when the Order was filled (only provided when the Order's
        # state is FILLED)
        #
        self.filledTime = kwargs.get("filledTime")
 
        #
        # Trade ID of Trade opened when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was opened as a result
        # of the fill)
        #
        self.tradeOpenedID = kwargs.get("tradeOpenedID")
 
        #
        # Trade ID of Trade reduced when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was reduced as a result
        # of the fill)
        #
        self.tradeReducedID = kwargs.get("tradeReducedID")
 
        #
        # Trade IDs of Trades closed when the Order was filled (only provided
        # when the Order's state is FILLED and one or more Trades were closed
        # as a result of the fill)
        #
        self.tradeClosedIDs = kwargs.get("tradeClosedIDs")
 
        #
        # ID of the Transaction that cancelled the Order (only provided when
        # the Order's state is CANCELLED)
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")
 
        #
        # Date/time when the Order was cancelled (only provided when the state
        # of the Order is CANCELLED)
        #
        self.cancelledTime = kwargs.get("cancelledTime")
 
        #
        # The ID of the Order that was replaced by this Order (only provided if
        # this Order was created as part of a cancel/replace).
        #
        self.replacesOrderID = kwargs.get("replacesOrderID")
 
        #
        # The ID of the Order that replaced this Order (only provided if this
        # Order was cancelled as part of a cancel/replace).
        #
        self.replacedByOrderID = kwargs.get("replacedByOrderID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new StopOrder from a dict (generally from loading a JSON
        response). The data used to instantiate the StopOrder is a shallow copy
        of the dict passed in, with any complex child types instantiated
        appropriately.
        """

        data = data.copy()

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('units') is not None:
            data['units'] = ctx.convert_decimal_number(
                data.get('units')
            )

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('priceBound') is not None:
            data['priceBound'] = ctx.convert_decimal_number(
                data.get('priceBound')
            )

        if data.get('takeProfitOnFill') is not None:
            data['takeProfitOnFill'] = \
                ctx.transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill'], ctx
                )

        if data.get('stopLossOnFill') is not None:
            data['stopLossOnFill'] = \
                ctx.transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill'], ctx
                )

        if data.get('trailingStopLossOnFill') is not None:
            data['trailingStopLossOnFill'] = \
                ctx.transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill'], ctx
                )

        if data.get('tradeClientExtensions') is not None:
            data['tradeClientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions'], ctx
                )


        return StopOrder(**data)


class MarketIfTouchedOrder(BaseEntity):
    """
    A MarketIfTouchedOrder is an order that is created with a price threshold,
    and will only be filled by a market price that is touches or crosses the
    threshold.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "{units} units of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "MIT Order {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_MarketIfTouchedOrder

    def __init__(self, **kwargs):
        """
        Create a new MarketIfTouchedOrder instance
        """
        super(MarketIfTouchedOrder, self).__init__()
 
        #
        # The Order's identifier, unique within the Order's Account.
        #
        self.id = kwargs.get("id")
 
        #
        # The time when the Order was created.
        #
        self.createTime = kwargs.get("createTime")
 
        #
        # The current state of the Order.
        #
        self.state = kwargs.get("state")
 
        #
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The type of the Order. Always set to "MARKET_IF_TOUCHED" for Market
        # If Touched Orders.
        #
        self.type = kwargs.get("type", "MARKET_IF_TOUCHED")
 
        #
        # The MarketIfTouched Order's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The quantity requested to be filled by the MarketIfTouched Order. A
        # posititive number of units results in a long Order, and a negative
        # number of units results in a short Order.
        #
        self.units = kwargs.get("units")
 
        #
        # The price threshold specified for the MarketIfTouched Order. The
        # MarketIfTouched Order will only be filled by a market price that
        # crosses this price from the direction of the market price at the time
        # when the Order was created (the initialMarketPrice). Depending on the
        # value of the Order's price and initialMarketPrice, the
        # MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        #
        self.price = kwargs.get("price")
 
        #
        # The worst market price that may be used to fill this MarketIfTouched
        # Order.
        #
        self.priceBound = kwargs.get("priceBound")
 
        #
        # The time-in-force requested for the MarketIfTouched Order. Restricted
        # to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date/time when the MarketIfTouched Order will be cancelled if its
        # timeInForce is "GTD".
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # Specification of how Positions in the Account are modified when the
        # Order is filled.
        #
        self.positionFill = kwargs.get("positionFill", "DEFAULT")
 
        #
        # Specification of which price component should be used when
        # determining if an Order should be triggered and filled. This allows
        # Orders to be triggered based on the bid, ask, mid, default (ask for
        # buy, bid for sell) or inverse (ask for sell, bid for buy) price
        # depending on the desired behaviour. Orders are always filled using
        # their default price component. This feature is only provided through
        # the REST API. Clients who choose to specify a non-default trigger
        # condition will not see it reflected in any of OANDA's proprietary or
        # partner trading platforms, their transaction history or their account
        # statements. OANDA platforms always assume that an Order's trigger
        # condition is set to the default value when indicating the distance
        # from an Order's trigger price, and will always provide the default
        # trigger condition when creating or modifying an Order. A special
        # restriction applies when creating a guaranteed Stop Loss Order. In
        # this case the TriggerCondition value must either be "DEFAULT", or the
        # "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order
        # for a long trade valid values are "DEFAULT" and "BID", and for short
        # trades "DEFAULT" and "ASK" are valid.
        #
        self.triggerCondition = kwargs.get("triggerCondition", "DEFAULT")
 
        #
        # The Market price at the time when the MarketIfTouched Order was
        # created.
        #
        self.initialMarketPrice = kwargs.get("initialMarketPrice")
 
        #
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Take Profit, or when a Trade's
        # dependent Take Profit Order is modified directly through the Trade.
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # StopLossDetails specifies the details of a Stop Loss Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Stop Loss, or when a Trade's
        # dependent Stop Loss Order is modified directly through the Trade.
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an
        # Order is filled that opens a Trade requiring a Trailing Stop Loss, or
        # when a Trade's dependent Trailing Stop Loss Order is modified
        # directly through the Trade.
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")
 
        #
        # ID of the Transaction that filled this Order (only provided when the
        # Order's state is FILLED)
        #
        self.fillingTransactionID = kwargs.get("fillingTransactionID")
 
        #
        # Date/time when the Order was filled (only provided when the Order's
        # state is FILLED)
        #
        self.filledTime = kwargs.get("filledTime")
 
        #
        # Trade ID of Trade opened when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was opened as a result
        # of the fill)
        #
        self.tradeOpenedID = kwargs.get("tradeOpenedID")
 
        #
        # Trade ID of Trade reduced when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was reduced as a result
        # of the fill)
        #
        self.tradeReducedID = kwargs.get("tradeReducedID")
 
        #
        # Trade IDs of Trades closed when the Order was filled (only provided
        # when the Order's state is FILLED and one or more Trades were closed
        # as a result of the fill)
        #
        self.tradeClosedIDs = kwargs.get("tradeClosedIDs")
 
        #
        # ID of the Transaction that cancelled the Order (only provided when
        # the Order's state is CANCELLED)
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")
 
        #
        # Date/time when the Order was cancelled (only provided when the state
        # of the Order is CANCELLED)
        #
        self.cancelledTime = kwargs.get("cancelledTime")
 
        #
        # The ID of the Order that was replaced by this Order (only provided if
        # this Order was created as part of a cancel/replace).
        #
        self.replacesOrderID = kwargs.get("replacesOrderID")
 
        #
        # The ID of the Order that replaced this Order (only provided if this
        # Order was cancelled as part of a cancel/replace).
        #
        self.replacedByOrderID = kwargs.get("replacedByOrderID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarketIfTouchedOrder from a dict (generally from
        loading a JSON response). The data used to instantiate the
        MarketIfTouchedOrder is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('units') is not None:
            data['units'] = ctx.convert_decimal_number(
                data.get('units')
            )

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('priceBound') is not None:
            data['priceBound'] = ctx.convert_decimal_number(
                data.get('priceBound')
            )

        if data.get('initialMarketPrice') is not None:
            data['initialMarketPrice'] = ctx.convert_decimal_number(
                data.get('initialMarketPrice')
            )

        if data.get('takeProfitOnFill') is not None:
            data['takeProfitOnFill'] = \
                ctx.transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill'], ctx
                )

        if data.get('stopLossOnFill') is not None:
            data['stopLossOnFill'] = \
                ctx.transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill'], ctx
                )

        if data.get('trailingStopLossOnFill') is not None:
            data['trailingStopLossOnFill'] = \
                ctx.transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill'], ctx
                )

        if data.get('tradeClientExtensions') is not None:
            data['tradeClientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions'], ctx
                )


        return MarketIfTouchedOrder(**data)


class TakeProfitOrder(BaseEntity):
    """
    A TakeProfitOrder is an order that is linked to an open Trade and created
    with a price threshold. The Order will be filled (closing the Trade) by the
    first price that is equal to or better than the threshold. A
    TakeProfitOrder cannot be used to open a new Position.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Take Profit for Trade {tradeID} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "TP Order {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_TakeProfitOrder

    def __init__(self, **kwargs):
        """
        Create a new TakeProfitOrder instance
        """
        super(TakeProfitOrder, self).__init__()
 
        #
        # The Order's identifier, unique within the Order's Account.
        #
        self.id = kwargs.get("id")
 
        #
        # The time when the Order was created.
        #
        self.createTime = kwargs.get("createTime")
 
        #
        # The current state of the Order.
        #
        self.state = kwargs.get("state")
 
        #
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The type of the Order. Always set to "TAKE_PROFIT" for Take Profit
        # Orders.
        #
        self.type = kwargs.get("type", "TAKE_PROFIT")
 
        #
        # The ID of the Trade to close when the price threshold is breached.
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The client ID of the Trade to be closed when the price threshold is
        # breached.
        #
        self.clientTradeID = kwargs.get("clientTradeID")
 
        #
        # The price threshold specified for the TakeProfit Order. The
        # associated Trade will be closed by a market price that is equal to or
        # better than this threshold.
        #
        self.price = kwargs.get("price")
 
        #
        # The time-in-force requested for the TakeProfit Order. Restricted to
        # "GTC", "GFD" and "GTD" for TakeProfit Orders.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date/time when the TakeProfit Order will be cancelled if its
        # timeInForce is "GTD".
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # Specification of which price component should be used when
        # determining if an Order should be triggered and filled. This allows
        # Orders to be triggered based on the bid, ask, mid, default (ask for
        # buy, bid for sell) or inverse (ask for sell, bid for buy) price
        # depending on the desired behaviour. Orders are always filled using
        # their default price component. This feature is only provided through
        # the REST API. Clients who choose to specify a non-default trigger
        # condition will not see it reflected in any of OANDA's proprietary or
        # partner trading platforms, their transaction history or their account
        # statements. OANDA platforms always assume that an Order's trigger
        # condition is set to the default value when indicating the distance
        # from an Order's trigger price, and will always provide the default
        # trigger condition when creating or modifying an Order. A special
        # restriction applies when creating a guaranteed Stop Loss Order. In
        # this case the TriggerCondition value must either be "DEFAULT", or the
        # "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order
        # for a long trade valid values are "DEFAULT" and "BID", and for short
        # trades "DEFAULT" and "ASK" are valid.
        #
        self.triggerCondition = kwargs.get("triggerCondition", "DEFAULT")
 
        #
        # ID of the Transaction that filled this Order (only provided when the
        # Order's state is FILLED)
        #
        self.fillingTransactionID = kwargs.get("fillingTransactionID")
 
        #
        # Date/time when the Order was filled (only provided when the Order's
        # state is FILLED)
        #
        self.filledTime = kwargs.get("filledTime")
 
        #
        # Trade ID of Trade opened when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was opened as a result
        # of the fill)
        #
        self.tradeOpenedID = kwargs.get("tradeOpenedID")
 
        #
        # Trade ID of Trade reduced when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was reduced as a result
        # of the fill)
        #
        self.tradeReducedID = kwargs.get("tradeReducedID")
 
        #
        # Trade IDs of Trades closed when the Order was filled (only provided
        # when the Order's state is FILLED and one or more Trades were closed
        # as a result of the fill)
        #
        self.tradeClosedIDs = kwargs.get("tradeClosedIDs")
 
        #
        # ID of the Transaction that cancelled the Order (only provided when
        # the Order's state is CANCELLED)
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")
 
        #
        # Date/time when the Order was cancelled (only provided when the state
        # of the Order is CANCELLED)
        #
        self.cancelledTime = kwargs.get("cancelledTime")
 
        #
        # The ID of the Order that was replaced by this Order (only provided if
        # this Order was created as part of a cancel/replace).
        #
        self.replacesOrderID = kwargs.get("replacesOrderID")
 
        #
        # The ID of the Order that replaced this Order (only provided if this
        # Order was cancelled as part of a cancel/replace).
        #
        self.replacedByOrderID = kwargs.get("replacedByOrderID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TakeProfitOrder from a dict (generally from loading a
        JSON response). The data used to instantiate the TakeProfitOrder is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )


        return TakeProfitOrder(**data)


class StopLossOrder(BaseEntity):
    """
    A StopLossOrder is an order that is linked to an open Trade and created
    with a price threshold. The Order will be filled (closing the Trade) by the
    first price that is equal to or worse than the threshold. A StopLossOrder
    cannot be used to open a new Position.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Stop Loss for Trade {tradeID} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "SL Order {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_StopLossOrder

    def __init__(self, **kwargs):
        """
        Create a new StopLossOrder instance
        """
        super(StopLossOrder, self).__init__()
 
        #
        # The Order's identifier, unique within the Order's Account.
        #
        self.id = kwargs.get("id")
 
        #
        # The time when the Order was created.
        #
        self.createTime = kwargs.get("createTime")
 
        #
        # The current state of the Order.
        #
        self.state = kwargs.get("state")
 
        #
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The type of the Order. Always set to "STOP_LOSS" for Stop Loss
        # Orders.
        #
        self.type = kwargs.get("type", "STOP_LOSS")
 
        #
        # The premium that will be charged if the Stop Loss Order is guaranteed
        # and the Order is filled at the guaranteed price. It is in price units
        # and is charged for each unit of the Trade.
        #
        self.guaranteedExecutionPremium = kwargs.get("guaranteedExecutionPremium")
 
        #
        # The ID of the Trade to close when the price threshold is breached.
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The client ID of the Trade to be closed when the price threshold is
        # breached.
        #
        self.clientTradeID = kwargs.get("clientTradeID")
 
        #
        # The price threshold specified for the Stop Loss Order. If the
        # guaranteed flag is false, the associated Trade will be closed by a
        # market price that is equal to or worse than this threshold. If the
        # flag is true the associated Trade will be closed at this price.
        #
        self.price = kwargs.get("price")
 
        #
        # Specifies the distance (in price units) from the Account's current
        # price to use as the Stop Loss Order price. If the Trade is short the
        # Instrument's bid price is used, and for long Trades the ask is used.
        #
        self.distance = kwargs.get("distance")
 
        #
        # The time-in-force requested for the StopLoss Order. Restricted to
        # "GTC", "GFD" and "GTD" for StopLoss Orders.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date/time when the StopLoss Order will be cancelled if its
        # timeInForce is "GTD".
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # Specification of which price component should be used when
        # determining if an Order should be triggered and filled. This allows
        # Orders to be triggered based on the bid, ask, mid, default (ask for
        # buy, bid for sell) or inverse (ask for sell, bid for buy) price
        # depending on the desired behaviour. Orders are always filled using
        # their default price component. This feature is only provided through
        # the REST API. Clients who choose to specify a non-default trigger
        # condition will not see it reflected in any of OANDA's proprietary or
        # partner trading platforms, their transaction history or their account
        # statements. OANDA platforms always assume that an Order's trigger
        # condition is set to the default value when indicating the distance
        # from an Order's trigger price, and will always provide the default
        # trigger condition when creating or modifying an Order. A special
        # restriction applies when creating a guaranteed Stop Loss Order. In
        # this case the TriggerCondition value must either be "DEFAULT", or the
        # "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order
        # for a long trade valid values are "DEFAULT" and "BID", and for short
        # trades "DEFAULT" and "ASK" are valid.
        #
        self.triggerCondition = kwargs.get("triggerCondition", "DEFAULT")
 
        #
        # Flag indicating that the Stop Loss Order is guaranteed. The default
        # value depends on the GuaranteedStopLossOrderMode of the account, if
        # it is REQUIRED, the default will be true, for DISABLED or ENABLED the
        # default is false.
        #
        self.guaranteed = kwargs.get("guaranteed")
 
        #
        # ID of the Transaction that filled this Order (only provided when the
        # Order's state is FILLED)
        #
        self.fillingTransactionID = kwargs.get("fillingTransactionID")
 
        #
        # Date/time when the Order was filled (only provided when the Order's
        # state is FILLED)
        #
        self.filledTime = kwargs.get("filledTime")
 
        #
        # Trade ID of Trade opened when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was opened as a result
        # of the fill)
        #
        self.tradeOpenedID = kwargs.get("tradeOpenedID")
 
        #
        # Trade ID of Trade reduced when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was reduced as a result
        # of the fill)
        #
        self.tradeReducedID = kwargs.get("tradeReducedID")
 
        #
        # Trade IDs of Trades closed when the Order was filled (only provided
        # when the Order's state is FILLED and one or more Trades were closed
        # as a result of the fill)
        #
        self.tradeClosedIDs = kwargs.get("tradeClosedIDs")
 
        #
        # ID of the Transaction that cancelled the Order (only provided when
        # the Order's state is CANCELLED)
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")
 
        #
        # Date/time when the Order was cancelled (only provided when the state
        # of the Order is CANCELLED)
        #
        self.cancelledTime = kwargs.get("cancelledTime")
 
        #
        # The ID of the Order that was replaced by this Order (only provided if
        # this Order was created as part of a cancel/replace).
        #
        self.replacesOrderID = kwargs.get("replacesOrderID")
 
        #
        # The ID of the Order that replaced this Order (only provided if this
        # Order was cancelled as part of a cancel/replace).
        #
        self.replacedByOrderID = kwargs.get("replacedByOrderID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new StopLossOrder from a dict (generally from loading a
        JSON response). The data used to instantiate the StopLossOrder is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('guaranteedExecutionPremium') is not None:
            data['guaranteedExecutionPremium'] = ctx.convert_decimal_number(
                data.get('guaranteedExecutionPremium')
            )

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('distance') is not None:
            data['distance'] = ctx.convert_decimal_number(
                data.get('distance')
            )


        return StopLossOrder(**data)


class TrailingStopLossOrder(BaseEntity):
    """
    A TrailingStopLossOrder is an order that is linked to an open Trade and
    created with a price distance. The price distance is used to calculate a
    trailing stop value for the order that is in the losing direction from the
    market price at the time of the order's creation. The trailing stop value
    will follow the market price as it moves in the winning direction, and the
    order will filled (closing the Trade) by the first price that is equal to
    or worse than the trailing stop value. A TrailingStopLossOrder cannot be
    used to open a new Position.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Trailing Stop Loss for Trade {tradeID} @ {trailingStopValue}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "TSL Order {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_TrailingStopLossOrder

    def __init__(self, **kwargs):
        """
        Create a new TrailingStopLossOrder instance
        """
        super(TrailingStopLossOrder, self).__init__()
 
        #
        # The Order's identifier, unique within the Order's Account.
        #
        self.id = kwargs.get("id")
 
        #
        # The time when the Order was created.
        #
        self.createTime = kwargs.get("createTime")
 
        #
        # The current state of the Order.
        #
        self.state = kwargs.get("state")
 
        #
        # The client extensions of the Order. Do not set, modify, or delete
        # clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The type of the Order. Always set to "TRAILING_STOP_LOSS" for
        # Trailing Stop Loss Orders.
        #
        self.type = kwargs.get("type", "TRAILING_STOP_LOSS")
 
        #
        # The ID of the Trade to close when the price threshold is breached.
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The client ID of the Trade to be closed when the price threshold is
        # breached.
        #
        self.clientTradeID = kwargs.get("clientTradeID")
 
        #
        # The price distance (in price units) specified for the
        # TrailingStopLoss Order.
        #
        self.distance = kwargs.get("distance")
 
        #
        # The time-in-force requested for the TrailingStopLoss Order.
        # Restricted to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date/time when the StopLoss Order will be cancelled if its
        # timeInForce is "GTD".
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # Specification of which price component should be used when
        # determining if an Order should be triggered and filled. This allows
        # Orders to be triggered based on the bid, ask, mid, default (ask for
        # buy, bid for sell) or inverse (ask for sell, bid for buy) price
        # depending on the desired behaviour. Orders are always filled using
        # their default price component. This feature is only provided through
        # the REST API. Clients who choose to specify a non-default trigger
        # condition will not see it reflected in any of OANDA's proprietary or
        # partner trading platforms, their transaction history or their account
        # statements. OANDA platforms always assume that an Order's trigger
        # condition is set to the default value when indicating the distance
        # from an Order's trigger price, and will always provide the default
        # trigger condition when creating or modifying an Order. A special
        # restriction applies when creating a guaranteed Stop Loss Order. In
        # this case the TriggerCondition value must either be "DEFAULT", or the
        # "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order
        # for a long trade valid values are "DEFAULT" and "BID", and for short
        # trades "DEFAULT" and "ASK" are valid.
        #
        self.triggerCondition = kwargs.get("triggerCondition", "DEFAULT")
 
        #
        # The trigger price for the Trailing Stop Loss Order. The trailing stop
        # value will trail (follow) the market price by the TSL order's
        # configured "distance" as the market price moves in the winning
        # direction. If the market price moves to a level that is equal to or
        # worse than the trailing stop value, the order will be filled and the
        # Trade will be closed.
        #
        self.trailingStopValue = kwargs.get("trailingStopValue")
 
        #
        # ID of the Transaction that filled this Order (only provided when the
        # Order's state is FILLED)
        #
        self.fillingTransactionID = kwargs.get("fillingTransactionID")
 
        #
        # Date/time when the Order was filled (only provided when the Order's
        # state is FILLED)
        #
        self.filledTime = kwargs.get("filledTime")
 
        #
        # Trade ID of Trade opened when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was opened as a result
        # of the fill)
        #
        self.tradeOpenedID = kwargs.get("tradeOpenedID")
 
        #
        # Trade ID of Trade reduced when the Order was filled (only provided
        # when the Order's state is FILLED and a Trade was reduced as a result
        # of the fill)
        #
        self.tradeReducedID = kwargs.get("tradeReducedID")
 
        #
        # Trade IDs of Trades closed when the Order was filled (only provided
        # when the Order's state is FILLED and one or more Trades were closed
        # as a result of the fill)
        #
        self.tradeClosedIDs = kwargs.get("tradeClosedIDs")
 
        #
        # ID of the Transaction that cancelled the Order (only provided when
        # the Order's state is CANCELLED)
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")
 
        #
        # Date/time when the Order was cancelled (only provided when the state
        # of the Order is CANCELLED)
        #
        self.cancelledTime = kwargs.get("cancelledTime")
 
        #
        # The ID of the Order that was replaced by this Order (only provided if
        # this Order was created as part of a cancel/replace).
        #
        self.replacesOrderID = kwargs.get("replacesOrderID")
 
        #
        # The ID of the Order that replaced this Order (only provided if this
        # Order was cancelled as part of a cancel/replace).
        #
        self.replacedByOrderID = kwargs.get("replacedByOrderID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TrailingStopLossOrder from a dict (generally from
        loading a JSON response). The data used to instantiate the
        TrailingStopLossOrder is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('distance') is not None:
            data['distance'] = ctx.convert_decimal_number(
                data.get('distance')
            )

        if data.get('trailingStopValue') is not None:
            data['trailingStopValue'] = ctx.convert_decimal_number(
                data.get('trailingStopValue')
            )


        return TrailingStopLossOrder(**data)


class OrderRequest(BaseEntity):
    """
    The base Order specification used when requesting that an Order be created.
    Each specific Order-type extends this definition.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = ""

    #
    # Format string used when generating a name for this object
    #
    _name_format = "OrderRequest"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_OrderRequest

    def __init__(self, **kwargs):
        """
        Create a new OrderRequest instance
        """
        super(OrderRequest, self).__init__()

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new OrderRequest from a dict (generally from loading a
        JSON response). The data used to instantiate the OrderRequest is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        return OrderRequest(**data)


class MarketOrderRequest(BaseEntity):
    """
    A MarketOrderRequest specifies the parameters that may be set when creating
    a Market Order.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "{units} units of {instrument}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Market Order Request"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_MarketOrderRequest

    def __init__(self, **kwargs):
        """
        Create a new MarketOrderRequest instance
        """
        super(MarketOrderRequest, self).__init__()
 
        #
        # The type of the Order to Create. Must be set to "MARKET" when
        # creating a Market Order.
        #
        self.type = kwargs.get("type", "MARKET")
 
        #
        # The Market Order's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The quantity requested to be filled by the Market Order. A posititive
        # number of units results in a long Order, and a negative number of
        # units results in a short Order.
        #
        self.units = kwargs.get("units")
 
        #
        # The time-in-force requested for the Market Order. Restricted to FOK
        # or IOC for a MarketOrder.
        #
        self.timeInForce = kwargs.get("timeInForce", "FOK")
 
        #
        # The worst price that the client is willing to have the Market Order
        # filled at.
        #
        self.priceBound = kwargs.get("priceBound")
 
        #
        # Specification of how Positions in the Account are modified when the
        # Order is filled.
        #
        self.positionFill = kwargs.get("positionFill", "DEFAULT")
 
        #
        # The client extensions to add to the Order. Do not set, modify, or
        # delete clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Take Profit, or when a Trade's
        # dependent Take Profit Order is modified directly through the Trade.
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # StopLossDetails specifies the details of a Stop Loss Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Stop Loss, or when a Trade's
        # dependent Stop Loss Order is modified directly through the Trade.
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an
        # Order is filled that opens a Trade requiring a Trailing Stop Loss, or
        # when a Trade's dependent Trailing Stop Loss Order is modified
        # directly through the Trade.
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarketOrderRequest from a dict (generally from
        loading a JSON response). The data used to instantiate the
        MarketOrderRequest is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('units') is not None:
            data['units'] = ctx.convert_decimal_number(
                data.get('units')
            )

        if data.get('priceBound') is not None:
            data['priceBound'] = ctx.convert_decimal_number(
                data.get('priceBound')
            )

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('takeProfitOnFill') is not None:
            data['takeProfitOnFill'] = \
                ctx.transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill'], ctx
                )

        if data.get('stopLossOnFill') is not None:
            data['stopLossOnFill'] = \
                ctx.transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill'], ctx
                )

        if data.get('trailingStopLossOnFill') is not None:
            data['trailingStopLossOnFill'] = \
                ctx.transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill'], ctx
                )

        if data.get('tradeClientExtensions') is not None:
            data['tradeClientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions'], ctx
                )

        return MarketOrderRequest(**data)


class LimitOrderRequest(BaseEntity):
    """
    A LimitOrderRequest specifies the parameters that may be set when creating
    a Limit Order.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "{units} units of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Limit Order Request"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_LimitOrderRequest

    def __init__(self, **kwargs):
        """
        Create a new LimitOrderRequest instance
        """
        super(LimitOrderRequest, self).__init__()
 
        #
        # The type of the Order to Create. Must be set to "LIMIT" when creating
        # a Market Order.
        #
        self.type = kwargs.get("type", "LIMIT")
 
        #
        # The Limit Order's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The quantity requested to be filled by the Limit Order. A posititive
        # number of units results in a long Order, and a negative number of
        # units results in a short Order.
        #
        self.units = kwargs.get("units")
 
        #
        # The price threshold specified for the Limit Order. The Limit Order
        # will only be filled by a market price that is equal to or better than
        # this price.
        #
        self.price = kwargs.get("price")
 
        #
        # The time-in-force requested for the Limit Order.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date/time when the Limit Order will be cancelled if its
        # timeInForce is "GTD".
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # Specification of how Positions in the Account are modified when the
        # Order is filled.
        #
        self.positionFill = kwargs.get("positionFill", "DEFAULT")
 
        #
        # Specification of which price component should be used when
        # determining if an Order should be triggered and filled. This allows
        # Orders to be triggered based on the bid, ask, mid, default (ask for
        # buy, bid for sell) or inverse (ask for sell, bid for buy) price
        # depending on the desired behaviour. Orders are always filled using
        # their default price component. This feature is only provided through
        # the REST API. Clients who choose to specify a non-default trigger
        # condition will not see it reflected in any of OANDA's proprietary or
        # partner trading platforms, their transaction history or their account
        # statements. OANDA platforms always assume that an Order's trigger
        # condition is set to the default value when indicating the distance
        # from an Order's trigger price, and will always provide the default
        # trigger condition when creating or modifying an Order. A special
        # restriction applies when creating a guaranteed Stop Loss Order. In
        # this case the TriggerCondition value must either be "DEFAULT", or the
        # "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order
        # for a long trade valid values are "DEFAULT" and "BID", and for short
        # trades "DEFAULT" and "ASK" are valid.
        #
        self.triggerCondition = kwargs.get("triggerCondition", "DEFAULT")
 
        #
        # The client extensions to add to the Order. Do not set, modify, or
        # delete clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Take Profit, or when a Trade's
        # dependent Take Profit Order is modified directly through the Trade.
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # StopLossDetails specifies the details of a Stop Loss Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Stop Loss, or when a Trade's
        # dependent Stop Loss Order is modified directly through the Trade.
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an
        # Order is filled that opens a Trade requiring a Trailing Stop Loss, or
        # when a Trade's dependent Trailing Stop Loss Order is modified
        # directly through the Trade.
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new LimitOrderRequest from a dict (generally from loading
        a JSON response). The data used to instantiate the LimitOrderRequest is
        a shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('units') is not None:
            data['units'] = ctx.convert_decimal_number(
                data.get('units')
            )

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('takeProfitOnFill') is not None:
            data['takeProfitOnFill'] = \
                ctx.transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill'], ctx
                )

        if data.get('stopLossOnFill') is not None:
            data['stopLossOnFill'] = \
                ctx.transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill'], ctx
                )

        if data.get('trailingStopLossOnFill') is not None:
            data['trailingStopLossOnFill'] = \
                ctx.transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill'], ctx
                )

        if data.get('tradeClientExtensions') is not None:
            data['tradeClientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions'], ctx
                )

        return LimitOrderRequest(**data)


class StopOrderRequest(BaseEntity):
    """
    A StopOrderRequest specifies the parameters that may be set when creating a
    Stop Order.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "{units} units of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Stop Order Request"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_StopOrderRequest

    def __init__(self, **kwargs):
        """
        Create a new StopOrderRequest instance
        """
        super(StopOrderRequest, self).__init__()
 
        #
        # The type of the Order to Create. Must be set to "STOP" when creating
        # a Stop Order.
        #
        self.type = kwargs.get("type", "STOP")
 
        #
        # The Stop Order's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The quantity requested to be filled by the Stop Order. A posititive
        # number of units results in a long Order, and a negative number of
        # units results in a short Order.
        #
        self.units = kwargs.get("units")
 
        #
        # The price threshold specified for the Stop Order. The Stop Order will
        # only be filled by a market price that is equal to or worse than this
        # price.
        #
        self.price = kwargs.get("price")
 
        #
        # The worst market price that may be used to fill this Stop Order. If
        # the market gaps and crosses through both the price and the
        # priceBound, the Stop Order will be cancelled instead of being filled.
        #
        self.priceBound = kwargs.get("priceBound")
 
        #
        # The time-in-force requested for the Stop Order.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date/time when the Stop Order will be cancelled if its
        # timeInForce is "GTD".
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # Specification of how Positions in the Account are modified when the
        # Order is filled.
        #
        self.positionFill = kwargs.get("positionFill", "DEFAULT")
 
        #
        # Specification of which price component should be used when
        # determining if an Order should be triggered and filled. This allows
        # Orders to be triggered based on the bid, ask, mid, default (ask for
        # buy, bid for sell) or inverse (ask for sell, bid for buy) price
        # depending on the desired behaviour. Orders are always filled using
        # their default price component. This feature is only provided through
        # the REST API. Clients who choose to specify a non-default trigger
        # condition will not see it reflected in any of OANDA's proprietary or
        # partner trading platforms, their transaction history or their account
        # statements. OANDA platforms always assume that an Order's trigger
        # condition is set to the default value when indicating the distance
        # from an Order's trigger price, and will always provide the default
        # trigger condition when creating or modifying an Order. A special
        # restriction applies when creating a guaranteed Stop Loss Order. In
        # this case the TriggerCondition value must either be "DEFAULT", or the
        # "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order
        # for a long trade valid values are "DEFAULT" and "BID", and for short
        # trades "DEFAULT" and "ASK" are valid.
        #
        self.triggerCondition = kwargs.get("triggerCondition", "DEFAULT")
 
        #
        # The client extensions to add to the Order. Do not set, modify, or
        # delete clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Take Profit, or when a Trade's
        # dependent Take Profit Order is modified directly through the Trade.
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # StopLossDetails specifies the details of a Stop Loss Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Stop Loss, or when a Trade's
        # dependent Stop Loss Order is modified directly through the Trade.
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an
        # Order is filled that opens a Trade requiring a Trailing Stop Loss, or
        # when a Trade's dependent Trailing Stop Loss Order is modified
        # directly through the Trade.
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new StopOrderRequest from a dict (generally from loading
        a JSON response). The data used to instantiate the StopOrderRequest is
        a shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('units') is not None:
            data['units'] = ctx.convert_decimal_number(
                data.get('units')
            )

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('priceBound') is not None:
            data['priceBound'] = ctx.convert_decimal_number(
                data.get('priceBound')
            )

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('takeProfitOnFill') is not None:
            data['takeProfitOnFill'] = \
                ctx.transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill'], ctx
                )

        if data.get('stopLossOnFill') is not None:
            data['stopLossOnFill'] = \
                ctx.transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill'], ctx
                )

        if data.get('trailingStopLossOnFill') is not None:
            data['trailingStopLossOnFill'] = \
                ctx.transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill'], ctx
                )

        if data.get('tradeClientExtensions') is not None:
            data['tradeClientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions'], ctx
                )

        return StopOrderRequest(**data)


class MarketIfTouchedOrderRequest(BaseEntity):
    """
    A MarketIfTouchedOrderRequest specifies the parameters that may be set when
    creating a Market-if-Touched Order.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "{units} units of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "MIT Order Request"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_MarketIfTouchedOrderRequest

    def __init__(self, **kwargs):
        """
        Create a new MarketIfTouchedOrderRequest instance
        """
        super(MarketIfTouchedOrderRequest, self).__init__()
 
        #
        # The type of the Order to Create. Must be set to "MARKET_IF_TOUCHED"
        # when creating a Market If Touched Order.
        #
        self.type = kwargs.get("type", "MARKET_IF_TOUCHED")
 
        #
        # The MarketIfTouched Order's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The quantity requested to be filled by the MarketIfTouched Order. A
        # posititive number of units results in a long Order, and a negative
        # number of units results in a short Order.
        #
        self.units = kwargs.get("units")
 
        #
        # The price threshold specified for the MarketIfTouched Order. The
        # MarketIfTouched Order will only be filled by a market price that
        # crosses this price from the direction of the market price at the time
        # when the Order was created (the initialMarketPrice). Depending on the
        # value of the Order's price and initialMarketPrice, the
        # MarketIfTouchedOrder will behave like a Limit or a Stop Order.
        #
        self.price = kwargs.get("price")
 
        #
        # The worst market price that may be used to fill this MarketIfTouched
        # Order.
        #
        self.priceBound = kwargs.get("priceBound")
 
        #
        # The time-in-force requested for the MarketIfTouched Order. Restricted
        # to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date/time when the MarketIfTouched Order will be cancelled if its
        # timeInForce is "GTD".
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # Specification of how Positions in the Account are modified when the
        # Order is filled.
        #
        self.positionFill = kwargs.get("positionFill", "DEFAULT")
 
        #
        # Specification of which price component should be used when
        # determining if an Order should be triggered and filled. This allows
        # Orders to be triggered based on the bid, ask, mid, default (ask for
        # buy, bid for sell) or inverse (ask for sell, bid for buy) price
        # depending on the desired behaviour. Orders are always filled using
        # their default price component. This feature is only provided through
        # the REST API. Clients who choose to specify a non-default trigger
        # condition will not see it reflected in any of OANDA's proprietary or
        # partner trading platforms, their transaction history or their account
        # statements. OANDA platforms always assume that an Order's trigger
        # condition is set to the default value when indicating the distance
        # from an Order's trigger price, and will always provide the default
        # trigger condition when creating or modifying an Order. A special
        # restriction applies when creating a guaranteed Stop Loss Order. In
        # this case the TriggerCondition value must either be "DEFAULT", or the
        # "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order
        # for a long trade valid values are "DEFAULT" and "BID", and for short
        # trades "DEFAULT" and "ASK" are valid.
        #
        self.triggerCondition = kwargs.get("triggerCondition", "DEFAULT")
 
        #
        # The client extensions to add to the Order. Do not set, modify, or
        # delete clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # TakeProfitDetails specifies the details of a Take Profit Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Take Profit, or when a Trade's
        # dependent Take Profit Order is modified directly through the Trade.
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # StopLossDetails specifies the details of a Stop Loss Order to be
        # created on behalf of a client. This may happen when an Order is
        # filled that opens a Trade requiring a Stop Loss, or when a Trade's
        # dependent Stop Loss Order is modified directly through the Trade.
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # TrailingStopLossDetails specifies the details of a Trailing Stop Loss
        # Order to be created on behalf of a client. This may happen when an
        # Order is filled that opens a Trade requiring a Trailing Stop Loss, or
        # when a Trade's dependent Trailing Stop Loss Order is modified
        # directly through the Trade.
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created). Do not set, modify, or delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarketIfTouchedOrderRequest from a dict (generally
        from loading a JSON response). The data used to instantiate the
        MarketIfTouchedOrderRequest is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('units') is not None:
            data['units'] = ctx.convert_decimal_number(
                data.get('units')
            )

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('priceBound') is not None:
            data['priceBound'] = ctx.convert_decimal_number(
                data.get('priceBound')
            )

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('takeProfitOnFill') is not None:
            data['takeProfitOnFill'] = \
                ctx.transaction.TakeProfitDetails.from_dict(
                    data['takeProfitOnFill'], ctx
                )

        if data.get('stopLossOnFill') is not None:
            data['stopLossOnFill'] = \
                ctx.transaction.StopLossDetails.from_dict(
                    data['stopLossOnFill'], ctx
                )

        if data.get('trailingStopLossOnFill') is not None:
            data['trailingStopLossOnFill'] = \
                ctx.transaction.TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill'], ctx
                )

        if data.get('tradeClientExtensions') is not None:
            data['tradeClientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensions'], ctx
                )

        return MarketIfTouchedOrderRequest(**data)


class TakeProfitOrderRequest(BaseEntity):
    """
    A TakeProfitOrderRequest specifies the parameters that may be set when
    creating a Take Profit Order. Only one of the price and distance fields may
    be specified.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Take Profit for Trade {tradeID} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "TP Order Request"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_TakeProfitOrderRequest

    def __init__(self, **kwargs):
        """
        Create a new TakeProfitOrderRequest instance
        """
        super(TakeProfitOrderRequest, self).__init__()
 
        #
        # The type of the Order to Create. Must be set to "TAKE_PROFIT" when
        # creating a Take Profit Order.
        #
        self.type = kwargs.get("type", "TAKE_PROFIT")
 
        #
        # The ID of the Trade to close when the price threshold is breached.
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The client ID of the Trade to be closed when the price threshold is
        # breached.
        #
        self.clientTradeID = kwargs.get("clientTradeID")
 
        #
        # The price threshold specified for the TakeProfit Order. The
        # associated Trade will be closed by a market price that is equal to or
        # better than this threshold.
        #
        self.price = kwargs.get("price")
 
        #
        # The time-in-force requested for the TakeProfit Order. Restricted to
        # "GTC", "GFD" and "GTD" for TakeProfit Orders.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date/time when the TakeProfit Order will be cancelled if its
        # timeInForce is "GTD".
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # Specification of which price component should be used when
        # determining if an Order should be triggered and filled. This allows
        # Orders to be triggered based on the bid, ask, mid, default (ask for
        # buy, bid for sell) or inverse (ask for sell, bid for buy) price
        # depending on the desired behaviour. Orders are always filled using
        # their default price component. This feature is only provided through
        # the REST API. Clients who choose to specify a non-default trigger
        # condition will not see it reflected in any of OANDA's proprietary or
        # partner trading platforms, their transaction history or their account
        # statements. OANDA platforms always assume that an Order's trigger
        # condition is set to the default value when indicating the distance
        # from an Order's trigger price, and will always provide the default
        # trigger condition when creating or modifying an Order. A special
        # restriction applies when creating a guaranteed Stop Loss Order. In
        # this case the TriggerCondition value must either be "DEFAULT", or the
        # "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order
        # for a long trade valid values are "DEFAULT" and "BID", and for short
        # trades "DEFAULT" and "ASK" are valid.
        #
        self.triggerCondition = kwargs.get("triggerCondition", "DEFAULT")
 
        #
        # The client extensions to add to the Order. Do not set, modify, or
        # delete clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TakeProfitOrderRequest from a dict (generally from
        loading a JSON response). The data used to instantiate the
        TakeProfitOrderRequest is a shallow copy of the dict passed in, with
        any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        return TakeProfitOrderRequest(**data)


class StopLossOrderRequest(BaseEntity):
    """
    A StopLossOrderRequest specifies the parameters that may be set when
    creating a Stop Loss Order. Only one of the price and distance fields may
    be specified.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Stop Loss for Trade {tradeID} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "SL Order Request"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_StopLossOrderRequest

    def __init__(self, **kwargs):
        """
        Create a new StopLossOrderRequest instance
        """
        super(StopLossOrderRequest, self).__init__()
 
        #
        # The type of the Order to Create. Must be set to "STOP_LOSS" when
        # creating a Stop Loss Order.
        #
        self.type = kwargs.get("type", "STOP_LOSS")
 
        #
        # The ID of the Trade to close when the price threshold is breached.
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The client ID of the Trade to be closed when the price threshold is
        # breached.
        #
        self.clientTradeID = kwargs.get("clientTradeID")
 
        #
        # The price threshold specified for the Stop Loss Order. If the
        # guaranteed flag is false, the associated Trade will be closed by a
        # market price that is equal to or worse than this threshold. If the
        # flag is true the associated Trade will be closed at this price.
        #
        self.price = kwargs.get("price")
 
        #
        # Specifies the distance (in price units) from the Account's current
        # price to use as the Stop Loss Order price. If the Trade is short the
        # Instrument's bid price is used, and for long Trades the ask is used.
        #
        self.distance = kwargs.get("distance")
 
        #
        # The time-in-force requested for the StopLoss Order. Restricted to
        # "GTC", "GFD" and "GTD" for StopLoss Orders.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date/time when the StopLoss Order will be cancelled if its
        # timeInForce is "GTD".
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # Specification of which price component should be used when
        # determining if an Order should be triggered and filled. This allows
        # Orders to be triggered based on the bid, ask, mid, default (ask for
        # buy, bid for sell) or inverse (ask for sell, bid for buy) price
        # depending on the desired behaviour. Orders are always filled using
        # their default price component. This feature is only provided through
        # the REST API. Clients who choose to specify a non-default trigger
        # condition will not see it reflected in any of OANDA's proprietary or
        # partner trading platforms, their transaction history or their account
        # statements. OANDA platforms always assume that an Order's trigger
        # condition is set to the default value when indicating the distance
        # from an Order's trigger price, and will always provide the default
        # trigger condition when creating or modifying an Order. A special
        # restriction applies when creating a guaranteed Stop Loss Order. In
        # this case the TriggerCondition value must either be "DEFAULT", or the
        # "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order
        # for a long trade valid values are "DEFAULT" and "BID", and for short
        # trades "DEFAULT" and "ASK" are valid.
        #
        self.triggerCondition = kwargs.get("triggerCondition", "DEFAULT")
 
        #
        # Flag indicating that the Stop Loss Order is guaranteed. The default
        # value depends on the GuaranteedStopLossOrderMode of the account, if
        # it is REQUIRED, the default will be true, for DISABLED or ENABLED the
        # default is false.
        #
        self.guaranteed = kwargs.get("guaranteed")
 
        #
        # The client extensions to add to the Order. Do not set, modify, or
        # delete clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new StopLossOrderRequest from a dict (generally from
        loading a JSON response). The data used to instantiate the
        StopLossOrderRequest is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('distance') is not None:
            data['distance'] = ctx.convert_decimal_number(
                data.get('distance')
            )

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        return StopLossOrderRequest(**data)


class TrailingStopLossOrderRequest(BaseEntity):
    """
    A TrailingStopLossOrderRequest specifies the parameters that may be set
    when creating a Trailing Stop Loss Order.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Trailing Stop Loss for Trade {tradeID} @ {trailingStopValue}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "TSL Order Request"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.order_TrailingStopLossOrderRequest

    def __init__(self, **kwargs):
        """
        Create a new TrailingStopLossOrderRequest instance
        """
        super(TrailingStopLossOrderRequest, self).__init__()
 
        #
        # The type of the Order to Create. Must be set to "TRAILING_STOP_LOSS"
        # when creating a Trailng Stop Loss Order.
        #
        self.type = kwargs.get("type", "TRAILING_STOP_LOSS")
 
        #
        # The ID of the Trade to close when the price threshold is breached.
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The client ID of the Trade to be closed when the price threshold is
        # breached.
        #
        self.clientTradeID = kwargs.get("clientTradeID")
 
        #
        # The price distance (in price units) specified for the
        # TrailingStopLoss Order.
        #
        self.distance = kwargs.get("distance")
 
        #
        # The time-in-force requested for the TrailingStopLoss Order.
        # Restricted to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date/time when the StopLoss Order will be cancelled if its
        # timeInForce is "GTD".
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # Specification of which price component should be used when
        # determining if an Order should be triggered and filled. This allows
        # Orders to be triggered based on the bid, ask, mid, default (ask for
        # buy, bid for sell) or inverse (ask for sell, bid for buy) price
        # depending on the desired behaviour. Orders are always filled using
        # their default price component. This feature is only provided through
        # the REST API. Clients who choose to specify a non-default trigger
        # condition will not see it reflected in any of OANDA's proprietary or
        # partner trading platforms, their transaction history or their account
        # statements. OANDA platforms always assume that an Order's trigger
        # condition is set to the default value when indicating the distance
        # from an Order's trigger price, and will always provide the default
        # trigger condition when creating or modifying an Order. A special
        # restriction applies when creating a guaranteed Stop Loss Order. In
        # this case the TriggerCondition value must either be "DEFAULT", or the
        # "natural" trigger side "DEFAULT" results in. So for a Stop Loss Order
        # for a long trade valid values are "DEFAULT" and "BID", and for short
        # trades "DEFAULT" and "ASK" are valid.
        #
        self.triggerCondition = kwargs.get("triggerCondition", "DEFAULT")
 
        #
        # The client extensions to add to the Order. Do not set, modify, or
        # delete clientExtensions if your account is associated with MT4.
        #
        self.clientExtensions = kwargs.get("clientExtensions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TrailingStopLossOrderRequest from a dict (generally
        from loading a JSON response). The data used to instantiate the
        TrailingStopLossOrderRequest is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('distance') is not None:
            data['distance'] = ctx.convert_decimal_number(
                data.get('distance')
            )

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        return TrailingStopLossOrderRequest(**data)


class UnitsAvailableDetails(BaseEntity):
    """
    Representation of many units of an Instrument are available to be traded
    for both long and short Orders.
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
    _properties = spec_properties.order_UnitsAvailableDetails

    def __init__(self, **kwargs):
        """
        Create a new UnitsAvailableDetails instance
        """
        super(UnitsAvailableDetails, self).__init__()
 
        #
        # The units available for long Orders.
        #
        self.long = kwargs.get("long")
 
        #
        # The units available for short Orders.
        #
        self.short = kwargs.get("short")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new UnitsAvailableDetails from a dict (generally from
        loading a JSON response). The data used to instantiate the
        UnitsAvailableDetails is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('long') is not None:
            data['long'] = ctx.convert_decimal_number(
                data.get('long')
            )

        if data.get('short') is not None:
            data['short'] = ctx.convert_decimal_number(
                data.get('short')
            )

        return UnitsAvailableDetails(**data)


class UnitsAvailable(BaseEntity):
    """
    Representation of how many units of an Instrument are available to be
    traded by an Order depending on its postionFill option.
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
    _properties = spec_properties.order_UnitsAvailable

    def __init__(self, **kwargs):
        """
        Create a new UnitsAvailable instance
        """
        super(UnitsAvailable, self).__init__()
 
        #
        # The number of units that are available to be traded using an Order
        # with a positionFill option of "DEFAULT". For an Account with hedging
        # enabled, this value will be the same as the "OPEN_ONLY" value. For an
        # Account without hedging enabled, this value will be the same as the
        # "REDUCE_FIRST" value.
        #
        self.default = kwargs.get("default")
 
        #
        # The number of units that may are available to be traded with an Order
        # with a positionFill option of "REDUCE_FIRST".
        #
        self.reduceFirst = kwargs.get("reduceFirst")
 
        #
        # The number of units that may are available to be traded with an Order
        # with a positionFill option of "REDUCE_ONLY".
        #
        self.reduceOnly = kwargs.get("reduceOnly")
 
        #
        # The number of units that may are available to be traded with an Order
        # with a positionFill option of "OPEN_ONLY".
        #
        self.openOnly = kwargs.get("openOnly")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new UnitsAvailable from a dict (generally from loading a
        JSON response). The data used to instantiate the UnitsAvailable is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('default') is not None:
            data['default'] = \
                ctx.order.UnitsAvailableDetails.from_dict(
                    data['default'], ctx
                )

        if data.get('reduceFirst') is not None:
            data['reduceFirst'] = \
                ctx.order.UnitsAvailableDetails.from_dict(
                    data['reduceFirst'], ctx
                )

        if data.get('reduceOnly') is not None:
            data['reduceOnly'] = \
                ctx.order.UnitsAvailableDetails.from_dict(
                    data['reduceOnly'], ctx
                )

        if data.get('openOnly') is not None:
            data['openOnly'] = \
                ctx.order.UnitsAvailableDetails.from_dict(
                    data['openOnly'], ctx
                )

        return UnitsAvailable(**data)


class GuaranteedStopLossOrderEntryData(BaseEntity):
    """
    Details required by clients creating a Guaranteed Stop Loss Order
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
    _properties = spec_properties.order_GuaranteedStopLossOrderEntryData

    def __init__(self, **kwargs):
        """
        Create a new GuaranteedStopLossOrderEntryData instance
        """
        super(GuaranteedStopLossOrderEntryData, self).__init__()
 
        #
        # The minimum distance allowed between the Trade's fill price and the
        # configured price for guaranteed Stop Loss Orders created for this
        # instrument. Specified in price units.
        #
        self.minimumDistance = kwargs.get("minimumDistance")
 
        #
        # The amount that is charged to the account if a guaranteed Stop Loss
        # Order is triggered and filled. The value is in price units and is
        # charged for each unit of the Trade.
        #
        self.premium = kwargs.get("premium")
 
        #
        # The guaranteed Stop Loss Order level restriction for this instrument.
        #
        self.levelRestriction = kwargs.get("levelRestriction")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new GuaranteedStopLossOrderEntryData from a dict
        (generally from loading a JSON response). The data used to instantiate
        the GuaranteedStopLossOrderEntryData is a shallow copy of the dict
        passed in, with any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('minimumDistance') is not None:
            data['minimumDistance'] = ctx.convert_decimal_number(
                data.get('minimumDistance')
            )

        if data.get('premium') is not None:
            data['premium'] = ctx.convert_decimal_number(
                data.get('premium')
            )

        if data.get('levelRestriction') is not None:
            data['levelRestriction'] = \
                ctx.primitives.GuaranteedStopLossOrderLevelRestriction.from_dict(
                    data['levelRestriction'], ctx
                )

        return GuaranteedStopLossOrderEntryData(**data)


class EntitySpec(object):
    """
    The order.EntitySpec wraps the order module's type definitions
    and API methods so they can be easily accessed through an instance of a v20
    Context.
    """

    OrderIdentifier = OrderIdentifier
    DynamicOrderState = DynamicOrderState
    Order = Order
    MarketOrder = MarketOrder
    FixedPriceOrder = FixedPriceOrder
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
    UnitsAvailableDetails = UnitsAvailableDetails
    UnitsAvailable = UnitsAvailable
    GuaranteedStopLossOrderEntryData = GuaranteedStopLossOrderEntryData

    def __init__(self, ctx):
        self.ctx = ctx


    def create(
        self,
        accountID,
        **kwargs
    ):
        """
        Create an Order for an Account

        Args:
            accountID:
                Account Identifier
            order:
                Specification of the Order to create

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        if 'order' in kwargs:
            body.set('order', kwargs['order'])

        request.set_body_dict(body.dict)

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
        if str(response.status) == "201":
            if jbody.get('orderCreateTransaction') is not None:
                parsed_body['orderCreateTransaction'] = \
                    self.ctx.transaction.Transaction.from_dict(
                        jbody['orderCreateTransaction'],
                        self.ctx
                    )

            if jbody.get('orderFillTransaction') is not None:
                parsed_body['orderFillTransaction'] = \
                    self.ctx.transaction.OrderFillTransaction.from_dict(
                        jbody['orderFillTransaction'],
                        self.ctx
                    )

            if jbody.get('orderCancelTransaction') is not None:
                parsed_body['orderCancelTransaction'] = \
                    self.ctx.transaction.OrderCancelTransaction.from_dict(
                        jbody['orderCancelTransaction'],
                        self.ctx
                    )

            if jbody.get('orderReissueTransaction') is not None:
                parsed_body['orderReissueTransaction'] = \
                    self.ctx.transaction.Transaction.from_dict(
                        jbody['orderReissueTransaction'],
                        self.ctx
                    )

            if jbody.get('orderReissueRejectTransaction') is not None:
                parsed_body['orderReissueRejectTransaction'] = \
                    self.ctx.transaction.Transaction.from_dict(
                        jbody['orderReissueRejectTransaction'],
                        self.ctx
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

        elif str(response.status) == "400":
            if jbody.get('orderRejectTransaction') is not None:
                parsed_body['orderRejectTransaction'] = \
                    self.ctx.transaction.Transaction.from_dict(
                        jbody['orderRejectTransaction'],
                        self.ctx
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

        elif str(response.status) == "401":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        elif str(response.status) == "403":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        elif str(response.status) == "404":
            if jbody.get('orderRejectTransaction') is not None:
                parsed_body['orderRejectTransaction'] = \
                    self.ctx.transaction.Transaction.from_dict(
                        jbody['orderRejectTransaction'],
                        self.ctx
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


    def list(
        self,
        accountID,
        **kwargs
    ):
        """
        Get a list of Orders for an Account

        Args:
            accountID:
                Account Identifier
            ids:
                List of Order IDs to retrieve
            state:
                The state to filter the requested Orders by
            instrument:
                The instrument to filter the requested orders by
            count:
                The maximum number of Orders to return
            beforeID:
                The maximum Order ID to return. If not provided the most recent
                Orders in the Account are returned

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('orders') is not None:
                parsed_body['orders'] = [
                    self.ctx.order.Order.from_dict(d, self.ctx)
                    for d in jbody.get('orders')
                ]

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

        elif str(response.status) == "400":
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


    def list_pending(
        self,
        accountID,
        **kwargs
    ):
        """
        List all pending Orders in an Account

        Args:
            accountID:
                Account Identifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('orders') is not None:
                parsed_body['orders'] = [
                    self.ctx.order.Order.from_dict(d, self.ctx)
                    for d in jbody.get('orders')
                ]

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

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
        orderSpecifier,
        **kwargs
    ):
        """
        Get details for a single Order in an Account

        Args:
            accountID:
                Account Identifier
            orderSpecifier:
                The Order Specifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/accounts/{accountID}/orders/{orderSpecifier}'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'orderSpecifier',
            orderSpecifier
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
            if jbody.get('order') is not None:
                parsed_body['order'] = \
                    self.ctx.order.Order.from_dict(
                        jbody['order'],
                        self.ctx
                    )

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

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


    def replace(
        self,
        accountID,
        orderSpecifier,
        **kwargs
    ):
        """
        Replace an Order in an Account by simultaneously cancelling it and
        creating a replacement Order

        Args:
            accountID:
                Account Identifier
            orderSpecifier:
                The Order Specifier
            order:
                Specification of the replacing Order

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'PUT',
            '/v3/accounts/{accountID}/orders/{orderSpecifier}'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'orderSpecifier',
            orderSpecifier
        )

        body = EntityDict()

        if 'order' in kwargs:
            body.set('order', kwargs['order'])

        request.set_body_dict(body.dict)

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
        if str(response.status) == "201":
            if jbody.get('orderCancelTransaction') is not None:
                parsed_body['orderCancelTransaction'] = \
                    self.ctx.transaction.OrderCancelTransaction.from_dict(
                        jbody['orderCancelTransaction'],
                        self.ctx
                    )

            if jbody.get('orderCreateTransaction') is not None:
                parsed_body['orderCreateTransaction'] = \
                    self.ctx.transaction.Transaction.from_dict(
                        jbody['orderCreateTransaction'],
                        self.ctx
                    )

            if jbody.get('orderFillTransaction') is not None:
                parsed_body['orderFillTransaction'] = \
                    self.ctx.transaction.OrderFillTransaction.from_dict(
                        jbody['orderFillTransaction'],
                        self.ctx
                    )

            if jbody.get('orderReissueTransaction') is not None:
                parsed_body['orderReissueTransaction'] = \
                    self.ctx.transaction.Transaction.from_dict(
                        jbody['orderReissueTransaction'],
                        self.ctx
                    )

            if jbody.get('orderReissueRejectTransaction') is not None:
                parsed_body['orderReissueRejectTransaction'] = \
                    self.ctx.transaction.Transaction.from_dict(
                        jbody['orderReissueRejectTransaction'],
                        self.ctx
                    )

            if jbody.get('replacingOrderCancelTransaction') is not None:
                parsed_body['replacingOrderCancelTransaction'] = \
                    self.ctx.transaction.OrderCancelTransaction.from_dict(
                        jbody['replacingOrderCancelTransaction'],
                        self.ctx
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

        elif str(response.status) == "400":
            if jbody.get('orderRejectTransaction') is not None:
                parsed_body['orderRejectTransaction'] = \
                    self.ctx.transaction.Transaction.from_dict(
                        jbody['orderRejectTransaction'],
                        self.ctx
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

        elif str(response.status) == "401":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        elif str(response.status) == "404":
            if jbody.get('orderCancelRejectTransaction') is not None:
                parsed_body['orderCancelRejectTransaction'] = \
                    self.ctx.transaction.Transaction.from_dict(
                        jbody['orderCancelRejectTransaction'],
                        self.ctx
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


    def cancel(
        self,
        accountID,
        orderSpecifier,
        **kwargs
    ):
        """
        Cancel a pending Order in an Account

        Args:
            accountID:
                Account Identifier
            orderSpecifier:
                The Order Specifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'PUT',
            '/v3/accounts/{accountID}/orders/{orderSpecifier}/cancel'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'orderSpecifier',
            orderSpecifier
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
            if jbody.get('orderCancelTransaction') is not None:
                parsed_body['orderCancelTransaction'] = \
                    self.ctx.transaction.OrderCancelTransaction.from_dict(
                        jbody['orderCancelTransaction'],
                        self.ctx
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

        elif str(response.status) == "401":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')

        elif str(response.status) == "404":
            if jbody.get('orderCancelRejectTransaction') is not None:
                parsed_body['orderCancelRejectTransaction'] = \
                    self.ctx.transaction.OrderCancelRejectTransaction.from_dict(
                        jbody['orderCancelRejectTransaction'],
                        self.ctx
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


    def set_client_extensions(
        self,
        accountID,
        orderSpecifier,
        **kwargs
    ):
        """
        Update the Client Extensions for an Order in an Account. Do not set,
        modify, or delete clientExtensions if your account is associated with
        MT4.

        Args:
            accountID:
                Account Identifier
            orderSpecifier:
                The Order Specifier
            clientExtensions:
                The Client Extensions to update for the Order. Do not set,
                modify, or delete clientExtensions if your account is
                associated with MT4.
            tradeClientExtensions:
                The Client Extensions to update for the Trade created when the
                Order is filled. Do not set, modify, or delete clientExtensions
                if your account is associated with MT4.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'PUT',
            '/v3/accounts/{accountID}/orders/{orderSpecifier}/clientExtensions'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'orderSpecifier',
            orderSpecifier
        )

        body = EntityDict()

        if 'clientExtensions' in kwargs:
            body.set('clientExtensions', kwargs['clientExtensions'])

        if 'tradeClientExtensions' in kwargs:
            body.set('tradeClientExtensions', kwargs['tradeClientExtensions'])

        request.set_body_dict(body.dict)

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
            if jbody.get('orderClientExtensionsModifyTransaction') is not None:
                parsed_body['orderClientExtensionsModifyTransaction'] = \
                    self.ctx.transaction.OrderClientExtensionsModifyTransaction.from_dict(
                        jbody['orderClientExtensionsModifyTransaction'],
                        self.ctx
                    )

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

        elif str(response.status) == "400":
            if jbody.get('orderClientExtensionsModifyRejectTransaction') is not None:
                parsed_body['orderClientExtensionsModifyRejectTransaction'] = \
                    self.ctx.transaction.OrderClientExtensionsModifyRejectTransaction.from_dict(
                        jbody['orderClientExtensionsModifyRejectTransaction'],
                        self.ctx
                    )

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

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
            if jbody.get('orderClientExtensionsModifyRejectTransaction') is not None:
                parsed_body['orderClientExtensionsModifyRejectTransaction'] = \
                    self.ctx.transaction.OrderClientExtensionsModifyRejectTransaction.from_dict(
                        jbody['orderClientExtensionsModifyRejectTransaction'],
                        self.ctx
                    )

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

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


    def market(self, accountID, **kwargs):
        """
        Shortcut to create a Market Order in an Account

        Args:
            accountID : The ID of the Account
            kwargs : The arguments to create a MarketOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.create(
            accountID,
            order=MarketOrderRequest(**kwargs)
        )


    def limit(self, accountID, **kwargs):
        """
        Shortcut to create a Limit Order in an Account

        Args:
            accountID : The ID of the Account
            kwargs : The arguments to create a LimitOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.create(
            accountID,
            order=LimitOrderRequest(**kwargs)
        )


    def limit_replace(self, accountID, orderID, **kwargs):
        """
        Shortcut to replace a pending Limit Order in an Account

        Args:
            accountID : The ID of the Account
            orderID : The ID of the Limit Order to replace
            kwargs : The arguments to create a LimitOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.replace(
            accountID,
            orderID,
            order=LimitOrderRequest(**kwargs)
        )


    def stop(self, accountID, **kwargs):
        """
        Shortcut to create a Stop Order in an Account

        Args:
            accountID : The ID of the Account
            kwargs : The arguments to create a StopOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.create(
            accountID,
            order=StopOrderRequest(**kwargs)
        )


    def stop_replace(self, accountID, orderID, **kwargs):
        """
        Shortcut to replace a pending Stop Order in an Account

        Args:
            accountID : The ID of the Account
            orderID : The ID of the Stop Order to replace
            kwargs : The arguments to create a StopOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.replace(
            accountID,
            orderID,
            order=StopOrderRequest(**kwargs)
        )


    def market_if_touched(self, accountID, **kwargs):
        """
        Shortcut to create a MarketIfTouched Order in an Account

        Args:
            accountID : The ID of the Account
            kwargs : The arguments to create a MarketIfTouchedOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.create(
            accountID,
            order=MarketIfTouchedOrderRequest(**kwargs)
        )


    def market_if_touched_replace(self, accountID, orderID, **kwargs):
        """
        Shortcut to replace a pending MarketIfTouched Order in an Account

        Args:
            accountID : The ID of the Account
            orderID : The ID of the MarketIfTouched Order to replace
            kwargs : The arguments to create a MarketIfTouchedOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.replace(
            accountID,
            orderID,
            order=MarketIfTouchedOrderRequest(**kwargs)
        )


    def take_profit(self, accountID, **kwargs):
        """
        Shortcut to create a Take Profit Order in an Account

        Args:
            accountID : The ID of the Account
            kwargs : The arguments to create a TakeProfitOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.create(
            accountID,
            order=TakeProfitOrderRequest(**kwargs)
        )


    def take_profit_replace(self, accountID, orderID, **kwargs):
        """
        Shortcut to replace a pending Take Profit Order in an Account

        Args:
            accountID : The ID of the Account
            orderID : The ID of the Take Profit Order to replace
            kwargs : The arguments to create a TakeProfitOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.replace(
            accountID,
            orderID,
            order=TakeProfitOrderRequest(**kwargs)
        )


    def stop_loss(self, accountID, **kwargs):
        """
        Shortcut to create a Stop Loss Order in an Account

        Args:
            accountID : The ID of the Account
            kwargs : The arguments to create a StopLossOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.create(
            accountID,
            order=StopLossOrderRequest(**kwargs)
        )


    def stop_loss_replace(self, accountID, orderID, **kwargs):
        """
        Shortcut to replace a pending Stop Loss Order in an Account

        Args:
            accountID : The ID of the Account
            orderID : The ID of the Stop Loss Order to replace
            kwargs : The arguments to create a StopLossOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.replace(
            accountID,
            orderID,
            order=StopLossOrderRequest(**kwargs)
        )


    def trailing_stop_loss(self, accountID, **kwargs):
        """
        Shortcut to create a Trailing Stop Loss Order in an Account

        Args:
            accountID : The ID of the Account
            kwargs : The arguments to create a TrailingStopLossOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.create(
            accountID,
            order=TrailingStopLossOrderRequest(**kwargs)
        )


    def trailing_stop_loss_replace(self, accountID, orderID, **kwargs):
        """
        Shortcut to replace a pending Trailing Stop Loss Order in an Account

        Args:
            accountID : The ID of the Account
            orderID : The ID of the Take Profit Order to replace
            kwargs : The arguments to create a TrailingStopLossOrderRequest

        Returns:
            v20.response.Response containing the results from submitting
            the request
        """
        return self.replace(
            accountID,
            orderID,
            order=TrailingStopLossOrderRequest(**kwargs)
        )
