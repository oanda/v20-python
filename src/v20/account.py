import ujson as json
from v20.base_entity import BaseEntity
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import spec_properties



class Account(BaseEntity):
    """
    The full details of a client's Account. This includes full open Trade, open
    Position and pending Order representation.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Account {id}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = ""

    #
    # Property metadata for this object
    #
    _properties = spec_properties.account_Account

    def __init__(self, **kwargs):
        """
        Create a new Account instance
        """
        super(Account, self).__init__()
 
        #
        # The Account's identifier
        #
        self.id = kwargs.get("id")
 
        #
        # Client-assigned alias for the Account. Only provided if the Account
        # has an alias set
        #
        self.alias = kwargs.get("alias")
 
        #
        # The home currency of the Account
        #
        self.currency = kwargs.get("currency")
 
        #
        # The current balance of the Account.
        #
        self.balance = kwargs.get("balance")
 
        #
        # ID of the user that created the Account.
        #
        self.createdByUserID = kwargs.get("createdByUserID")
 
        #
        # The date/time when the Account was created.
        #
        self.createdTime = kwargs.get("createdTime")
 
        #
        # The current guaranteed Stop Loss Order mode of the Account.
        #
        self.guaranteedStopLossOrderMode = kwargs.get("guaranteedStopLossOrderMode")
 
        #
        # The total profit/loss realized over the lifetime of the Account.
        #
        self.pl = kwargs.get("pl")
 
        #
        # The total realized profit/loss for the Account since it was last
        # reset by the client.
        #
        self.resettablePL = kwargs.get("resettablePL")
 
        #
        # The date/time that the Account's resettablePL was last reset.
        #
        self.resettablePLTime = kwargs.get("resettablePLTime")
 
        #
        # The total amount of financing paid/collected over the lifetime of the
        # Account.
        #
        self.financing = kwargs.get("financing")
 
        #
        # The total amount of commission paid over the lifetime of the Account.
        #
        self.commission = kwargs.get("commission")
 
        #
        # The total amount of fees charged over the lifetime of the Account for
        # the execution of guaranteed Stop Loss Orders.
        #
        self.guaranteedExecutionFees = kwargs.get("guaranteedExecutionFees")
 
        #
        # Client-provided margin rate override for the Account. The effective
        # margin rate of the Account is the lesser of this value and the OANDA
        # margin rate for the Account's division. This value is only provided
        # if a margin rate override exists for the Account.
        #
        self.marginRate = kwargs.get("marginRate")
 
        #
        # The date/time when the Account entered a margin call state. Only
        # provided if the Account is in a margin call.
        #
        self.marginCallEnterTime = kwargs.get("marginCallEnterTime")
 
        #
        # The number of times that the Account's current margin call was
        # extended.
        #
        self.marginCallExtensionCount = kwargs.get("marginCallExtensionCount")
 
        #
        # The date/time of the Account's last margin call extension.
        #
        self.lastMarginCallExtensionTime = kwargs.get("lastMarginCallExtensionTime")
 
        #
        # The number of Trades currently open in the Account.
        #
        self.openTradeCount = kwargs.get("openTradeCount")
 
        #
        # The number of Positions currently open in the Account.
        #
        self.openPositionCount = kwargs.get("openPositionCount")
 
        #
        # The number of Orders currently pending in the Account.
        #
        self.pendingOrderCount = kwargs.get("pendingOrderCount")
 
        #
        # Flag indicating that the Account has hedging enabled.
        #
        self.hedgingEnabled = kwargs.get("hedgingEnabled")
 
        #
        # The date/time of the last order that was filled for this account.
        #
        self.lastOrderFillTimestamp = kwargs.get("lastOrderFillTimestamp")
 
        #
        # The total unrealized profit/loss for all Trades currently open in the
        # Account.
        #
        self.unrealizedPL = kwargs.get("unrealizedPL")
 
        #
        # The net asset value of the Account. Equal to Account balance +
        # unrealizedPL.
        #
        self.NAV = kwargs.get("NAV")
 
        #
        # Margin currently used for the Account.
        #
        self.marginUsed = kwargs.get("marginUsed")
 
        #
        # Margin available for Account currency.
        #
        self.marginAvailable = kwargs.get("marginAvailable")
 
        #
        # The value of the Account's open positions represented in the
        # Account's home currency.
        #
        self.positionValue = kwargs.get("positionValue")
 
        #
        # The Account's margin closeout unrealized PL.
        #
        self.marginCloseoutUnrealizedPL = kwargs.get("marginCloseoutUnrealizedPL")
 
        #
        # The Account's margin closeout NAV.
        #
        self.marginCloseoutNAV = kwargs.get("marginCloseoutNAV")
 
        #
        # The Account's margin closeout margin used.
        #
        self.marginCloseoutMarginUsed = kwargs.get("marginCloseoutMarginUsed")
 
        #
        # The Account's margin closeout percentage. When this value is 1.0 or
        # above the Account is in a margin closeout situation.
        #
        self.marginCloseoutPercent = kwargs.get("marginCloseoutPercent")
 
        #
        # The value of the Account's open positions as used for margin closeout
        # calculations represented in the Account's home currency.
        #
        self.marginCloseoutPositionValue = kwargs.get("marginCloseoutPositionValue")
 
        #
        # The current WithdrawalLimit for the account which will be zero or a
        # positive value indicating how much can be withdrawn from the account.
        #
        self.withdrawalLimit = kwargs.get("withdrawalLimit")
 
        #
        # The Account's margin call margin used.
        #
        self.marginCallMarginUsed = kwargs.get("marginCallMarginUsed")
 
        #
        # The Account's margin call percentage. When this value is 1.0 or above
        # the Account is in a margin call situation.
        #
        self.marginCallPercent = kwargs.get("marginCallPercent")
 
        #
        # The ID of the last Transaction created for the Account.
        #
        self.lastTransactionID = kwargs.get("lastTransactionID")
 
        #
        # The details of the Trades currently open in the Account.
        #
        self.trades = kwargs.get("trades")
 
        #
        # The details all Account Positions.
        #
        self.positions = kwargs.get("positions")
 
        #
        # The details of the Orders currently pending in the Account.
        #
        self.orders = kwargs.get("orders")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new Account from a dict (generally from loading a JSON
        response). The data used to instantiate the Account is a shallow copy
        of the dict passed in, with any complex child types instantiated
        appropriately.
        """

        data = data.copy()

        if data.get('balance') is not None:
            data['balance'] = ctx.convert_decimal_number(
                data.get('balance')
            )

        if data.get('pl') is not None:
            data['pl'] = ctx.convert_decimal_number(
                data.get('pl')
            )

        if data.get('resettablePL') is not None:
            data['resettablePL'] = ctx.convert_decimal_number(
                data.get('resettablePL')
            )

        if data.get('financing') is not None:
            data['financing'] = ctx.convert_decimal_number(
                data.get('financing')
            )

        if data.get('commission') is not None:
            data['commission'] = ctx.convert_decimal_number(
                data.get('commission')
            )

        if data.get('guaranteedExecutionFees') is not None:
            data['guaranteedExecutionFees'] = ctx.convert_decimal_number(
                data.get('guaranteedExecutionFees')
            )

        if data.get('marginRate') is not None:
            data['marginRate'] = ctx.convert_decimal_number(
                data.get('marginRate')
            )

        if data.get('unrealizedPL') is not None:
            data['unrealizedPL'] = ctx.convert_decimal_number(
                data.get('unrealizedPL')
            )

        if data.get('NAV') is not None:
            data['NAV'] = ctx.convert_decimal_number(
                data.get('NAV')
            )

        if data.get('marginUsed') is not None:
            data['marginUsed'] = ctx.convert_decimal_number(
                data.get('marginUsed')
            )

        if data.get('marginAvailable') is not None:
            data['marginAvailable'] = ctx.convert_decimal_number(
                data.get('marginAvailable')
            )

        if data.get('positionValue') is not None:
            data['positionValue'] = ctx.convert_decimal_number(
                data.get('positionValue')
            )

        if data.get('marginCloseoutUnrealizedPL') is not None:
            data['marginCloseoutUnrealizedPL'] = ctx.convert_decimal_number(
                data.get('marginCloseoutUnrealizedPL')
            )

        if data.get('marginCloseoutNAV') is not None:
            data['marginCloseoutNAV'] = ctx.convert_decimal_number(
                data.get('marginCloseoutNAV')
            )

        if data.get('marginCloseoutMarginUsed') is not None:
            data['marginCloseoutMarginUsed'] = ctx.convert_decimal_number(
                data.get('marginCloseoutMarginUsed')
            )

        if data.get('marginCloseoutPercent') is not None:
            data['marginCloseoutPercent'] = ctx.convert_decimal_number(
                data.get('marginCloseoutPercent')
            )

        if data.get('marginCloseoutPositionValue') is not None:
            data['marginCloseoutPositionValue'] = ctx.convert_decimal_number(
                data.get('marginCloseoutPositionValue')
            )

        if data.get('withdrawalLimit') is not None:
            data['withdrawalLimit'] = ctx.convert_decimal_number(
                data.get('withdrawalLimit')
            )

        if data.get('marginCallMarginUsed') is not None:
            data['marginCallMarginUsed'] = ctx.convert_decimal_number(
                data.get('marginCallMarginUsed')
            )

        if data.get('marginCallPercent') is not None:
            data['marginCallPercent'] = ctx.convert_decimal_number(
                data.get('marginCallPercent')
            )

        if data.get('trades') is not None:
            data['trades'] = [
                ctx.trade.TradeSummary.from_dict(d, ctx)
                for d in data.get('trades')
            ]

        if data.get('positions') is not None:
            data['positions'] = [
                ctx.position.Position.from_dict(d, ctx)
                for d in data.get('positions')
            ]

        if data.get('orders') is not None:
            data['orders'] = [
                ctx.order.Order.from_dict(d, ctx)
                for d in data.get('orders')
            ]

        return Account(**data)


