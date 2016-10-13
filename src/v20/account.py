import json
from v20.base_entity import BaseEntity
from v20.base_entity import Property
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import trade
from v20 import position
from v20 import order
from v20 import transaction
from v20 import primitives



class Account(BaseEntity):
    _summary_format = "Account {id}"
    _name_format = ""

    _properties = [
        Property(
            "id",
            "Account ID",
            "The Account's identifier",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "alias",
            "Alias",
            "Client-assigned alias for the Account. Only provided if the Account has an alias set",
            "primitive",
            "string",
            False,
            None
        ),
        Property(
            "currency",
            "Home Currency",
            "The home currency of the Account",
            "primitive",
            "primitives.Currency",
            False,
            None
        ),
        Property(
            "balance",
            "Balance",
            "The current balance of the Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "createdByUserID",
            "Created by User ID",
            "ID of the user that created the Account.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "createdTime",
            "Create Time",
            "The date/time when the Account was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "pl",
            "Profit/Loss",
            "The total profit/loss realized over the lifetime of the Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "resettabledPL",
            "Resettable Profit/Loss",
            "The total realized profit/loss for the Account since it was last reset by the client. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "resettabledPLTime",
            "Profit/Loss Reset Time",
            "The date/time that the Account's resettablePL was last reset.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "marginRate",
            "Margin Rate",
            "Client-provided margin rate override for the Account. The effective margin rate of the Account is the lesser of this value and the OANDA margin rate for the Account's division. This value is only provided if a margin rate override exists for the Account.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "marginCallEnterTime",
            "Margin Call Enter Time",
            "The date/time when the Account entered a margin call state. Only provided if the Account is in a margin call.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "marginCallExtensionCount",
            "Margin Call Extension Count",
            "The number of times that the Account's current margin call was extended.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "lastMarginCallExtensionTime",
            "Last Margin Call Extension Time",
            "The date/time of the Account's last margin call extension.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "openTradeCount",
            "Open Trade Count",
            "The number of Trades currently open in the Account.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "openPositionCount",
            "Open Position Count",
            "The number of Positions currently open in the Account.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "pendingOrderCount",
            "Pending Order Count",
            "The number of Orders currently pending in the Account.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "hedgingEnabled",
            "Hedging Enabled",
            "Flag indicating that the Account has hedging enabled.",
            "primitive",
            "boolean",
            False,
            None
        ),
        Property(
            "unrealizedPL",
            "Unrealized Profit/Loss",
            "The total unrealized profit/loss for all Trades currently open in the Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "NAV",
            "Net Asset Value",
            "The net asset value of the Account. Equal to Account balance + unrealizedPL. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginUsed",
            "Margin Used",
            "Margin currently used for the Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginAvailable",
            "Margin Available",
            "Margin available for Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "positionValue",
            "Position Value",
            "The value of the Account's open positions represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCloseoutUnrealizedPL",
            "Closeout UPL",
            "The Account's margin closeout unrealized PL.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCloseoutNAV",
            "Closeout NAV",
            "The Account's margin closeout NAV.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCloseoutMarginUsed",
            "Closeout Margin Used",
            "The Account's margin closeout margin used.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCloseoutPercent",
            "Margin Closeout Percentage",
            "The Account's margin closeout percentage. When this value is 1.0 or above the Account is in a margin closeout situation.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "withdrawalLimit",
            "Withdrawal Limit",
            "The current WithdrawalLimit for the account which will be zero or a positive value indicating how much can be withdrawn from the account.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCallMarginUsed",
            "Margin Call Margin Used",
            "The Account's margin call margin used.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCallPercent",
            "Margin Call Percentage",
            "The Account's margin call percentage. When this value is 1.0 or above the Account is in a margin call situation.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "lastTransactionID",
            "Last Transaction ID",
            "The ID of the last Transaction created for the Account.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "trades",
            "Open Trades",
            "The details of the Trades currently open in the Account.",
            "array_object",
            "TradeSummary",
            False,
            None
        ),
        Property(
            "positions",
            "Positions",
            "The details all Account Positions.",
            "array_object",
            "Position",
            False,
            None
        ),
        Property(
            "orders",
            "Pending Orders",
            "The details of the Orders currently pending in the Account.",
            "array_object",
            "Order",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(Account, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('alias') is not None:
            body['alias'] = \
                data.get('alias')

        if data.get('currency') is not None:
            body['currency'] = \
                data.get('currency')

        if data.get('balance') is not None:
            body['balance'] = \
                data.get('balance')

        if data.get('createdByUserID') is not None:
            body['createdByUserID'] = \
                data.get('createdByUserID')

        if data.get('createdTime') is not None:
            body['createdTime'] = \
                data.get('createdTime')

        if data.get('pl') is not None:
            body['pl'] = \
                data.get('pl')

        if data.get('resettabledPL') is not None:
            body['resettabledPL'] = \
                data.get('resettabledPL')

        if data.get('resettabledPLTime') is not None:
            body['resettabledPLTime'] = \
                data.get('resettabledPLTime')

        if data.get('marginRate') is not None:
            body['marginRate'] = \
                data.get('marginRate')

        if data.get('marginCallEnterTime') is not None:
            body['marginCallEnterTime'] = \
                data.get('marginCallEnterTime')

        if data.get('marginCallExtensionCount') is not None:
            body['marginCallExtensionCount'] = \
                data.get('marginCallExtensionCount')

        if data.get('lastMarginCallExtensionTime') is not None:
            body['lastMarginCallExtensionTime'] = \
                data.get('lastMarginCallExtensionTime')

        if data.get('openTradeCount') is not None:
            body['openTradeCount'] = \
                data.get('openTradeCount')

        if data.get('openPositionCount') is not None:
            body['openPositionCount'] = \
                data.get('openPositionCount')

        if data.get('pendingOrderCount') is not None:
            body['pendingOrderCount'] = \
                data.get('pendingOrderCount')

        if data.get('hedgingEnabled') is not None:
            body['hedgingEnabled'] = \
                data.get('hedgingEnabled')

        if data.get('unrealizedPL') is not None:
            body['unrealizedPL'] = \
                data.get('unrealizedPL')

        if data.get('NAV') is not None:
            body['NAV'] = \
                data.get('NAV')

        if data.get('marginUsed') is not None:
            body['marginUsed'] = \
                data.get('marginUsed')

        if data.get('marginAvailable') is not None:
            body['marginAvailable'] = \
                data.get('marginAvailable')

        if data.get('positionValue') is not None:
            body['positionValue'] = \
                data.get('positionValue')

        if data.get('marginCloseoutUnrealizedPL') is not None:
            body['marginCloseoutUnrealizedPL'] = \
                data.get('marginCloseoutUnrealizedPL')

        if data.get('marginCloseoutNAV') is not None:
            body['marginCloseoutNAV'] = \
                data.get('marginCloseoutNAV')

        if data.get('marginCloseoutMarginUsed') is not None:
            body['marginCloseoutMarginUsed'] = \
                data.get('marginCloseoutMarginUsed')

        if data.get('marginCloseoutPercent') is not None:
            body['marginCloseoutPercent'] = \
                data.get('marginCloseoutPercent')

        if data.get('withdrawalLimit') is not None:
            body['withdrawalLimit'] = \
                data.get('withdrawalLimit')

        if data.get('marginCallMarginUsed') is not None:
            body['marginCallMarginUsed'] = \
                data.get('marginCallMarginUsed')

        if data.get('marginCallPercent') is not None:
            body['marginCallPercent'] = \
                data.get('marginCallPercent')

        if data.get('lastTransactionID') is not None:
            body['lastTransactionID'] = \
                data.get('lastTransactionID')

        if data.get('trades') is not None:
            body['trades'] = [
                trade.TradeSummary.from_dict(d)
                for d in data.get('trades')\
            ]

        if data.get('positions') is not None:
            body['positions'] = [
                position.Position.from_dict(d)
                for d in data.get('positions')\
            ]

        if data.get('orders') is not None:
            body['orders'] = [
                order.Order.from_dict(d)
                for d in data.get('orders')\
            ]

        self = Account(**body)

        return self


class AccountState(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "unrealizedPL",
            "Unrealized Profit/Loss",
            "The total unrealized profit/loss for all Trades currently open in the Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "NAV",
            "Net Asset Value",
            "The net asset value of the Account. Equal to Account balance + unrealizedPL. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginUsed",
            "Margin Used",
            "Margin currently used for the Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginAvailable",
            "Margin Available",
            "Margin available for Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "positionValue",
            "Position Value",
            "The value of the Account's open positions represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCloseoutUnrealizedPL",
            "Closeout UPL",
            "The Account's margin closeout unrealized PL.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCloseoutNAV",
            "Closeout NAV",
            "The Account's margin closeout NAV.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCloseoutMarginUsed",
            "Closeout Margin Used",
            "The Account's margin closeout margin used.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCloseoutPercent",
            "Margin Closeout Percentage",
            "The Account's margin closeout percentage. When this value is 1.0 or above the Account is in a margin closeout situation.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "withdrawalLimit",
            "Withdrawal Limit",
            "The current WithdrawalLimit for the account which will be zero or a positive value indicating how much can be withdrawn from the account.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCallMarginUsed",
            "Margin Call Margin Used",
            "The Account's margin call margin used.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCallPercent",
            "Margin Call Percentage",
            "The Account's margin call percentage. When this value is 1.0 or above the Account is in a margin call situation.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "orders",
            "Order States",
            "The price-dependent state of each pending Order in the Account.",
            "array_object",
            "DynamicOrderState",
            False,
            None
        ),
        Property(
            "trades",
            "Trade States",
            "The price-dependent state for each open Trade in the Account.",
            "array_object",
            "CalculatedTradeState",
            False,
            None
        ),
        Property(
            "positions",
            "Position States",
            "The price-dependent state for each open Position in the Account.",
            "array_object",
            "CalculatedPositionState",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(AccountState, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('unrealizedPL') is not None:
            body['unrealizedPL'] = \
                data.get('unrealizedPL')

        if data.get('NAV') is not None:
            body['NAV'] = \
                data.get('NAV')

        if data.get('marginUsed') is not None:
            body['marginUsed'] = \
                data.get('marginUsed')

        if data.get('marginAvailable') is not None:
            body['marginAvailable'] = \
                data.get('marginAvailable')

        if data.get('positionValue') is not None:
            body['positionValue'] = \
                data.get('positionValue')

        if data.get('marginCloseoutUnrealizedPL') is not None:
            body['marginCloseoutUnrealizedPL'] = \
                data.get('marginCloseoutUnrealizedPL')

        if data.get('marginCloseoutNAV') is not None:
            body['marginCloseoutNAV'] = \
                data.get('marginCloseoutNAV')

        if data.get('marginCloseoutMarginUsed') is not None:
            body['marginCloseoutMarginUsed'] = \
                data.get('marginCloseoutMarginUsed')

        if data.get('marginCloseoutPercent') is not None:
            body['marginCloseoutPercent'] = \
                data.get('marginCloseoutPercent')

        if data.get('withdrawalLimit') is not None:
            body['withdrawalLimit'] = \
                data.get('withdrawalLimit')

        if data.get('marginCallMarginUsed') is not None:
            body['marginCallMarginUsed'] = \
                data.get('marginCallMarginUsed')

        if data.get('marginCallPercent') is not None:
            body['marginCallPercent'] = \
                data.get('marginCallPercent')

        if data.get('orders') is not None:
            body['orders'] = [
                order.DynamicOrderState.from_dict(d)
                for d in data.get('orders')\
            ]

        if data.get('trades') is not None:
            body['trades'] = [
                trade.CalculatedTradeState.from_dict(d)
                for d in data.get('trades')\
            ]

        if data.get('positions') is not None:
            body['positions'] = [
                position.CalculatedPositionState.from_dict(d)
                for d in data.get('positions')\
            ]

        self = AccountState(**body)

        return self


class AccountProperties(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "id",
            "ID",
            "The Account's identifier",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "mt4AccountID",
            "MT4 Account ID",
            "The Account's associated MT4 Account ID. This field will not be present if the Account is not an MT4 account.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "tags",
            "Account Tags",
            "The Account's tags",
            "array_primitive",
            "string",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(AccountProperties, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('mt4AccountID') is not None:
            body['mt4AccountID'] = \
                data.get('mt4AccountID')

        if data.get('tags') is not None:
            body['tags'] = \
                data.get('tags')

        self = AccountProperties(**body)

        return self


class AccountSummary(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "id",
            "Account ID",
            "The Account's identifier",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "alias",
            "Alias",
            "Client-assigned alias for the Account. Only provided if the Account has an alias set",
            "primitive",
            "string",
            False,
            None
        ),
        Property(
            "currency",
            "Home Currency",
            "The home currency of the Account",
            "primitive",
            "primitives.Currency",
            False,
            None
        ),
        Property(
            "balance",
            "Balance",
            "The current balance of the Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "createdByUserID",
            "Created by User ID",
            "ID of the user that created the Account.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "createdTime",
            "Create Time",
            "The date/time when the Account was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "pl",
            "Profit/Loss",
            "The total profit/loss realized over the lifetime of the Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "resettabledPL",
            "Resettable Profit/Loss",
            "The total realized profit/loss for the Account since it was last reset by the client. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "resettabledPLTime",
            "Profit/Loss Reset Time",
            "The date/time that the Account's resettablePL was last reset.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "marginRate",
            "Margin Rate",
            "Client-provided margin rate override for the Account. The effective margin rate of the Account is the lesser of this value and the OANDA margin rate for the Account's division. This value is only provided if a margin rate override exists for the Account.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "marginCallEnterTime",
            "Margin Call Enter Time",
            "The date/time when the Account entered a margin call state. Only provided if the Account is in a margin call.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "marginCallExtensionCount",
            "Margin Call Extension Count",
            "The number of times that the Account's current margin call was extended.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "lastMarginCallExtensionTime",
            "Last Margin Call Extension Time",
            "The date/time of the Account's last margin call extension.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "openTradeCount",
            "Open Trade Count",
            "The number of Trades currently open in the Account.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "openPositionCount",
            "Open Position Count",
            "The number of Positions currently open in the Account.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "pendingOrderCount",
            "Pending Order Count",
            "The number of Orders currently pending in the Account.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "hedgingEnabled",
            "Hedging Enabled",
            "Flag indicating that the Account has hedging enabled.",
            "primitive",
            "boolean",
            False,
            None
        ),
        Property(
            "unrealizedPL",
            "Unrealized Profit/Loss",
            "The total unrealized profit/loss for all Trades currently open in the Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "NAV",
            "Net Asset Value",
            "The net asset value of the Account. Equal to Account balance + unrealizedPL. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginUsed",
            "Margin Used",
            "Margin currently used for the Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginAvailable",
            "Margin Available",
            "Margin available for Account. Represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "positionValue",
            "Position Value",
            "The value of the Account's open positions represented in the Account's home currency.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCloseoutUnrealizedPL",
            "Closeout UPL",
            "The Account's margin closeout unrealized PL.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCloseoutNAV",
            "Closeout NAV",
            "The Account's margin closeout NAV.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCloseoutMarginUsed",
            "Closeout Margin Used",
            "The Account's margin closeout margin used.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCloseoutPercent",
            "Margin Closeout Percentage",
            "The Account's margin closeout percentage. When this value is 1.0 or above the Account is in a margin closeout situation.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "withdrawalLimit",
            "Withdrawal Limit",
            "The current WithdrawalLimit for the account which will be zero or a positive value indicating how much can be withdrawn from the account.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCallMarginUsed",
            "Margin Call Margin Used",
            "The Account's margin call margin used.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "marginCallPercent",
            "Margin Call Percentage",
            "The Account's margin call percentage. When this value is 1.0 or above the Account is in a margin call situation.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "lastTransactionID",
            "Last Transaction ID",
            "The ID of the last Transaction created for the Account.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(AccountSummary, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('alias') is not None:
            body['alias'] = \
                data.get('alias')

        if data.get('currency') is not None:
            body['currency'] = \
                data.get('currency')

        if data.get('balance') is not None:
            body['balance'] = \
                data.get('balance')

        if data.get('createdByUserID') is not None:
            body['createdByUserID'] = \
                data.get('createdByUserID')

        if data.get('createdTime') is not None:
            body['createdTime'] = \
                data.get('createdTime')

        if data.get('pl') is not None:
            body['pl'] = \
                data.get('pl')

        if data.get('resettabledPL') is not None:
            body['resettabledPL'] = \
                data.get('resettabledPL')

        if data.get('resettabledPLTime') is not None:
            body['resettabledPLTime'] = \
                data.get('resettabledPLTime')

        if data.get('marginRate') is not None:
            body['marginRate'] = \
                data.get('marginRate')

        if data.get('marginCallEnterTime') is not None:
            body['marginCallEnterTime'] = \
                data.get('marginCallEnterTime')

        if data.get('marginCallExtensionCount') is not None:
            body['marginCallExtensionCount'] = \
                data.get('marginCallExtensionCount')

        if data.get('lastMarginCallExtensionTime') is not None:
            body['lastMarginCallExtensionTime'] = \
                data.get('lastMarginCallExtensionTime')

        if data.get('openTradeCount') is not None:
            body['openTradeCount'] = \
                data.get('openTradeCount')

        if data.get('openPositionCount') is not None:
            body['openPositionCount'] = \
                data.get('openPositionCount')

        if data.get('pendingOrderCount') is not None:
            body['pendingOrderCount'] = \
                data.get('pendingOrderCount')

        if data.get('hedgingEnabled') is not None:
            body['hedgingEnabled'] = \
                data.get('hedgingEnabled')

        if data.get('unrealizedPL') is not None:
            body['unrealizedPL'] = \
                data.get('unrealizedPL')

        if data.get('NAV') is not None:
            body['NAV'] = \
                data.get('NAV')

        if data.get('marginUsed') is not None:
            body['marginUsed'] = \
                data.get('marginUsed')

        if data.get('marginAvailable') is not None:
            body['marginAvailable'] = \
                data.get('marginAvailable')

        if data.get('positionValue') is not None:
            body['positionValue'] = \
                data.get('positionValue')

        if data.get('marginCloseoutUnrealizedPL') is not None:
            body['marginCloseoutUnrealizedPL'] = \
                data.get('marginCloseoutUnrealizedPL')

        if data.get('marginCloseoutNAV') is not None:
            body['marginCloseoutNAV'] = \
                data.get('marginCloseoutNAV')

        if data.get('marginCloseoutMarginUsed') is not None:
            body['marginCloseoutMarginUsed'] = \
                data.get('marginCloseoutMarginUsed')

        if data.get('marginCloseoutPercent') is not None:
            body['marginCloseoutPercent'] = \
                data.get('marginCloseoutPercent')

        if data.get('withdrawalLimit') is not None:
            body['withdrawalLimit'] = \
                data.get('withdrawalLimit')

        if data.get('marginCallMarginUsed') is not None:
            body['marginCallMarginUsed'] = \
                data.get('marginCallMarginUsed')

        if data.get('marginCallPercent') is not None:
            body['marginCallPercent'] = \
                data.get('marginCallPercent')

        if data.get('lastTransactionID') is not None:
            body['lastTransactionID'] = \
                data.get('lastTransactionID')

        self = AccountSummary(**body)

        return self


class AccountChanges(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "ordersCreated",
            "Orders Created",
            "The Orders created. These Orders may have been filled, cancelled or triggered in the same period.",
            "array_object",
            "Order",
            False,
            None
        ),
        Property(
            "ordersCancelled",
            "Orders Cancelled",
            "The Orders cancelled.",
            "array_object",
            "Order",
            False,
            None
        ),
        Property(
            "ordersFilled",
            "Orders Filled",
            "The Orders filled.",
            "array_object",
            "Order",
            False,
            None
        ),
        Property(
            "ordersTriggered",
            "Orders Triggered",
            "The Orders triggered.",
            "array_object",
            "Order",
            False,
            None
        ),
        Property(
            "tradesOpened",
            "Trades Opened",
            "The Trades opened.",
            "array_object",
            "Trade",
            False,
            None
        ),
        Property(
            "tradesReduced",
            "Trades Reduced",
            "The Trades reduced.",
            "array_object",
            "Trade",
            False,
            None
        ),
        Property(
            "tradesClosed",
            "Trades Closed",
            "The Trades closed.",
            "array_object",
            "Trade",
            False,
            None
        ),
        Property(
            "positions",
            "Positions",
            "The Positions changed.",
            "array_object",
            "Position",
            False,
            None
        ),
        Property(
            "transactions",
            "Transactions",
            "The Transactions that have been generated.",
            "array_object",
            "Transaction",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(AccountChanges, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('ordersCreated') is not None:
            body['ordersCreated'] = [
                order.Order.from_dict(d)
                for d in data.get('ordersCreated')\
            ]

        if data.get('ordersCancelled') is not None:
            body['ordersCancelled'] = [
                order.Order.from_dict(d)
                for d in data.get('ordersCancelled')\
            ]

        if data.get('ordersFilled') is not None:
            body['ordersFilled'] = [
                order.Order.from_dict(d)
                for d in data.get('ordersFilled')\
            ]

        if data.get('ordersTriggered') is not None:
            body['ordersTriggered'] = [
                order.Order.from_dict(d)
                for d in data.get('ordersTriggered')\
            ]

        if data.get('tradesOpened') is not None:
            body['tradesOpened'] = [
                trade.Trade.from_dict(d)
                for d in data.get('tradesOpened')\
            ]

        if data.get('tradesReduced') is not None:
            body['tradesReduced'] = [
                trade.Trade.from_dict(d)
                for d in data.get('tradesReduced')\
            ]

        if data.get('tradesClosed') is not None:
            body['tradesClosed'] = [
                trade.Trade.from_dict(d)
                for d in data.get('tradesClosed')\
            ]

        if data.get('positions') is not None:
            body['positions'] = [
                position.Position.from_dict(d)
                for d in data.get('positions')\
            ]

        if data.get('transactions') is not None:
            body['transactions'] = [
                transaction.Transaction.from_dict(d)
                for d in data.get('transactions')\
            ]

        self = AccountChanges(**body)

        return self

class EntitySpec(object):
    Account = Account
    AccountState = AccountState
    AccountProperties = AccountProperties
    AccountSummary = AccountSummary
    AccountChanges = AccountChanges

    def __init__(self, ctx):
        self.ctx = ctx


    def list(
        self,
        **kwargs
    ):
        """List Accounts

        Get a list of all Accounts authorized for the provided token.

        Parameters
        ----------
        """


        request = Request(
            'GET',
            '/v3/accounts'
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('accounts') is not None:
                parsed_body['accounts'] = [
                    AccountProperties.from_dict(d)
                    for d in jbody.get('accounts')
                ]


        if str(response.status) == "401":
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
        **kwargs
    ):
        """Account Details

        Get the full details for a single Account that a client has access to.
        Full pending Order, open Trade and open Position representations are
        provided.

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}'
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
            if jbody.get('account') is not None:
                parsed_body['account'] = \
                    Account.from_dict(
                        jbody['account']
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


    def summary(
        self,
        accountID,
        **kwargs
    ):
        """Account Summary

        Get a summary for a single Account that a client has access to.

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/summary'
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
            if jbody.get('account') is not None:
                parsed_body['account'] = \
                    AccountSummary.from_dict(
                        jbody['account']
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


    def instruments(
        self,
        accountID,
        **kwargs
    ):
        """Account Instruments

        Get the list of tradeable instruments for the given Account. The list
        of tradeable instruments is dependent on the regulatory division that
        the Account is located in, thus should be the same for all Accounts
        owned by a single user.

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch
        instruments : array, optional
            List of instruments to query specifically.
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/instruments'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_param(
            'instruments',
            kwargs.get('instruments')
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('instruments') is not None:
                parsed_body['instruments'] = [
                    primitives.Instrument.from_dict(d)
                    for d in jbody.get('instruments')\
                ]


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


    def configure(
        self,
        accountID,
        **kwargs
    ):
        """Configure Account

        Set the client-configurable portions of an Account.

        Parameters
        ----------
        accountID : 
            ID of the Account to configure
        alias : string, optional
            Client-defined alias (name) for the Account
        marginRate : None, optional
            The string representation of a decimal number.
        """


        request = Request(
            'PATCH',
            '/v3/accounts/{accountID}/configuration'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        body = EntityDict()

        body.set('alias', kwargs.get('alias'))

        body.set('marginRate', kwargs.get('marginRate'))

        request.set_body_dict(body.dict)

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('configureTransaction') is not None:
                parsed_body['configureTransaction'] = \
                    transaction.ClientConfigureTransaction.from_dict(
                        jbody['configureTransaction']
                    )

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


        if str(response.status) == "400":
            if jbody.get('configureRejectTransaction') is not None:
                parsed_body['configureRejectTransaction'] = \
                    transaction.ClientConfigureRejectTransaction.from_dict(
                        jbody['configureRejectTransaction']
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


    def changes(
        self,
        accountID,
        **kwargs
    ):
        """Poll Account Updates

        Endpoint used to poll an Account for its current state and changes
        since a specified TransactionID.

        Parameters
        ----------
        accountID : 
            ID of the Account to get changes for
        sinceTransactionID : , optional
            ID of the Transaction to get Account changes since.
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/changes'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_param(
            'sinceTransactionID',
            kwargs.get('sinceTransactionID')
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('changes') is not None:
                parsed_body['changes'] = \
                    AccountChanges.from_dict(
                        jbody['changes']
                    )

            if jbody.get('state') is not None:
                parsed_body['state'] = \
                    AccountState.from_dict(
                        jbody['state']
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


        if str(response.status) == "416":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')


        response.body = parsed_body

        return response

