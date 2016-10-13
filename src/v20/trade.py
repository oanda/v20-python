import json
from v20.base_entity import BaseEntity
from v20.base_entity import Property
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import transaction
from v20 import order



class Trade(BaseEntity):
    _summary_format = "{initialUnits} of {instrument} @ {price}"
    _name_format = "Trade {id}"

    _properties = [
        Property(
            "id",
            "Trade ID",
            "The Trade's identifier, unique within the Trade's Account.",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "instrument",
            "Instrument",
            "The Trade's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            False,
            None
        ),
        Property(
            "price",
            "Fill Price",
            "The execution price of the Trade.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "openTime",
            "Open Time",
            "The date/time when the Trade was opened.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "state",
            "State",
            "The current state of the Trade.",
            "primitive",
            "trade.TradeState",
            False,
            None
        ),
        Property(
            "initialUnits",
            "Initial Trade Units",
            "The initial size of the Trade. Negative values indicate a short Trade, and positive values indicate a long Trade.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "currentUnits",
            "Current Open Trade Units",
            "The number of units currently open for the Trade. This value is reduced to 0.0 as the Trade is closed.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "realizedPL",
            "Realized Profit/Loss",
            "The total profit/loss realized on the closed portion of the Trade.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "unrealizedPL",
            "Unrealized Profit/Loss",
            "The unrealized profit/loss on the open portion of the Trade.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "closingTransactionIDs",
            "Closing Transaction IDs",
            "The IDs of the Transactions that have closed portions of this Trade.",
            "array_primitive",
            "TransactionID",
            False,
            None
        ),
        Property(
            "financing",
            "Financing",
            "The financing paid/collected for this Trade.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "closeTime",
            "Close Time",
            "The date/time when the Trade was fully closed. Only provided for Trades whose state is CLOSED.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions of the Trade.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOrder",
            "Take Profit Order",
            "Full representation of the Trade's Take Profit Order, only provided if such an Order exists.",
            "object",
            "order.TakeProfitOrder",
            False,
            None
        ),
        Property(
            "stopLossOrder",
            "Stop Loss Order",
            "Full representation of the Trade's Stop Loss Order, only provided if such an Order exists.",
            "object",
            "order.StopLossOrder",
            False,
            None
        ),
        Property(
            "trailingStopLossOrder",
            "Trailing Stop Loss Order",
            "Full representation of the Trade's Trailing Stop Loss Order, only provided if such an Order exists.",
            "object",
            "order.TrailingStopLossOrder",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(Trade, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('openTime') is not None:
            body['openTime'] = \
                data.get('openTime')

        if data.get('state') is not None:
            body['state'] = \
                data.get('state')

        if data.get('initialUnits') is not None:
            body['initialUnits'] = \
                data.get('initialUnits')

        if data.get('currentUnits') is not None:
            body['currentUnits'] = \
                data.get('currentUnits')

        if data.get('realizedPL') is not None:
            body['realizedPL'] = \
                data.get('realizedPL')

        if data.get('unrealizedPL') is not None:
            body['unrealizedPL'] = \
                data.get('unrealizedPL')

        if data.get('closingTransactionIDs') is not None:
            body['closingTransactionIDs'] = \
                data.get('closingTransactionIDs')

        if data.get('financing') is not None:
            body['financing'] = \
                data.get('financing')

        if data.get('closeTime') is not None:
            body['closeTime'] = \
                data.get('closeTime')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOrder') is not None:
            body['takeProfitOrder'] = \
                order.TakeProfitOrder.from_dict(
                    data['takeProfitOrder']
                )

        if data.get('stopLossOrder') is not None:
            body['stopLossOrder'] = \
                order.StopLossOrder.from_dict(
                    data['stopLossOrder']
                )

        if data.get('trailingStopLossOrder') is not None:
            body['trailingStopLossOrder'] = \
                order.TrailingStopLossOrder.from_dict(
                    data['trailingStopLossOrder']
                )

        self = Trade(**body)

        return self


class TradeSummary(BaseEntity):
    _summary_format = "{initialUnits} of {instrument} @ {price}"
    _name_format = "Trade {id}"

    _properties = [
        Property(
            "id",
            "Trade ID",
            "The Trade's identifier, unique within the Trade's Account.",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "instrument",
            "Instrument",
            "The Trade's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            False,
            None
        ),
        Property(
            "price",
            "Fill Price",
            "The execution price of the Trade.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "openTime",
            "Open Time",
            "The date/time when the Trade was opened.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "state",
            "State",
            "The current state of the Trade.",
            "primitive",
            "trade.TradeState",
            False,
            None
        ),
        Property(
            "initialUnits",
            "Initial Trade Units",
            "The initial size of the Trade. Negative values indicate a short Trade, and positive values indicate a long Trade.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "currentUnits",
            "Current Open Trade Units",
            "The number of units currently open for the Trade. This value is reduced to 0.0 as the Trade is closed.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "realizedPL",
            "Realized Profit/Loss",
            "The total profit/loss realized on the closed portion of the Trade.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "unrealizedPL",
            "Unrealized Profit/Loss",
            "The unrealized profit/loss on the open portion of the Trade.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "closingTransactionIDs",
            "Closing Transaction IDs",
            "The IDs of the Transactions that have closed portions of this Trade.",
            "array_primitive",
            "TransactionID",
            False,
            None
        ),
        Property(
            "financing",
            "Financing",
            "The financing paid/collected for this Trade.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "closeTime",
            "Close Time",
            "The date/time when the Trade was fully closed. Only provided for Trades whose state is CLOSED.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions of the Trade.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOrderID",
            "Take Profit Order ID",
            "ID of the Trade's Take Profit Order, only provided if such an Order exists.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "stopLossOrderID",
            "Stop Loss Order ID",
            "ID of the Trade's Stop Loss Order, only provided if such an Order exists.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "trailingStopLossOrderID",
            "Trailing Stop Loss Order ID",
            "ID of the Trade's Trailing Stop Loss Order, only provided if such an Order exists.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TradeSummary, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('openTime') is not None:
            body['openTime'] = \
                data.get('openTime')

        if data.get('state') is not None:
            body['state'] = \
                data.get('state')

        if data.get('initialUnits') is not None:
            body['initialUnits'] = \
                data.get('initialUnits')

        if data.get('currentUnits') is not None:
            body['currentUnits'] = \
                data.get('currentUnits')

        if data.get('realizedPL') is not None:
            body['realizedPL'] = \
                data.get('realizedPL')

        if data.get('unrealizedPL') is not None:
            body['unrealizedPL'] = \
                data.get('unrealizedPL')

        if data.get('closingTransactionIDs') is not None:
            body['closingTransactionIDs'] = \
                data.get('closingTransactionIDs')

        if data.get('financing') is not None:
            body['financing'] = \
                data.get('financing')

        if data.get('closeTime') is not None:
            body['closeTime'] = \
                data.get('closeTime')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                transaction.ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOrderID') is not None:
            body['takeProfitOrderID'] = \
                data.get('takeProfitOrderID')

        if data.get('stopLossOrderID') is not None:
            body['stopLossOrderID'] = \
                data.get('stopLossOrderID')

        if data.get('trailingStopLossOrderID') is not None:
            body['trailingStopLossOrderID'] = \
                data.get('trailingStopLossOrderID')

        self = TradeSummary(**body)

        return self


class CalculatedTradeState(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "id",
            "Trade ID",
            "The Trade's ID.",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "unrealizedPL",
            "Trade UPL",
            "The Trade's unrealized profit/loss.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(CalculatedTradeState, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('unrealizedPL') is not None:
            body['unrealizedPL'] = \
                data.get('unrealizedPL')

        self = CalculatedTradeState(**body)

        return self

class EntitySpec(object):
    Trade = Trade
    TradeSummary = TradeSummary
    CalculatedTradeState = CalculatedTradeState

    def __init__(self, ctx):
        self.ctx = ctx


    def list(
        self,
        accountID,
        **kwargs
    ):
        """List Trades

        Get a list of Trades for an Account

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch Trades for.
        ids : array, optional
            List of Trade IDs to retrieve.
        state : , optional
            The state to filter the requested Trades by.
        instrument : , optional
            The instrument to filter the requested Trades by.
        count : integer, optional
            The maximum number of Trades to return.
        beforeID : , optional
            The maximum Trade ID to return. If not provided the most recent
            Trades in the Account are returned.
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/trades'
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
            if jbody.get('trades') is not None:
                parsed_body['trades'] = [
                    Trade.from_dict(d)
                    for d in jbody.get('trades')
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


    def list_open(
        self,
        accountID,
        **kwargs
    ):
        """List Open Trades

        Get the list of open Trades for an Account

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch Trades for.
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/openTrades'
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
            if jbody.get('trades') is not None:
                parsed_body['trades'] = [
                    Trade.from_dict(d)
                    for d in jbody.get('trades')
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
        tradeID,
        **kwargs
    ):
        """Trade Details

        Get the details of a specific Trade in an Account

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch Trades for.
        tradeID : 
            ID of the Trade to fetch
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/trades/{tradeID}'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'tradeID',
            tradeID
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('trade') is not None:
                parsed_body['trade'] = \
                    Trade.from_dict(
                        jbody['trade']
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


    def close(
        self,
        accountID,
        tradeID,
        **kwargs
    ):
        """Close Trade

        Close (partially or fully) a specific open Trade in an Account

        Parameters
        ----------
        accountID : 
            ID of the Account to close a Trade in.
        tradeID : 
            ID of the Trade to close.
        units : string, optional
            Indication of how much of the Trade to close. Either the string
            "ALL" (indicating that all of the Trade should be closed), or a
            DecimalNumber representing the number of units of the open Trade to
            Close using a TradeClose MarketOrder. The units specified must
            always be positive, and the magnitude of the value cannot exceed
            the magnitude of the Trade's open units.
        """


        request = Request(
            'PUT',
            '/v3/accounts/{accountID}/trades/{tradeID}/close'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'tradeID',
            tradeID
        )

        body = EntityDict()

        body.set('units', kwargs.get('units'))

        request.set_body_dict(body.dict)

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('orderCreateTransaction') is not None:
                parsed_body['orderCreateTransaction'] = \
                    transaction.MarketOrderTransaction.from_dict(
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

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


        if str(response.status) == "400":
            if jbody.get('orderRejectTransaction') is not None:
                parsed_body['orderRejectTransaction'] = \
                    transaction.MarketOrderRejectTransaction.from_dict(
                        jbody['orderRejectTransaction']
                    )

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
            if jbody.get('orderRejectTransaction') is not None:
                parsed_body['orderRejectTransaction'] = \
                    transaction.MarketOrderRejectTransaction.from_dict(
                        jbody['orderRejectTransaction']
                    )

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
        tradeID,
        **kwargs
    ):
        """Set Trade Client Extensions

        Update the Client Extensions for a Trade. Do not add, update, or delete
        the Client Extensions if your account is associated with MT4.

        Parameters
        ----------
        accountID : 
            ID of the Account.
        tradeID : 
            ID of the Trade to update the Client Extension of.
        clientExtensions : None, optional
            The Client Extensions to update the Trade with. Do not add, update,
            or delete the Client Extensions if your account is associated with
            MT4.
        """


        request = Request(
            'PUT',
            '/v3/accounts/{accountID}/trades/{tradeID}/clientExtensions'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'tradeID',
            tradeID
        )

        body = EntityDict()

        body.set('clientExtensions', kwargs.get('clientExtensions'))

        request.set_body_dict(body.dict)

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('tradeClientExtensionsModifyTransaction') is not None:
                parsed_body['tradeClientExtensionsModifyTransaction'] = \
                    transaction.TradeClientExtensionsModifyTransaction.from_dict(
                        jbody['tradeClientExtensionsModifyTransaction']
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


        if str(response.status) == "400":
            if jbody.get('tradeClientExtensionsModifyRejectTransaction') is not None:
                parsed_body['tradeClientExtensionsModifyRejectTransaction'] = \
                    transaction.TradeClientExtensionsModifyRejectTransaction.from_dict(
                        jbody['tradeClientExtensionsModifyRejectTransaction']
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


    def set_dependent_orders(
        self,
        accountID,
        tradeID,
        **kwargs
    ):
        """Set Dependent Orders

        Create, replace and cancel a Trade's dependent Orders (Take Profit,
        Stop Loss and Trailing Stop Loss) through the Trade itself

        Parameters
        ----------
        accountID : 
            ID of the Account.
        tradeID : 
            ID of the Trade to modify the dependent Orders of.
        takeProfit : None, optional
            The specification of the Take Profit to create/modify/cancel. If
            takeProfit is set to null, the Take Profit Order will be cancelled
            if it exists. If takeProfit is not provided, the exisiting Take
            Profit Order will not be modified. If a sub-field of takeProfit is
            not specified, that field will be set to a default value on create,
            and be inherited by the replacing order on modify.
        stopLoss : None, optional
            The specification of the Stop Loss to create/modify/cancel. If
            stopLoss is set to null, the Stop Loss Order will be cancelled if
            it exists. If stopLoss is not provided, the exisiting Stop Loss
            Order will not be modified. If a sub-field of stopLoss is not
            specified, that field will be set to a default value on create, and
            be inherited by the replacing order on modify.
        trailingStopLoss : None, optional
            The specification of the Trailing Stop Loss to
            create/modify/cancel. If trailingStopLoss is set to null, the
            Trailing Stop Loss Order will be cancelled if it exists. If
            trailingStopLoss is not provided, the exisiting Trailing Stop Loss
            Order will not be modified. If a sub-field of trailngStopLoss is
            not specified, that field will be set to a default value on create,
            and be inherited by the replacing order on modify.
        """


        request = Request(
            'PUT',
            '/v3/accounts/{accountID}/trades/{tradeID}/orders'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'tradeID',
            tradeID
        )

        body = EntityDict()

        body.set('takeProfit', kwargs.get('takeProfit'))

        body.set('stopLoss', kwargs.get('stopLoss'))

        body.set('trailingStopLoss', kwargs.get('trailingStopLoss'))

        request.set_body_dict(body.dict)

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('takeProfitOrderCancelTransaction') is not None:
                parsed_body['takeProfitOrderCancelTransaction'] = \
                    transaction.OrderCancelTransaction.from_dict(
                        jbody['takeProfitOrderCancelTransaction']
                    )

            if jbody.get('takeProfitOrderTransaction') is not None:
                parsed_body['takeProfitOrderTransaction'] = \
                    transaction.TakeProfitOrderTransaction.from_dict(
                        jbody['takeProfitOrderTransaction']
                    )

            if jbody.get('takeProfitOrderFillTransaction') is not None:
                parsed_body['takeProfitOrderFillTransaction'] = \
                    transaction.OrderFillTransaction.from_dict(
                        jbody['takeProfitOrderFillTransaction']
                    )

            if jbody.get('takeProfitOrderCreatedCancelTransaction') is not None:
                parsed_body['takeProfitOrderCreatedCancelTransaction'] = \
                    transaction.OrderCancelTransaction.from_dict(
                        jbody['takeProfitOrderCreatedCancelTransaction']
                    )

            if jbody.get('stopLossOrderCancelTransaction') is not None:
                parsed_body['stopLossOrderCancelTransaction'] = \
                    transaction.OrderCancelTransaction.from_dict(
                        jbody['stopLossOrderCancelTransaction']
                    )

            if jbody.get('stopLossOrderTransaction') is not None:
                parsed_body['stopLossOrderTransaction'] = \
                    transaction.StopLossOrderTransaction.from_dict(
                        jbody['stopLossOrderTransaction']
                    )

            if jbody.get('stopLossOrderFillTransaction') is not None:
                parsed_body['stopLossOrderFillTransaction'] = \
                    transaction.OrderFillTransaction.from_dict(
                        jbody['stopLossOrderFillTransaction']
                    )

            if jbody.get('stopLossOrderCreatedCancelTransaction') is not None:
                parsed_body['stopLossOrderCreatedCancelTransaction'] = \
                    transaction.OrderCancelTransaction.from_dict(
                        jbody['stopLossOrderCreatedCancelTransaction']
                    )

            if jbody.get('trailingStopLossOrderCancelTransaction') is not None:
                parsed_body['trailingStopLossOrderCancelTransaction'] = \
                    transaction.OrderCancelTransaction.from_dict(
                        jbody['trailingStopLossOrderCancelTransaction']
                    )

            if jbody.get('trailingStopLossOrderTransaction') is not None:
                parsed_body['trailingStopLossOrderTransaction'] = \
                    transaction.TrailingStopLossOrderTransaction.from_dict(
                        jbody['trailingStopLossOrderTransaction']
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


        if str(response.status) == "400":
            if jbody.get('takeProfitOrderCancelRejectTransaction') is not None:
                parsed_body['takeProfitOrderCancelRejectTransaction'] = \
                    transaction.OrderCancelRejectTransaction.from_dict(
                        jbody['takeProfitOrderCancelRejectTransaction']
                    )

            if jbody.get('takeProfitOrderRejectTransaction') is not None:
                parsed_body['takeProfitOrderRejectTransaction'] = \
                    transaction.TakeProfitOrderRejectTransaction.from_dict(
                        jbody['takeProfitOrderRejectTransaction']
                    )

            if jbody.get('stopLossOrderCancelRejectTransaction') is not None:
                parsed_body['stopLossOrderCancelRejectTransaction'] = \
                    transaction.OrderCancelRejectTransaction.from_dict(
                        jbody['stopLossOrderCancelRejectTransaction']
                    )

            if jbody.get('stopLossOrderRejectTransaction') is not None:
                parsed_body['stopLossOrderRejectTransaction'] = \
                    transaction.StopLossOrderRejectTransaction.from_dict(
                        jbody['stopLossOrderRejectTransaction']
                    )

            if jbody.get('trailingStopLossOrderCancelRejectTransaction') is not None:
                parsed_body['trailingStopLossOrderCancelRejectTransaction'] = \
                    transaction.OrderCancelRejectTransaction.from_dict(
                        jbody['trailingStopLossOrderCancelRejectTransaction']
                    )

            if jbody.get('trailingStopLossOrderRejectTransaction') is not None:
                parsed_body['trailingStopLossOrderRejectTransaction'] = \
                    transaction.TrailingStopLossOrderRejectTransaction.from_dict(
                        jbody['trailingStopLossOrderRejectTransaction']
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