class AccountChangesState(BaseEntity):
    """
    An AccountState Object is used to represent an Account's current price-
    dependent state. Price-dependent Account state is dependent on OANDA's
    current Prices, and includes things like unrealized PL, NAV and Trailing
    Stop Loss Order state.
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
    _properties = spec_properties.account_AccountChangesState

    def __init__(self, **kwargs):
        """
        Create a new AccountChangesState instance
        """
        super(AccountChangesState, self).__init__()
 
        #
        # The total unrealized profit/loss for all Trades currently open in the
        # Account.
        #
        self.unrealizedPL = kwargs.get("unrealizedPL")
 
        #
        # The net asset value of the Account. Equal to Account balance +
        # unrealizedPL.
        #
        self.NAV = kwargs.get("NAV")
 
        #
        # Margin currently used for the Account.
        #
        self.marginUsed = kwargs.get("marginUsed")
 
        #
        # Margin available for Account currency.
        #
        self.marginAvailable = kwargs.get("marginAvailable")
 
        #
        # The value of the Account's open positions represented in the
        # Account's home currency.
        #
        self.positionValue = kwargs.get("positionValue")
 
        #
        # The Account's margin closeout unrealized PL.
        #
        self.marginCloseoutUnrealizedPL = kwargs.get("marginCloseoutUnrealizedPL")
 
        #
        # The Account's margin closeout NAV.
        #
        self.marginCloseoutNAV = kwargs.get("marginCloseoutNAV")
 
        #
        # The Account's margin closeout margin used.
        #
        self.marginCloseoutMarginUsed = kwargs.get("marginCloseoutMarginUsed")
 
        #
        # The Account's margin closeout percentage. When this value is 1.0 or
        # above the Account is in a margin closeout situation.
        #
        self.marginCloseoutPercent = kwargs.get("marginCloseoutPercent")
 
        #
        # The value of the Account's open positions as used for margin closeout
        # calculations represented in the Account's home currency.
        #
        self.marginCloseoutPositionValue = kwargs.get("marginCloseoutPositionValue")
 
        #
        # The current WithdrawalLimit for the account which will be zero or a
        # positive value indicating how much can be withdrawn from the account.
        #
        self.withdrawalLimit = kwargs.get("withdrawalLimit")
 
        #
        # The Account's margin call margin used.
        #
        self.marginCallMarginUsed = kwargs.get("marginCallMarginUsed")
 
        #
        # The Account's margin call percentage. When this value is 1.0 or above
        # the Account is in a margin call situation.
        #
        self.marginCallPercent = kwargs.get("marginCallPercent")
 
        #
        # The price-dependent state of each pending Order in the Account.
        #
        self.orders = kwargs.get("orders")
 
        #
        # The price-dependent state for each open Trade in the Account.
        #
        self.trades = kwargs.get("trades")
 
        #
        # The price-dependent state for each open Position in the Account.
        #
        self.positions = kwargs.get("positions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new AccountChangesState from a dict (generally from
        loading a JSON response). The data used to instantiate the
        AccountChangesState is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('unrealizedPL') is not None:
            data['unrealizedPL'] = ctx.convert_decimal_number(
                data.get('unrealizedPL')
            )

        if data.get('NAV') is not None:
            data['NAV'] = ctx.convert_decimal_number(
                data.get('NAV')
            )

        if data.get('marginUsed') is not None:
            data['marginUsed'] = ctx.convert_decimal_number(
                data.get('marginUsed')
            )

        if data.get('marginAvailable') is not None:
            data['marginAvailable'] = ctx.convert_decimal_number(
                data.get('marginAvailable')
            )

        if data.get('positionValue') is not None:
            data['positionValue'] = ctx.convert_decimal_number(
                data.get('positionValue')
            )

        if data.get('marginCloseoutUnrealizedPL') is not None:
            data['marginCloseoutUnrealizedPL'] = ctx.convert_decimal_number(
                data.get('marginCloseoutUnrealizedPL')
            )

        if data.get('marginCloseoutNAV') is not None:
            data['marginCloseoutNAV'] = ctx.convert_decimal_number(
                data.get('marginCloseoutNAV')
            )

        if data.get('marginCloseoutMarginUsed') is not None:
            data['marginCloseoutMarginUsed'] = ctx.convert_decimal_number(
                data.get('marginCloseoutMarginUsed')
            )

        if data.get('marginCloseoutPercent') is not None:
            data['marginCloseoutPercent'] = ctx.convert_decimal_number(
                data.get('marginCloseoutPercent')
            )

        if data.get('marginCloseoutPositionValue') is not None:
            data['marginCloseoutPositionValue'] = ctx.convert_decimal_number(
                data.get('marginCloseoutPositionValue')
            )

        if data.get('withdrawalLimit') is not None:
            data['withdrawalLimit'] = ctx.convert_decimal_number(
                data.get('withdrawalLimit')
            )

        if data.get('marginCallMarginUsed') is not None:
            data['marginCallMarginUsed'] = ctx.convert_decimal_number(
                data.get('marginCallMarginUsed')
            )

        if data.get('marginCallPercent') is not None:
            data['marginCallPercent'] = ctx.convert_decimal_number(
                data.get('marginCallPercent')
            )

        if data.get('orders') is not None:
            data['orders'] = [
                ctx.order.DynamicOrderState.from_dict(d, ctx)
                for d in data.get('orders')
            ]

        if data.get('trades') is not None:
            data['trades'] = [
                ctx.trade.CalculatedTradeState.from_dict(d, ctx)
                for d in data.get('trades')
            ]

        if data.get('positions') is not None:
            data['positions'] = [
                ctx.position.CalculatedPositionState.from_dict(d, ctx)
                for d in data.get('positions')
            ]

        return AccountChangesState(**data)


class AccountProperties(BaseEntity):
    """
    Properties related to an Account.
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
    _properties = spec_properties.account_AccountProperties

    def __init__(self, **kwargs):
        """
        Create a new AccountProperties instance
        """
        super(AccountProperties, self).__init__()
 
        #
        # The Account's identifier
        #
        self.id = kwargs.get("id")
 
        #
        # The Account's associated MT4 Account ID. This field will not be
        # present if the Account is not an MT4 account.
        #
        self.mt4AccountID = kwargs.get("mt4AccountID")
 
        #
        # The Account's tags
        #
        self.tags = kwargs.get("tags")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new AccountProperties from a dict (generally from loading
        a JSON response). The data used to instantiate the AccountProperties is
        a shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()


        return AccountProperties(**data)


class AccountSummary(BaseEntity):
    """
    A summary representation of a client's Account. The AccountSummary does not
    provide to full specification of pending Orders, open Trades and Positions.
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
    _properties = spec_properties.account_AccountSummary

    def __init__(self, **kwargs):
        """
        Create a new AccountSummary instance
        """
        super(AccountSummary, self).__init__()
 
        #
        # The Account's identifier
        #
        self.id = kwargs.get("id")
 
        #
        # Client-assigned alias for the Account. Only provided if the Account
        # has an alias set
        #
        self.alias = kwargs.get("alias")
 
        #
        # The home currency of the Account
        #
        self.currency = kwargs.get("currency")
 
        #
        # The current balance of the Account.
        #
        self.balance = kwargs.get("balance")
 
        #
        # ID of the user that created the Account.
        #
        self.createdByUserID = kwargs.get("createdByUserID")
 
        #
        # The date/time when the Account was created.
        #
        self.createdTime = kwargs.get("createdTime")
 
        #
        # The current guaranteed Stop Loss Order mode of the Account.
        #
        self.guaranteedStopLossOrderMode = kwargs.get("guaranteedStopLossOrderMode")
 
        #
        # The total profit/loss realized over the lifetime of the Account.
        #
        self.pl = kwargs.get("pl")
 
        #
        # The total realized profit/loss for the Account since it was last
        # reset by the client.
        #
        self.resettablePL = kwargs.get("resettablePL")
 
        #
        # The date/time that the Account's resettablePL was last reset.
        #
        self.resettablePLTime = kwargs.get("resettablePLTime")
 
        #
        # The total amount of financing paid/collected over the lifetime of the
        # Account.
        #
        self.financing = kwargs.get("financing")
 
        #
        # The total amount of commission paid over the lifetime of the Account.
        #
        self.commission = kwargs.get("commission")
 
        #
        # The total amount of fees charged over the lifetime of the Account for
        # the execution of guaranteed Stop Loss Orders.
        #
        self.guaranteedExecutionFees = kwargs.get("guaranteedExecutionFees")
 
        #
        # Client-provided margin rate override for the Account. The effective
        # margin rate of the Account is the lesser of this value and the OANDA
        # margin rate for the Account's division. This value is only provided
        # if a margin rate override exists for the Account.
        #
        self.marginRate = kwargs.get("marginRate")
 
        #
        # The date/time when the Account entered a margin call state. Only
        # provided if the Account is in a margin call.
        #
        self.marginCallEnterTime = kwargs.get("marginCallEnterTime")
 
        #
        # The number of times that the Account's current margin call was
        # extended.
        #
        self.marginCallExtensionCount = kwargs.get("marginCallExtensionCount")
 
        #
        # The date/time of the Account's last margin call extension.
        #
        self.lastMarginCallExtensionTime = kwargs.get("lastMarginCallExtensionTime")
 
        #
        # The number of Trades currently open in the Account.
        #
        self.openTradeCount = kwargs.get("openTradeCount")
 
        #
        # The number of Positions currently open in the Account.
        #
        self.openPositionCount = kwargs.get("openPositionCount")
 
        #
        # The number of Orders currently pending in the Account.
        #
        self.pendingOrderCount = kwargs.get("pendingOrderCount")
 
        #
        # Flag indicating that the Account has hedging enabled.
        #
        self.hedgingEnabled = kwargs.get("hedgingEnabled")
 
        #
        # The date/time of the last order that was filled for this account.
        #
        self.lastOrderFillTimestamp = kwargs.get("lastOrderFillTimestamp")
 
        #
        # The total unrealized profit/loss for all Trades currently open in the
        # Account.
        #
        self.unrealizedPL = kwargs.get("unrealizedPL")
 
        #
        # The net asset value of the Account. Equal to Account balance +
        # unrealizedPL.
        #
        self.NAV = kwargs.get("NAV")
 
        #
        # Margin currently used for the Account.
        #
        self.marginUsed = kwargs.get("marginUsed")
 
        #
        # Margin available for Account currency.
        #
        self.marginAvailable = kwargs.get("marginAvailable")
 
        #
        # The value of the Account's open positions represented in the
        # Account's home currency.
        #
        self.positionValue = kwargs.get("positionValue")
 
        #
        # The Account's margin closeout unrealized PL.
        #
        self.marginCloseoutUnrealizedPL = kwargs.get("marginCloseoutUnrealizedPL")
 
        #
        # The Account's margin closeout NAV.
        #
        self.marginCloseoutNAV = kwargs.get("marginCloseoutNAV")
 
        #
        # The Account's margin closeout margin used.
        #
        self.marginCloseoutMarginUsed = kwargs.get("marginCloseoutMarginUsed")
 
        #
        # The Account's margin closeout percentage. When this value is 1.0 or
        # above the Account is in a margin closeout situation.
        #
        self.marginCloseoutPercent = kwargs.get("marginCloseoutPercent")
 
        #
        # The value of the Account's open positions as used for margin closeout
        # calculations represented in the Account's home currency.
        #
        self.marginCloseoutPositionValue = kwargs.get("marginCloseoutPositionValue")
 
        #
        # The current WithdrawalLimit for the account which will be zero or a
        # positive value indicating how much can be withdrawn from the account.
        #
        self.withdrawalLimit = kwargs.get("withdrawalLimit")
 
        #
        # The Account's margin call margin used.
        #
        self.marginCallMarginUsed = kwargs.get("marginCallMarginUsed")
 
        #
        # The Account's margin call percentage. When this value is 1.0 or above
        # the Account is in a margin call situation.
        #
        self.marginCallPercent = kwargs.get("marginCallPercent")
 
        #
        # The ID of the last Transaction created for the Account.
        #
        self.lastTransactionID = kwargs.get("lastTransactionID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new AccountSummary from a dict (generally from loading a
        JSON response). The data used to instantiate the AccountSummary is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('balance') is not None:
            data['balance'] = ctx.convert_decimal_number(
                data.get('balance')
            )

        if data.get('pl') is not None:
            data['pl'] = ctx.convert_decimal_number(
                data.get('pl')
            )

        if data.get('resettablePL') is not None:
            data['resettablePL'] = ctx.convert_decimal_number(
                data.get('resettablePL')
            )

        if data.get('financing') is not None:
            data['financing'] = ctx.convert_decimal_number(
                data.get('financing')
            )

        if data.get('commission') is not None:
            data['commission'] = ctx.convert_decimal_number(
                data.get('commission')
            )

        if data.get('guaranteedExecutionFees') is not None:
            data['guaranteedExecutionFees'] = ctx.convert_decimal_number(
                data.get('guaranteedExecutionFees')
            )

        if data.get('marginRate') is not None:
            data['marginRate'] = ctx.convert_decimal_number(
                data.get('marginRate')
            )

        if data.get('unrealizedPL') is not None:
            data['unrealizedPL'] = ctx.convert_decimal_number(
                data.get('unrealizedPL')
            )

        if data.get('NAV') is not None:
            data['NAV'] = ctx.convert_decimal_number(
                data.get('NAV')
            )

        if data.get('marginUsed') is not None:
            data['marginUsed'] = ctx.convert_decimal_number(
                data.get('marginUsed')
            )

        if data.get('marginAvailable') is not None:
            data['marginAvailable'] = ctx.convert_decimal_number(
                data.get('marginAvailable')
            )

        if data.get('positionValue') is not None:
            data['positionValue'] = ctx.convert_decimal_number(
                data.get('positionValue')
            )

        if data.get('marginCloseoutUnrealizedPL') is not None:
            data['marginCloseoutUnrealizedPL'] = ctx.convert_decimal_number(
                data.get('marginCloseoutUnrealizedPL')
            )

        if data.get('marginCloseoutNAV') is not None:
            data['marginCloseoutNAV'] = ctx.convert_decimal_number(
                data.get('marginCloseoutNAV')
            )

        if data.get('marginCloseoutMarginUsed') is not None:
            data['marginCloseoutMarginUsed'] = ctx.convert_decimal_number(
                data.get('marginCloseoutMarginUsed')
            )

        if data.get('marginCloseoutPercent') is not None:
            data['marginCloseoutPercent'] = ctx.convert_decimal_number(
                data.get('marginCloseoutPercent')
            )

        if data.get('marginCloseoutPositionValue') is not None:
            data['marginCloseoutPositionValue'] = ctx.convert_decimal_number(
                data.get('marginCloseoutPositionValue')
            )

        if data.get('withdrawalLimit') is not None:
            data['withdrawalLimit'] = ctx.convert_decimal_number(
                data.get('withdrawalLimit')
            )

        if data.get('marginCallMarginUsed') is not None:
            data['marginCallMarginUsed'] = ctx.convert_decimal_number(
                data.get('marginCallMarginUsed')
            )

        if data.get('marginCallPercent') is not None:
            data['marginCallPercent'] = ctx.convert_decimal_number(
                data.get('marginCallPercent')
            )

        return AccountSummary(**data)


class CalculatedAccountState(BaseEntity):
    """
    The dynamically calculated state of a client's Account.
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
    _properties = spec_properties.account_CalculatedAccountState

    def __init__(self, **kwargs):
        """
        Create a new CalculatedAccountState instance
        """
        super(CalculatedAccountState, self).__init__()
 
        #
        # The total unrealized profit/loss for all Trades currently open in the
        # Account.
        #
        self.unrealizedPL = kwargs.get("unrealizedPL")
 
        #
        # The net asset value of the Account. Equal to Account balance +
        # unrealizedPL.
        #
        self.NAV = kwargs.get("NAV")
 
        #
        # Margin currently used for the Account.
        #
        self.marginUsed = kwargs.get("marginUsed")
 
        #
        # Margin available for Account currency.
        #
        self.marginAvailable = kwargs.get("marginAvailable")
 
        #
        # The value of the Account's open positions represented in the
        # Account's home currency.
        #
        self.positionValue = kwargs.get("positionValue")
 
        #
        # The Account's margin closeout unrealized PL.
        #
        self.marginCloseoutUnrealizedPL = kwargs.get("marginCloseoutUnrealizedPL")
 
        #
        # The Account's margin closeout NAV.
        #
        self.marginCloseoutNAV = kwargs.get("marginCloseoutNAV")
 
        #
        # The Account's margin closeout margin used.
        #
        self.marginCloseoutMarginUsed = kwargs.get("marginCloseoutMarginUsed")
 
        #
        # The Account's margin closeout percentage. When this value is 1.0 or
        # above the Account is in a margin closeout situation.
        #
        self.marginCloseoutPercent = kwargs.get("marginCloseoutPercent")
 
        #
        # The value of the Account's open positions as used for margin closeout
        # calculations represented in the Account's home currency.
        #
        self.marginCloseoutPositionValue = kwargs.get("marginCloseoutPositionValue")
 
        #
        # The current WithdrawalLimit for the account which will be zero or a
        # positive value indicating how much can be withdrawn from the account.
        #
        self.withdrawalLimit = kwargs.get("withdrawalLimit")
 
        #
        # The Account's margin call margin used.
        #
        self.marginCallMarginUsed = kwargs.get("marginCallMarginUsed")
 
        #
        # The Account's margin call percentage. When this value is 1.0 or above
        # the Account is in a margin call situation.
        #
        self.marginCallPercent = kwargs.get("marginCallPercent")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new CalculatedAccountState from a dict (generally from
        loading a JSON response). The data used to instantiate the
        CalculatedAccountState is a shallow copy of the dict passed in, with
        any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('unrealizedPL') is not None:
            data['unrealizedPL'] = ctx.convert_decimal_number(
                data.get('unrealizedPL')
            )

        if data.get('NAV') is not None:
            data['NAV'] = ctx.convert_decimal_number(
                data.get('NAV')
            )

        if data.get('marginUsed') is not None:
            data['marginUsed'] = ctx.convert_decimal_number(
                data.get('marginUsed')
            )

        if data.get('marginAvailable') is not None:
            data['marginAvailable'] = ctx.convert_decimal_number(
                data.get('marginAvailable')
            )

        if data.get('positionValue') is not None:
            data['positionValue'] = ctx.convert_decimal_number(
                data.get('positionValue')
            )

        if data.get('marginCloseoutUnrealizedPL') is not None:
            data['marginCloseoutUnrealizedPL'] = ctx.convert_decimal_number(
                data.get('marginCloseoutUnrealizedPL')
            )

        if data.get('marginCloseoutNAV') is not None:
            data['marginCloseoutNAV'] = ctx.convert_decimal_number(
                data.get('marginCloseoutNAV')
            )

        if data.get('marginCloseoutMarginUsed') is not None:
            data['marginCloseoutMarginUsed'] = ctx.convert_decimal_number(
                data.get('marginCloseoutMarginUsed')
            )

        if data.get('marginCloseoutPercent') is not None:
            data['marginCloseoutPercent'] = ctx.convert_decimal_number(
                data.get('marginCloseoutPercent')
            )

        if data.get('marginCloseoutPositionValue') is not None:
            data['marginCloseoutPositionValue'] = ctx.convert_decimal_number(
                data.get('marginCloseoutPositionValue')
            )

        if data.get('withdrawalLimit') is not None:
            data['withdrawalLimit'] = ctx.convert_decimal_number(
                data.get('withdrawalLimit')
            )

        if data.get('marginCallMarginUsed') is not None:
            data['marginCallMarginUsed'] = ctx.convert_decimal_number(
                data.get('marginCallMarginUsed')
            )

        if data.get('marginCallPercent') is not None:
            data['marginCallPercent'] = ctx.convert_decimal_number(
                data.get('marginCallPercent')
            )

        return CalculatedAccountState(**data)


class AccountChanges(BaseEntity):
    """
    An AccountChanges Object is used to represent the changes to an Account's
    Orders, Trades and Positions since a specified Account TransactionID in the
    past.
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
    _properties = spec_properties.account_AccountChanges

    def __init__(self, **kwargs):
        """
        Create a new AccountChanges instance
        """
        super(AccountChanges, self).__init__()
 
        #
        # The Orders created. These Orders may have been filled, cancelled or
        # triggered in the same period.
        #
        self.ordersCreated = kwargs.get("ordersCreated")
 
        #
        # The Orders cancelled.
        #
        self.ordersCancelled = kwargs.get("ordersCancelled")
 
        #
        # The Orders filled.
        #
        self.ordersFilled = kwargs.get("ordersFilled")
 
        #
        # The Orders triggered.
        #
        self.ordersTriggered = kwargs.get("ordersTriggered")
 
        #
        # The Trades opened.
        #
        self.tradesOpened = kwargs.get("tradesOpened")
 
        #
        # The Trades reduced.
        #
        self.tradesReduced = kwargs.get("tradesReduced")
 
        #
        # The Trades closed.
        #
        self.tradesClosed = kwargs.get("tradesClosed")
 
        #
        # The Positions changed.
        #
        self.positions = kwargs.get("positions")
 
        #
        # The Transactions that have been generated.
        #
        self.transactions = kwargs.get("transactions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new AccountChanges from a dict (generally from loading a
        JSON response). The data used to instantiate the AccountChanges is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('ordersCreated') is not None:
            data['ordersCreated'] = [
                ctx.order.Order.from_dict(d, ctx)
                for d in data.get('ordersCreated')
            ]

        if data.get('ordersCancelled') is not None:
            data['ordersCancelled'] = [
                ctx.order.Order.from_dict(d, ctx)
                for d in data.get('ordersCancelled')
            ]

        if data.get('ordersFilled') is not None:
            data['ordersFilled'] = [
                ctx.order.Order.from_dict(d, ctx)
                for d in data.get('ordersFilled')
            ]

        if data.get('ordersTriggered') is not None:
            data['ordersTriggered'] = [
                ctx.order.Order.from_dict(d, ctx)
                for d in data.get('ordersTriggered')
            ]

        if data.get('tradesOpened') is not None:
            data['tradesOpened'] = [
                ctx.trade.TradeSummary.from_dict(d, ctx)
                for d in data.get('tradesOpened')
            ]

        if data.get('tradesReduced') is not None:
            data['tradesReduced'] = [
                ctx.trade.TradeSummary.from_dict(d, ctx)
                for d in data.get('tradesReduced')
            ]

        if data.get('tradesClosed') is not None:
            data['tradesClosed'] = [
                ctx.trade.TradeSummary.from_dict(d, ctx)
                for d in data.get('tradesClosed')
            ]

        if data.get('positions') is not None:
            data['positions'] = [
                ctx.position.Position.from_dict(d, ctx)
                for d in data.get('positions')
            ]

        if data.get('transactions') is not None:
            data['transactions'] = [
                ctx.transaction.Transaction.from_dict(d, ctx)
                for d in data.get('transactions')
            ]

        return AccountChanges(**data)


class EntitySpec(object):
    """
    The account.EntitySpec wraps the account module's type definitions
    and API methods so they can be easily accessed through an instance of a v20
    Context.
    """

    Account = Account
    AccountChangesState = AccountChangesState
    AccountProperties = AccountProperties
    AccountSummary = AccountSummary
    CalculatedAccountState = CalculatedAccountState
    AccountChanges = AccountChanges

    def __init__(self, ctx):
        self.ctx = ctx


    def list(
        self,
        **kwargs
    ):
        """
        Get a list of all Accounts authorized for the provided token.

        Args:

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('accounts') is not None:
                parsed_body['accounts'] = [
                    self.ctx.account.AccountProperties.from_dict(d, self.ctx)
                    for d in jbody.get('accounts')
                ]

        elif str(response.status) == "401":
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
        Get the full details for a single Account that a client has access to.
        Full pending Order, open Trade and open Position representations are
        provided.

        Args:
            accountID:
                Account Identifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('account') is not None:
                parsed_body['account'] = \
                    self.ctx.account.Account.from_dict(
                        jbody['account'],
                        self.ctx
                    )

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

        elif str(response.status) == "401":
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


    def summary(
        self,
        accountID,
        **kwargs
    ):
        """
        Get a summary for a single Account that a client has access to.

        Args:
            accountID:
                Account Identifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('account') is not None:
                parsed_body['account'] = \
                    self.ctx.account.AccountSummary.from_dict(
                        jbody['account'],
                        self.ctx
                    )

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

        elif str(response.status) == "401":
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


    def instruments(
        self,
        accountID,
        **kwargs
    ):
        """
        Get the list of tradeable instruments for the given Account. The list
        of tradeable instruments is dependent on the regulatory division that
        the Account is located in, thus should be the same for all Accounts
        owned by a single user.

        Args:
            accountID:
                Account Identifier
            instruments:
                List of instruments to query specifically.

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('instruments') is not None:
                parsed_body['instruments'] = [
                    self.ctx.primitives.Instrument.from_dict(d, self.ctx)
                    for d in jbody.get('instruments')
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

        elif str(response.status) == "401":
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


    def configure(
        self,
        accountID,
        **kwargs
    ):
        """
        Set the client-configurable portions of an Account.

        Args:
            accountID:
                Account Identifier
            alias:
                Client-defined alias (name) for the Account
            marginRate:
                The string representation of a decimal number.

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        if 'alias' in kwargs:
            body.set('alias', kwargs['alias'])

        if 'marginRate' in kwargs:
            body.set('marginRate', kwargs['marginRate'])

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
            if jbody.get('clientConfigureTransaction') is not None:
                parsed_body['clientConfigureTransaction'] = \
                    self.ctx.transaction.ClientConfigureTransaction.from_dict(
                        jbody['clientConfigureTransaction'],
                        self.ctx
                    )

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

        elif str(response.status) == "400":
            if jbody.get('clientConfigureRejectTransaction') is not None:
                parsed_body['clientConfigureRejectTransaction'] = \
                    self.ctx.transaction.ClientConfigureRejectTransaction.from_dict(
                        jbody['clientConfigureRejectTransaction'],
                        self.ctx
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

        elif str(response.status) == "403":
            if jbody.get('clientConfigureRejectTransaction') is not None:
                parsed_body['clientConfigureRejectTransaction'] = \
                    self.ctx.transaction.ClientConfigureRejectTransaction.from_dict(
                        jbody['clientConfigureRejectTransaction'],
                        self.ctx
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


    def changes(
        self,
        accountID,
        **kwargs
    ):
        """
        Endpoint used to poll an Account for its current state and changes
        since a specified TransactionID.

        Args:
            accountID:
                Account Identifier
            sinceTransactionID:
                ID of the Transaction to get Account changes since.

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('changes') is not None:
                parsed_body['changes'] = \
                    self.ctx.account.AccountChanges.from_dict(
                        jbody['changes'],
                        self.ctx
                    )

            if jbody.get('state') is not None:
                parsed_body['state'] = \
                    self.ctx.account.AccountChangesState.from_dict(
                        jbody['state'],
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

        elif str(response.status) == "416":
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

