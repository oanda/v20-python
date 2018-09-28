import ujson as json
from v20.base_entity import BaseEntity
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import spec_properties



class Transaction(BaseEntity):
    """
    The base Transaction specification. Specifies properties that are common
    between all Transaction.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = ""

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_Transaction

    def __init__(self, **kwargs):
        """
        Create a new Transaction instance
        """
        super(Transaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new Transaction from a dict (generally from loading a
        JSON response). The data used to instantiate the Transaction is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        type = data.get("type")

        if type == "MARKET_ORDER":
            return MarketOrderTransaction.from_dict(data, ctx)
        if type == "ORDER_FILL":
            return OrderFillTransaction.from_dict(data, ctx)
        if type == "ORDER_CANCEL":
            return OrderCancelTransaction.from_dict(data, ctx)
        if type == "MARKET_ORDER_REJECT":
            return MarketOrderRejectTransaction.from_dict(data, ctx)
        if type == "TRADE_CLIENT_EXTENSIONS_MODIFY":
            return TradeClientExtensionsModifyTransaction.from_dict(data, ctx)
        if type == "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT":
            return TradeClientExtensionsModifyRejectTransaction.from_dict(data, ctx)
        if type == "TAKE_PROFIT_ORDER":
            return TakeProfitOrderTransaction.from_dict(data, ctx)
        if type == "STOP_LOSS_ORDER":
            return StopLossOrderTransaction.from_dict(data, ctx)
        if type == "TRAILING_STOP_LOSS_ORDER":
            return TrailingStopLossOrderTransaction.from_dict(data, ctx)
        if type == "ORDER_CANCEL_REJECT":
            return OrderCancelRejectTransaction.from_dict(data, ctx)
        if type == "TAKE_PROFIT_ORDER_REJECT":
            return TakeProfitOrderRejectTransaction.from_dict(data, ctx)
        if type == "STOP_LOSS_ORDER_REJECT":
            return StopLossOrderRejectTransaction.from_dict(data, ctx)
        if type == "TRAILING_STOP_LOSS_ORDER_REJECT":
            return TrailingStopLossOrderRejectTransaction.from_dict(data, ctx)
        if type == "CLIENT_CONFIGURE":
            return ClientConfigureTransaction.from_dict(data, ctx)
        if type == "CLIENT_CONFIGURE_REJECT":
            return ClientConfigureRejectTransaction.from_dict(data, ctx)
        if type == "CREATE":
            return CreateTransaction.from_dict(data, ctx)
        if type == "CLOSE":
            return CloseTransaction.from_dict(data, ctx)
        if type == "REOPEN":
            return ReopenTransaction.from_dict(data, ctx)
        if type == "TRANSFER_FUNDS":
            return TransferFundsTransaction.from_dict(data, ctx)
        if type == "TRANSFER_FUNDS_REJECT":
            return TransferFundsRejectTransaction.from_dict(data, ctx)
        if type == "FIXED_PRICE_ORDER":
            return FixedPriceOrderTransaction.from_dict(data, ctx)
        if type == "LIMIT_ORDER":
            return LimitOrderTransaction.from_dict(data, ctx)
        if type == "LIMIT_ORDER_REJECT":
            return LimitOrderRejectTransaction.from_dict(data, ctx)
        if type == "STOP_ORDER":
            return StopOrderTransaction.from_dict(data, ctx)
        if type == "STOP_ORDER_REJECT":
            return StopOrderRejectTransaction.from_dict(data, ctx)
        if type == "MARKET_IF_TOUCHED_ORDER":
            return MarketIfTouchedOrderTransaction.from_dict(data, ctx)
        if type == "MARKET_IF_TOUCHED_ORDER_REJECT":
            return MarketIfTouchedOrderRejectTransaction.from_dict(data, ctx)
        if type == "ORDER_CLIENT_EXTENSIONS_MODIFY":
            return OrderClientExtensionsModifyTransaction.from_dict(data, ctx)
        if type == "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT":
            return OrderClientExtensionsModifyRejectTransaction.from_dict(data, ctx)
        if type == "MARGIN_CALL_ENTER":
            return MarginCallEnterTransaction.from_dict(data, ctx)
        if type == "MARGIN_CALL_EXTEND":
            return MarginCallExtendTransaction.from_dict(data, ctx)
        if type == "MARGIN_CALL_EXIT":
            return MarginCallExitTransaction.from_dict(data, ctx)
        if type == "DELAYED_TRADE_CLOSURE":
            return DelayedTradeClosureTransaction.from_dict(data, ctx)
        if type == "DAILY_FINANCING":
            return DailyFinancingTransaction.from_dict(data, ctx)
        if type == "RESET_RESETTABLE_PL":
            return ResetResettablePLTransaction.from_dict(data, ctx)

        data = data.copy()

        return Transaction(**data)


class CreateTransaction(BaseEntity):
    """
    A CreateTransaction represents the creation of an Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Create Account {accountID}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_CreateTransaction

    def __init__(self, **kwargs):
        """
        Create a new CreateTransaction instance
        """
        super(CreateTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "CREATE" in a
        # CreateTransaction.
        #
        self.type = kwargs.get("type", "CREATE")
 
        #
        # The ID of the Division that the Account is in
        #
        self.divisionID = kwargs.get("divisionID")
 
        #
        # The ID of the Site that the Account was created at
        #
        self.siteID = kwargs.get("siteID")
 
        #
        # The ID of the user that the Account was created for
        #
        self.accountUserID = kwargs.get("accountUserID")
 
        #
        # The number of the Account within the site/division/user
        #
        self.accountNumber = kwargs.get("accountNumber")
 
        #
        # The home currency of the Account
        #
        self.homeCurrency = kwargs.get("homeCurrency")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new CreateTransaction from a dict (generally from loading
        a JSON response). The data used to instantiate the CreateTransaction is
        a shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        return CreateTransaction(**data)


class CloseTransaction(BaseEntity):
    """
    A CloseTransaction represents the closing of an Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Close Account {accountID}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_CloseTransaction

    def __init__(self, **kwargs):
        """
        Create a new CloseTransaction instance
        """
        super(CloseTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "CLOSE" in a
        # CloseTransaction.
        #
        self.type = kwargs.get("type", "CLOSE")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new CloseTransaction from a dict (generally from loading
        a JSON response). The data used to instantiate the CloseTransaction is
        a shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        return CloseTransaction(**data)


class ReopenTransaction(BaseEntity):
    """
    A ReopenTransaction represents the re-opening of a closed Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Reopen Account {accountID}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_ReopenTransaction

    def __init__(self, **kwargs):
        """
        Create a new ReopenTransaction instance
        """
        super(ReopenTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "REOPEN" in a
        # ReopenTransaction.
        #
        self.type = kwargs.get("type", "REOPEN")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new ReopenTransaction from a dict (generally from loading
        a JSON response). The data used to instantiate the ReopenTransaction is
        a shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        return ReopenTransaction(**data)


class ClientConfigureTransaction(BaseEntity):
    """
    A ClientConfigureTransaction represents the configuration of an Account by
    a client.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Client Configure"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_ClientConfigureTransaction

    def __init__(self, **kwargs):
        """
        Create a new ClientConfigureTransaction instance
        """
        super(ClientConfigureTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "CLIENT_CONFIGURE" in a
        # ClientConfigureTransaction.
        #
        self.type = kwargs.get("type", "CLIENT_CONFIGURE")
 
        #
        # The client-provided alias for the Account.
        #
        self.alias = kwargs.get("alias")
 
        #
        # The margin rate override for the Account.
        #
        self.marginRate = kwargs.get("marginRate")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new ClientConfigureTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        ClientConfigureTransaction is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('marginRate') is not None:
            data['marginRate'] = ctx.convert_decimal_number(
                data.get('marginRate')
            )

        return ClientConfigureTransaction(**data)


class ClientConfigureRejectTransaction(BaseEntity):
    """
    A ClientConfigureRejectTransaction represents the reject of configuration
    of an Account by a client.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Client Configure Reject"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_ClientConfigureRejectTransaction

    def __init__(self, **kwargs):
        """
        Create a new ClientConfigureRejectTransaction instance
        """
        super(ClientConfigureRejectTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "CLIENT_CONFIGURE_REJECT"
        # in a ClientConfigureRejectTransaction.
        #
        self.type = kwargs.get("type", "CLIENT_CONFIGURE_REJECT")
 
        #
        # The client-provided alias for the Account.
        #
        self.alias = kwargs.get("alias")
 
        #
        # The margin rate override for the Account.
        #
        self.marginRate = kwargs.get("marginRate")
 
        #
        # The reason that the Reject Transaction was created
        #
        self.rejectReason = kwargs.get("rejectReason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new ClientConfigureRejectTransaction from a dict
        (generally from loading a JSON response). The data used to instantiate
        the ClientConfigureRejectTransaction is a shallow copy of the dict
        passed in, with any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('marginRate') is not None:
            data['marginRate'] = ctx.convert_decimal_number(
                data.get('marginRate')
            )

        return ClientConfigureRejectTransaction(**data)


class TransferFundsTransaction(BaseEntity):
    """
    A TransferFundsTransaction represents the transfer of funds in/out of an
    Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Account Transfer of {amount}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_TransferFundsTransaction

    def __init__(self, **kwargs):
        """
        Create a new TransferFundsTransaction instance
        """
        super(TransferFundsTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "TRANSFER_FUNDS" in a
        # TransferFundsTransaction.
        #
        self.type = kwargs.get("type", "TRANSFER_FUNDS")
 
        #
        # The amount to deposit/withdraw from the Account in the Account's home
        # currency. A positive value indicates a deposit, a negative value
        # indicates a withdrawal.
        #
        self.amount = kwargs.get("amount")
 
        #
        # The reason that an Account is being funded.
        #
        self.fundingReason = kwargs.get("fundingReason")
 
        #
        # An optional comment that may be attached to a fund transfer for audit
        # purposes
        #
        self.comment = kwargs.get("comment")
 
        #
        # The Account's balance after funds are transferred.
        #
        self.accountBalance = kwargs.get("accountBalance")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TransferFundsTransaction from a dict (generally from
        loading a JSON response). The data used to instantiate the
        TransferFundsTransaction is a shallow copy of the dict passed in, with
        any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('amount') is not None:
            data['amount'] = ctx.convert_decimal_number(
                data.get('amount')
            )

        if data.get('accountBalance') is not None:
            data['accountBalance'] = ctx.convert_decimal_number(
                data.get('accountBalance')
            )

        return TransferFundsTransaction(**data)


class TransferFundsRejectTransaction(BaseEntity):
    """
    A TransferFundsRejectTransaction represents the rejection of the transfer
    of funds in/out of an Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Account Reject Transfer of {amount}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_TransferFundsRejectTransaction

    def __init__(self, **kwargs):
        """
        Create a new TransferFundsRejectTransaction instance
        """
        super(TransferFundsRejectTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "TRANSFER_FUNDS_REJECT" in
        # a TransferFundsRejectTransaction.
        #
        self.type = kwargs.get("type", "TRANSFER_FUNDS_REJECT")
 
        #
        # The amount to deposit/withdraw from the Account in the Account's home
        # currency. A positive value indicates a deposit, a negative value
        # indicates a withdrawal.
        #
        self.amount = kwargs.get("amount")
 
        #
        # The reason that an Account is being funded.
        #
        self.fundingReason = kwargs.get("fundingReason")
 
        #
        # An optional comment that may be attached to a fund transfer for audit
        # purposes
        #
        self.comment = kwargs.get("comment")
 
        #
        # The reason that the Reject Transaction was created
        #
        self.rejectReason = kwargs.get("rejectReason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TransferFundsRejectTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        TransferFundsRejectTransaction is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('amount') is not None:
            data['amount'] = ctx.convert_decimal_number(
                data.get('amount')
            )

        return TransferFundsRejectTransaction(**data)


class MarketOrderTransaction(BaseEntity):
    """
    A MarketOrderTransaction represents the creation of a Market Order in the
    user's account. A Market Order is an Order that is filled immediately at
    the current market price. Market Orders can be specialized when they are
    created to accomplish a specific task: to close a Trade, to closeout a
    Position or to particiate in in a Margin closeout.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Create Market Order {id} ({reason}): {units} of {instrument}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_MarketOrderTransaction

    def __init__(self, **kwargs):
        """
        Create a new MarketOrderTransaction instance
        """
        super(MarketOrderTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "MARKET_ORDER" in a
        # MarketOrderTransaction.
        #
        self.type = kwargs.get("type", "MARKET_ORDER")
 
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
        # The reason that the Market Order was created
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The specification of the Take Profit Order that should be created for
        # a Trade opened when the Order is filled (if such a Trade is created).
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # The specification of the Trailing Stop Loss Order that should be
        # created for a Trade that is opened when the Order is filled (if such
        # a Trade is created).
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarketOrderTransaction from a dict (generally from
        loading a JSON response). The data used to instantiate the
        MarketOrderTransaction is a shallow copy of the dict passed in, with
        any complex child types instantiated appropriately.
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

        return MarketOrderTransaction(**data)


class MarketOrderRejectTransaction(BaseEntity):
    """
    A MarketOrderRejectTransaction represents the rejection of the creation of
    a Market Order.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Reject Market Order ({reason}): {units} of {instrument}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_MarketOrderRejectTransaction

    def __init__(self, **kwargs):
        """
        Create a new MarketOrderRejectTransaction instance
        """
        super(MarketOrderRejectTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "MARKET_ORDER_REJECT" in a
        # MarketOrderRejectTransaction.
        #
        self.type = kwargs.get("type", "MARKET_ORDER_REJECT")
 
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
        # The reason that the Market Order was created
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The specification of the Take Profit Order that should be created for
        # a Trade opened when the Order is filled (if such a Trade is created).
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # The specification of the Trailing Stop Loss Order that should be
        # created for a Trade that is opened when the Order is filled (if such
        # a Trade is created).
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")
 
        #
        # The reason that the Reject Transaction was created
        #
        self.rejectReason = kwargs.get("rejectReason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarketOrderRejectTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        MarketOrderRejectTransaction is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
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

        return MarketOrderRejectTransaction(**data)


class FixedPriceOrderTransaction(BaseEntity):
    """
    A FixedPriceOrderTransaction represents the creation of a Fixed Price Order
    in the user's account. A Fixed Price Order is an Order that is filled
    immediately at a specified price.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Create Fixed Price Order {id} ({reason}): {units} of {instrument}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_FixedPriceOrderTransaction

    def __init__(self, **kwargs):
        """
        Create a new FixedPriceOrderTransaction instance
        """
        super(FixedPriceOrderTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "FIXED_PRICE_ORDER" in a
        # FixedPriceOrderTransaction.
        #
        self.type = kwargs.get("type", "FIXED_PRICE_ORDER")
 
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
        # The reason that the Fixed Price Order was created
        #
        self.reason = kwargs.get("reason")
 
        #
        # The client extensions for the Fixed Price Order.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The specification of the Take Profit Order that should be created for
        # a Trade opened when the Order is filled (if such a Trade is created).
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # The specification of the Trailing Stop Loss Order that should be
        # created for a Trade that is opened when the Order is filled (if such
        # a Trade is created).
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new FixedPriceOrderTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        FixedPriceOrderTransaction is a shallow copy of the dict passed in,
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

        return FixedPriceOrderTransaction(**data)


class LimitOrderTransaction(BaseEntity):
    """
    A LimitOrderTransaction represents the creation of a Limit Order in the
    user's Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Create Limit Order {id} ({reason}): {units} of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_LimitOrderTransaction

    def __init__(self, **kwargs):
        """
        Create a new LimitOrderTransaction instance
        """
        super(LimitOrderTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "LIMIT_ORDER" in a
        # LimitOrderTransaction.
        #
        self.type = kwargs.get("type", "LIMIT_ORDER")
 
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
        # The reason that the Limit Order was initiated
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The specification of the Take Profit Order that should be created for
        # a Trade opened when the Order is filled (if such a Trade is created).
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # The specification of the Trailing Stop Loss Order that should be
        # created for a Trade that is opened when the Order is filled (if such
        # a Trade is created).
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")
 
        #
        # The ID of the Order that this Order replaces (only provided if this
        # Order replaces an existing Order).
        #
        self.replacesOrderID = kwargs.get("replacesOrderID")
 
        #
        # The ID of the Transaction that cancels the replaced Order (only
        # provided if this Order replaces an existing Order).
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new LimitOrderTransaction from a dict (generally from
        loading a JSON response). The data used to instantiate the
        LimitOrderTransaction is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
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

        return LimitOrderTransaction(**data)


class LimitOrderRejectTransaction(BaseEntity):
    """
    A LimitOrderRejectTransaction represents the rejection of the creation of a
    Limit Order.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Reject Limit Order ({reason}): {units} of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_LimitOrderRejectTransaction

    def __init__(self, **kwargs):
        """
        Create a new LimitOrderRejectTransaction instance
        """
        super(LimitOrderRejectTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "LIMIT_ORDER_REJECT" in a
        # LimitOrderRejectTransaction.
        #
        self.type = kwargs.get("type", "LIMIT_ORDER_REJECT")
 
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
        # The reason that the Limit Order was initiated
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The specification of the Take Profit Order that should be created for
        # a Trade opened when the Order is filled (if such a Trade is created).
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # The specification of the Trailing Stop Loss Order that should be
        # created for a Trade that is opened when the Order is filled (if such
        # a Trade is created).
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")
 
        #
        # The ID of the Order that this Order was intended to replace (only
        # provided if this Order was intended to replace an existing Order).
        #
        self.intendedReplacesOrderID = kwargs.get("intendedReplacesOrderID")
 
        #
        # The reason that the Reject Transaction was created
        #
        self.rejectReason = kwargs.get("rejectReason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new LimitOrderRejectTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        LimitOrderRejectTransaction is a shallow copy of the dict passed in,
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

        return LimitOrderRejectTransaction(**data)


class StopOrderTransaction(BaseEntity):
    """
    A StopOrderTransaction represents the creation of a Stop Order in the
    user's Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Create Stop Order {id} ({reason}): {units} of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_StopOrderTransaction

    def __init__(self, **kwargs):
        """
        Create a new StopOrderTransaction instance
        """
        super(StopOrderTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "STOP_ORDER" in a
        # StopOrderTransaction.
        #
        self.type = kwargs.get("type", "STOP_ORDER")
 
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
        # The reason that the Stop Order was initiated
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The specification of the Take Profit Order that should be created for
        # a Trade opened when the Order is filled (if such a Trade is created).
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # The specification of the Trailing Stop Loss Order that should be
        # created for a Trade that is opened when the Order is filled (if such
        # a Trade is created).
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")
 
        #
        # The ID of the Order that this Order replaces (only provided if this
        # Order replaces an existing Order).
        #
        self.replacesOrderID = kwargs.get("replacesOrderID")
 
        #
        # The ID of the Transaction that cancels the replaced Order (only
        # provided if this Order replaces an existing Order).
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new StopOrderTransaction from a dict (generally from
        loading a JSON response). The data used to instantiate the
        StopOrderTransaction is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
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

        return StopOrderTransaction(**data)


class StopOrderRejectTransaction(BaseEntity):
    """
    A StopOrderRejectTransaction represents the rejection of the creation of a
    Stop Order.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Reject Stop Order ({reason}): {units} of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_StopOrderRejectTransaction

    def __init__(self, **kwargs):
        """
        Create a new StopOrderRejectTransaction instance
        """
        super(StopOrderRejectTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "STOP_ORDER_REJECT" in a
        # StopOrderRejectTransaction.
        #
        self.type = kwargs.get("type", "STOP_ORDER_REJECT")
 
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
        # The reason that the Stop Order was initiated
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The specification of the Take Profit Order that should be created for
        # a Trade opened when the Order is filled (if such a Trade is created).
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # The specification of the Trailing Stop Loss Order that should be
        # created for a Trade that is opened when the Order is filled (if such
        # a Trade is created).
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")
 
        #
        # The ID of the Order that this Order was intended to replace (only
        # provided if this Order was intended to replace an existing Order).
        #
        self.intendedReplacesOrderID = kwargs.get("intendedReplacesOrderID")
 
        #
        # The reason that the Reject Transaction was created
        #
        self.rejectReason = kwargs.get("rejectReason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new StopOrderRejectTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        StopOrderRejectTransaction is a shallow copy of the dict passed in,
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

        return StopOrderRejectTransaction(**data)


class MarketIfTouchedOrderTransaction(BaseEntity):
    """
    A MarketIfTouchedOrderTransaction represents the creation of a
    MarketIfTouched Order in the user's Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Create MIT Order {id} ({reason}): {units} of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_MarketIfTouchedOrderTransaction

    def __init__(self, **kwargs):
        """
        Create a new MarketIfTouchedOrderTransaction instance
        """
        super(MarketIfTouchedOrderTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "MARKET_IF_TOUCHED_ORDER"
        # in a MarketIfTouchedOrderTransaction.
        #
        self.type = kwargs.get("type", "MARKET_IF_TOUCHED_ORDER")
 
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
        # The reason that the Market-if-touched Order was initiated
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The specification of the Take Profit Order that should be created for
        # a Trade opened when the Order is filled (if such a Trade is created).
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # The specification of the Trailing Stop Loss Order that should be
        # created for a Trade that is opened when the Order is filled (if such
        # a Trade is created).
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")
 
        #
        # The ID of the Order that this Order replaces (only provided if this
        # Order replaces an existing Order).
        #
        self.replacesOrderID = kwargs.get("replacesOrderID")
 
        #
        # The ID of the Transaction that cancels the replaced Order (only
        # provided if this Order replaces an existing Order).
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarketIfTouchedOrderTransaction from a dict
        (generally from loading a JSON response). The data used to instantiate
        the MarketIfTouchedOrderTransaction is a shallow copy of the dict
        passed in, with any complex child types instantiated appropriately.
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

        return MarketIfTouchedOrderTransaction(**data)


class MarketIfTouchedOrderRejectTransaction(BaseEntity):
    """
    A MarketIfTouchedOrderRejectTransaction represents the rejection of the
    creation of a MarketIfTouched Order.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Reject MIT Order ({reason}): {units} of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_MarketIfTouchedOrderRejectTransaction

    def __init__(self, **kwargs):
        """
        Create a new MarketIfTouchedOrderRejectTransaction instance
        """
        super(MarketIfTouchedOrderRejectTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to
        # "MARKET_IF_TOUCHED_ORDER_REJECT" in a
        # MarketIfTouchedOrderRejectTransaction.
        #
        self.type = kwargs.get("type", "MARKET_IF_TOUCHED_ORDER_REJECT")
 
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
        # The reason that the Market-if-touched Order was initiated
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The specification of the Take Profit Order that should be created for
        # a Trade opened when the Order is filled (if such a Trade is created).
        #
        self.takeProfitOnFill = kwargs.get("takeProfitOnFill")
 
        #
        # The specification of the Stop Loss Order that should be created for a
        # Trade opened when the Order is filled (if such a Trade is created).
        #
        self.stopLossOnFill = kwargs.get("stopLossOnFill")
 
        #
        # The specification of the Trailing Stop Loss Order that should be
        # created for a Trade that is opened when the Order is filled (if such
        # a Trade is created).
        #
        self.trailingStopLossOnFill = kwargs.get("trailingStopLossOnFill")
 
        #
        # Client Extensions to add to the Trade created when the Order is
        # filled (if such a Trade is created).  Do not set, modify, delete
        # tradeClientExtensions if your account is associated with MT4.
        #
        self.tradeClientExtensions = kwargs.get("tradeClientExtensions")
 
        #
        # The ID of the Order that this Order was intended to replace (only
        # provided if this Order was intended to replace an existing Order).
        #
        self.intendedReplacesOrderID = kwargs.get("intendedReplacesOrderID")
 
        #
        # The reason that the Reject Transaction was created
        #
        self.rejectReason = kwargs.get("rejectReason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarketIfTouchedOrderRejectTransaction from a dict
        (generally from loading a JSON response). The data used to instantiate
        the MarketIfTouchedOrderRejectTransaction is a shallow copy of the dict
        passed in, with any complex child types instantiated appropriately.
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

        return MarketIfTouchedOrderRejectTransaction(**data)


class TakeProfitOrderTransaction(BaseEntity):
    """
    A TakeProfitOrderTransaction represents the creation of a TakeProfit Order
    in the user's Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Create Take Profit Order {id} ({reason}): Close Trade {tradeID} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_TakeProfitOrderTransaction

    def __init__(self, **kwargs):
        """
        Create a new TakeProfitOrderTransaction instance
        """
        super(TakeProfitOrderTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "TAKE_PROFIT_ORDER" in a
        # TakeProfitOrderTransaction.
        #
        self.type = kwargs.get("type", "TAKE_PROFIT_ORDER")
 
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
        # The reason that the Take Profit Order was initiated
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The ID of the OrderFill Transaction that caused this Order to be
        # created (only provided if this Order was created automatically when
        # another Order was filled).
        #
        self.orderFillTransactionID = kwargs.get("orderFillTransactionID")
 
        #
        # The ID of the Order that this Order replaces (only provided if this
        # Order replaces an existing Order).
        #
        self.replacesOrderID = kwargs.get("replacesOrderID")
 
        #
        # The ID of the Transaction that cancels the replaced Order (only
        # provided if this Order replaces an existing Order).
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TakeProfitOrderTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        TakeProfitOrderTransaction is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
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

        return TakeProfitOrderTransaction(**data)


class TakeProfitOrderRejectTransaction(BaseEntity):
    """
    A TakeProfitOrderRejectTransaction represents the rejection of the creation
    of a TakeProfit Order.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Reject Take Profit Order ({reason}): Close Trade {tradeID} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_TakeProfitOrderRejectTransaction

    def __init__(self, **kwargs):
        """
        Create a new TakeProfitOrderRejectTransaction instance
        """
        super(TakeProfitOrderRejectTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "TAKE_PROFIT_ORDER_REJECT"
        # in a TakeProfitOrderRejectTransaction.
        #
        self.type = kwargs.get("type", "TAKE_PROFIT_ORDER_REJECT")
 
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
        # The reason that the Take Profit Order was initiated
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The ID of the OrderFill Transaction that caused this Order to be
        # created (only provided if this Order was created automatically when
        # another Order was filled).
        #
        self.orderFillTransactionID = kwargs.get("orderFillTransactionID")
 
        #
        # The ID of the Order that this Order was intended to replace (only
        # provided if this Order was intended to replace an existing Order).
        #
        self.intendedReplacesOrderID = kwargs.get("intendedReplacesOrderID")
 
        #
        # The reason that the Reject Transaction was created
        #
        self.rejectReason = kwargs.get("rejectReason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TakeProfitOrderRejectTransaction from a dict
        (generally from loading a JSON response). The data used to instantiate
        the TakeProfitOrderRejectTransaction is a shallow copy of the dict
        passed in, with any complex child types instantiated appropriately.
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

        return TakeProfitOrderRejectTransaction(**data)


class StopLossOrderTransaction(BaseEntity):
    """
    A StopLossOrderTransaction represents the creation of a StopLoss Order in
    the user's Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Create Stop Loss Order {id} ({reason}): Close Trade {tradeID} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_StopLossOrderTransaction

    def __init__(self, **kwargs):
        """
        Create a new StopLossOrderTransaction instance
        """
        super(StopLossOrderTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "STOP_LOSS_ORDER" in a
        # StopLossOrderTransaction.
        #
        self.type = kwargs.get("type", "STOP_LOSS_ORDER")
 
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
        # The fee that will be charged if the Stop Loss Order is guaranteed and
        # the Order is filled at the guaranteed price. The value is determined
        # at Order creation time. It is in price units and is charged for each
        # unit of the Trade.
        #
        self.guaranteedExecutionPremium = kwargs.get("guaranteedExecutionPremium")
 
        #
        # The reason that the Stop Loss Order was initiated
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The ID of the OrderFill Transaction that caused this Order to be
        # created (only provided if this Order was created automatically when
        # another Order was filled).
        #
        self.orderFillTransactionID = kwargs.get("orderFillTransactionID")
 
        #
        # The ID of the Order that this Order replaces (only provided if this
        # Order replaces an existing Order).
        #
        self.replacesOrderID = kwargs.get("replacesOrderID")
 
        #
        # The ID of the Transaction that cancels the replaced Order (only
        # provided if this Order replaces an existing Order).
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new StopLossOrderTransaction from a dict (generally from
        loading a JSON response). The data used to instantiate the
        StopLossOrderTransaction is a shallow copy of the dict passed in, with
        any complex child types instantiated appropriately.
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

        if data.get('guaranteedExecutionPremium') is not None:
            data['guaranteedExecutionPremium'] = ctx.convert_decimal_number(
                data.get('guaranteedExecutionPremium')
            )

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        return StopLossOrderTransaction(**data)


class StopLossOrderRejectTransaction(BaseEntity):
    """
    A StopLossOrderRejectTransaction represents the rejection of the creation
    of a StopLoss Order.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Reject Stop Loss Order ({reason}): Close Trade {tradeID} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_StopLossOrderRejectTransaction

    def __init__(self, **kwargs):
        """
        Create a new StopLossOrderRejectTransaction instance
        """
        super(StopLossOrderRejectTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "STOP_LOSS_ORDER_REJECT"
        # in a StopLossOrderRejectTransaction.
        #
        self.type = kwargs.get("type", "STOP_LOSS_ORDER_REJECT")
 
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
        # The reason that the Stop Loss Order was initiated
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The ID of the OrderFill Transaction that caused this Order to be
        # created (only provided if this Order was created automatically when
        # another Order was filled).
        #
        self.orderFillTransactionID = kwargs.get("orderFillTransactionID")
 
        #
        # The ID of the Order that this Order was intended to replace (only
        # provided if this Order was intended to replace an existing Order).
        #
        self.intendedReplacesOrderID = kwargs.get("intendedReplacesOrderID")
 
        #
        # The reason that the Reject Transaction was created
        #
        self.rejectReason = kwargs.get("rejectReason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new StopLossOrderRejectTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        StopLossOrderRejectTransaction is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
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

        return StopLossOrderRejectTransaction(**data)


class TrailingStopLossOrderTransaction(BaseEntity):
    """
    A TrailingStopLossOrderTransaction represents the creation of a
    TrailingStopLoss Order in the user's Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Create Trailing Stop Loss Order {id} ({reason}): Close Trade {tradeID}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_TrailingStopLossOrderTransaction

    def __init__(self, **kwargs):
        """
        Create a new TrailingStopLossOrderTransaction instance
        """
        super(TrailingStopLossOrderTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "TRAILING_STOP_LOSS_ORDER"
        # in a TrailingStopLossOrderTransaction.
        #
        self.type = kwargs.get("type", "TRAILING_STOP_LOSS_ORDER")
 
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
        # The reason that the Trailing Stop Loss Order was initiated
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The ID of the OrderFill Transaction that caused this Order to be
        # created (only provided if this Order was created automatically when
        # another Order was filled).
        #
        self.orderFillTransactionID = kwargs.get("orderFillTransactionID")
 
        #
        # The ID of the Order that this Order replaces (only provided if this
        # Order replaces an existing Order).
        #
        self.replacesOrderID = kwargs.get("replacesOrderID")
 
        #
        # The ID of the Transaction that cancels the replaced Order (only
        # provided if this Order replaces an existing Order).
        #
        self.cancellingTransactionID = kwargs.get("cancellingTransactionID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TrailingStopLossOrderTransaction from a dict
        (generally from loading a JSON response). The data used to instantiate
        the TrailingStopLossOrderTransaction is a shallow copy of the dict
        passed in, with any complex child types instantiated appropriately.
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

        return TrailingStopLossOrderTransaction(**data)


class TrailingStopLossOrderRejectTransaction(BaseEntity):
    """
    A TrailingStopLossOrderRejectTransaction represents the rejection of the
    creation of a TrailingStopLoss Order.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Reject Trailing Stop Loss Order ({reason}): Close Trade {tradeID}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_TrailingStopLossOrderRejectTransaction

    def __init__(self, **kwargs):
        """
        Create a new TrailingStopLossOrderRejectTransaction instance
        """
        super(TrailingStopLossOrderRejectTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to
        # "TRAILING_STOP_LOSS_ORDER_REJECT" in a
        # TrailingStopLossOrderRejectTransaction.
        #
        self.type = kwargs.get("type", "TRAILING_STOP_LOSS_ORDER_REJECT")
 
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
        # The reason that the Trailing Stop Loss Order was initiated
        #
        self.reason = kwargs.get("reason")
 
        #
        # Client Extensions to add to the Order (only provided if the Order is
        # being created with client extensions).
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The ID of the OrderFill Transaction that caused this Order to be
        # created (only provided if this Order was created automatically when
        # another Order was filled).
        #
        self.orderFillTransactionID = kwargs.get("orderFillTransactionID")
 
        #
        # The ID of the Order that this Order was intended to replace (only
        # provided if this Order was intended to replace an existing Order).
        #
        self.intendedReplacesOrderID = kwargs.get("intendedReplacesOrderID")
 
        #
        # The reason that the Reject Transaction was created
        #
        self.rejectReason = kwargs.get("rejectReason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TrailingStopLossOrderRejectTransaction from a dict
        (generally from loading a JSON response). The data used to instantiate
        the TrailingStopLossOrderRejectTransaction is a shallow copy of the
        dict passed in, with any complex child types instantiated
        appropriately.
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

        return TrailingStopLossOrderRejectTransaction(**data)


class OrderFillTransaction(BaseEntity):
    """
    An OrderFillTransaction represents the filling of an Order in the client's
    Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Fill Order {orderID} ({reason}): {units} of {instrument} @ {price}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_OrderFillTransaction

    def __init__(self, **kwargs):
        """
        Create a new OrderFillTransaction instance
        """
        super(OrderFillTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "ORDER_FILL" for an
        # OrderFillTransaction.
        #
        self.type = kwargs.get("type", "ORDER_FILL")
 
        #
        # The ID of the Order filled.
        #
        self.orderID = kwargs.get("orderID")
 
        #
        # The client Order ID of the Order filled (only provided if the client
        # has assigned one).
        #
        self.clientOrderID = kwargs.get("clientOrderID")
 
        #
        # The name of the filled Order's instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The number of units filled by the OrderFill.
        #
        self.units = kwargs.get("units")
 
        #
        # This is the conversion factor in effect for the Account at the time
        # of the OrderFill for converting any gains realized in Instrument
        # quote units into units of the Account's home currency.
        #
        self.gainQuoteHomeConversionFactor = kwargs.get("gainQuoteHomeConversionFactor")
 
        #
        # This is the conversion factor in effect for the Account at the time
        # of the OrderFill for converting any losses realized in Instrument
        # quote units into units of the Account's home currency.
        #
        self.lossQuoteHomeConversionFactor = kwargs.get("lossQuoteHomeConversionFactor")
 
        #
        # This field is now deprecated and should no longer be used. The
        # individual tradesClosed, tradeReduced and tradeOpened fields contain
        # the exact/official price each unit was filled at.
        #
        self.price = kwargs.get("price")
 
        #
        # The price that all of the units of the OrderFill should have been
        # filled at, in the absence of guaranteed price execution. This factors
        # in the Account's current ClientPrice, used liquidity and the units of
        # the OrderFill only. If no Trades were closed with their price clamped
        # for guaranteed stop loss enforcement, then this value will match the
        # price fields of each Trade opened, closed, and reduced, and they will
        # all be the exact same.
        #
        self.fullVWAP = kwargs.get("fullVWAP")
 
        #
        # The price in effect for the account at the time of the Order fill.
        #
        self.fullPrice = kwargs.get("fullPrice")
 
        #
        # The reason that an Order was filled
        #
        self.reason = kwargs.get("reason")
 
        #
        # The profit or loss incurred when the Order was filled.
        #
        self.pl = kwargs.get("pl")
 
        #
        # The financing paid or collected when the Order was filled.
        #
        self.financing = kwargs.get("financing")
 
        #
        # The commission charged in the Account's home currency as a result of
        # filling the Order. The commission is always represented as a positive
        # quantity of the Account's home currency, however it reduces the
        # balance in the Account.
        #
        self.commission = kwargs.get("commission")
 
        #
        # The total guaranteed execution fees charged for all Trades opened,
        # closed or reduced with guaranteed Stop Loss Orders.
        #
        self.guaranteedExecutionFee = kwargs.get("guaranteedExecutionFee")
 
        #
        # The Account's balance after the Order was filled.
        #
        self.accountBalance = kwargs.get("accountBalance")
 
        #
        # The Trade that was opened when the Order was filled (only provided if
        # filling the Order resulted in a new Trade).
        #
        self.tradeOpened = kwargs.get("tradeOpened")
 
        #
        # The Trades that were closed when the Order was filled (only provided
        # if filling the Order resulted in a closing open Trades).
        #
        self.tradesClosed = kwargs.get("tradesClosed")
 
        #
        # The Trade that was reduced when the Order was filled (only provided
        # if filling the Order resulted in reducing an open Trade).
        #
        self.tradeReduced = kwargs.get("tradeReduced")
 
        #
        # The half spread cost for the OrderFill, which is the sum of the
        # halfSpreadCost values in the tradeOpened, tradesClosed and
        # tradeReduced fields. This can be a positive or negative value and is
        # represented in the home currency of the Account.
        #
        self.halfSpreadCost = kwargs.get("halfSpreadCost")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new OrderFillTransaction from a dict (generally from
        loading a JSON response). The data used to instantiate the
        OrderFillTransaction is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('units') is not None:
            data['units'] = ctx.convert_decimal_number(
                data.get('units')
            )

        if data.get('gainQuoteHomeConversionFactor') is not None:
            data['gainQuoteHomeConversionFactor'] = ctx.convert_decimal_number(
                data.get('gainQuoteHomeConversionFactor')
            )

        if data.get('lossQuoteHomeConversionFactor') is not None:
            data['lossQuoteHomeConversionFactor'] = ctx.convert_decimal_number(
                data.get('lossQuoteHomeConversionFactor')
            )

        if data.get('price') is not None:
            data['price'] = ctx.convert_decimal_number(
                data.get('price')
            )

        if data.get('fullVWAP') is not None:
            data['fullVWAP'] = ctx.convert_decimal_number(
                data.get('fullVWAP')
            )

        if data.get('fullPrice') is not None:
            data['fullPrice'] = \
                ctx.pricing.ClientPrice.from_dict(
                    data['fullPrice'], ctx
                )

        if data.get('pl') is not None:
            data['pl'] = ctx.convert_decimal_number(
                data.get('pl')
            )

        if data.get('financing') is not None:
            data['financing'] = ctx.convert_decimal_number(
                data.get('financing')
            )

        if data.get('commission') is not None:
            data['commission'] = ctx.convert_decimal_number(
                data.get('commission')
            )

        if data.get('guaranteedExecutionFee') is not None:
            data['guaranteedExecutionFee'] = ctx.convert_decimal_number(
                data.get('guaranteedExecutionFee')
            )

        if data.get('accountBalance') is not None:
            data['accountBalance'] = ctx.convert_decimal_number(
                data.get('accountBalance')
            )

        if data.get('tradeOpened') is not None:
            data['tradeOpened'] = \
                ctx.transaction.TradeOpen.from_dict(
                    data['tradeOpened'], ctx
                )

        if data.get('tradesClosed') is not None:
            data['tradesClosed'] = [
                ctx.transaction.TradeReduce.from_dict(d, ctx)
                for d in data.get('tradesClosed')
            ]

        if data.get('tradeReduced') is not None:
            data['tradeReduced'] = \
                ctx.transaction.TradeReduce.from_dict(
                    data['tradeReduced'], ctx
                )

        if data.get('halfSpreadCost') is not None:
            data['halfSpreadCost'] = ctx.convert_decimal_number(
                data.get('halfSpreadCost')
            )

        return OrderFillTransaction(**data)


class OrderCancelTransaction(BaseEntity):
    """
    An OrderCancelTransaction represents the cancellation of an Order in the
    client's Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Cancel Order {orderID}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_OrderCancelTransaction

    def __init__(self, **kwargs):
        """
        Create a new OrderCancelTransaction instance
        """
        super(OrderCancelTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "ORDER_CANCEL" for an
        # OrderCancelTransaction.
        #
        self.type = kwargs.get("type", "ORDER_CANCEL")
 
        #
        # The ID of the Order cancelled
        #
        self.orderID = kwargs.get("orderID")
 
        #
        # The client ID of the Order cancelled (only provided if the Order has
        # a client Order ID).
        #
        self.clientOrderID = kwargs.get("clientOrderID")
 
        #
        # The reason that the Order was cancelled.
        #
        self.reason = kwargs.get("reason")
 
        #
        # The ID of the Order that replaced this Order (only provided if this
        # Order was cancelled for replacement).
        #
        self.replacedByOrderID = kwargs.get("replacedByOrderID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new OrderCancelTransaction from a dict (generally from
        loading a JSON response). The data used to instantiate the
        OrderCancelTransaction is a shallow copy of the dict passed in, with
        any complex child types instantiated appropriately.
        """

        data = data.copy()

        return OrderCancelTransaction(**data)


class OrderCancelRejectTransaction(BaseEntity):
    """
    An OrderCancelRejectTransaction represents the rejection of the
    cancellation of an Order in the client's Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Order Cancel Reject {orderID}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_OrderCancelRejectTransaction

    def __init__(self, **kwargs):
        """
        Create a new OrderCancelRejectTransaction instance
        """
        super(OrderCancelRejectTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "ORDER_CANCEL_REJECT" for
        # an OrderCancelRejectTransaction.
        #
        self.type = kwargs.get("type", "ORDER_CANCEL_REJECT")
 
        #
        # The ID of the Order intended to be cancelled
        #
        self.orderID = kwargs.get("orderID")
 
        #
        # The client ID of the Order intended to be cancelled (only provided if
        # the Order has a client Order ID).
        #
        self.clientOrderID = kwargs.get("clientOrderID")
 
        #
        # The reason that the Reject Transaction was created
        #
        self.rejectReason = kwargs.get("rejectReason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new OrderCancelRejectTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        OrderCancelRejectTransaction is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        return OrderCancelRejectTransaction(**data)


class OrderClientExtensionsModifyTransaction(BaseEntity):
    """
    A OrderClientExtensionsModifyTransaction represents the modification of an
    Order's Client Extensions.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Modify Order {orderID} Client Extensions"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_OrderClientExtensionsModifyTransaction

    def __init__(self, **kwargs):
        """
        Create a new OrderClientExtensionsModifyTransaction instance
        """
        super(OrderClientExtensionsModifyTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to
        # "ORDER_CLIENT_EXTENSIONS_MODIFY" for a
        # OrderClienteExtensionsModifyTransaction.
        #
        self.type = kwargs.get("type", "ORDER_CLIENT_EXTENSIONS_MODIFY")
 
        #
        # The ID of the Order who's client extensions are to be modified.
        #
        self.orderID = kwargs.get("orderID")
 
        #
        # The original Client ID of the Order who's client extensions are to be
        # modified.
        #
        self.clientOrderID = kwargs.get("clientOrderID")
 
        #
        # The new Client Extensions for the Order.
        #
        self.clientExtensionsModify = kwargs.get("clientExtensionsModify")
 
        #
        # The new Client Extensions for the Order's Trade on fill.
        #
        self.tradeClientExtensionsModify = kwargs.get("tradeClientExtensionsModify")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new OrderClientExtensionsModifyTransaction from a dict
        (generally from loading a JSON response). The data used to instantiate
        the OrderClientExtensionsModifyTransaction is a shallow copy of the
        dict passed in, with any complex child types instantiated
        appropriately.
        """

        data = data.copy()

        if data.get('clientExtensionsModify') is not None:
            data['clientExtensionsModify'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensionsModify'], ctx
                )

        if data.get('tradeClientExtensionsModify') is not None:
            data['tradeClientExtensionsModify'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensionsModify'], ctx
                )

        return OrderClientExtensionsModifyTransaction(**data)


class OrderClientExtensionsModifyRejectTransaction(BaseEntity):
    """
    A OrderClientExtensionsModifyRejectTransaction represents the rejection of
    the modification of an Order's Client Extensions.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Reject Modify Order {orderID} Client Extensions"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_OrderClientExtensionsModifyRejectTransaction

    def __init__(self, **kwargs):
        """
        Create a new OrderClientExtensionsModifyRejectTransaction instance
        """
        super(OrderClientExtensionsModifyRejectTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to
        # "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT" for a
        # OrderClientExtensionsModifyRejectTransaction.
        #
        self.type = kwargs.get("type", "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT")
 
        #
        # The ID of the Order who's client extensions are to be modified.
        #
        self.orderID = kwargs.get("orderID")
 
        #
        # The original Client ID of the Order who's client extensions are to be
        # modified.
        #
        self.clientOrderID = kwargs.get("clientOrderID")
 
        #
        # The new Client Extensions for the Order.
        #
        self.clientExtensionsModify = kwargs.get("clientExtensionsModify")
 
        #
        # The new Client Extensions for the Order's Trade on fill.
        #
        self.tradeClientExtensionsModify = kwargs.get("tradeClientExtensionsModify")
 
        #
        # The reason that the Reject Transaction was created
        #
        self.rejectReason = kwargs.get("rejectReason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new OrderClientExtensionsModifyRejectTransaction from a
        dict (generally from loading a JSON response). The data used to
        instantiate the OrderClientExtensionsModifyRejectTransaction is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('clientExtensionsModify') is not None:
            data['clientExtensionsModify'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensionsModify'], ctx
                )

        if data.get('tradeClientExtensionsModify') is not None:
            data['tradeClientExtensionsModify'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensionsModify'], ctx
                )

        return OrderClientExtensionsModifyRejectTransaction(**data)


class TradeClientExtensionsModifyTransaction(BaseEntity):
    """
    A TradeClientExtensionsModifyTransaction represents the modification of a
    Trade's Client Extensions.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Modify Trade {tradeID} Client Extensions"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_TradeClientExtensionsModifyTransaction

    def __init__(self, **kwargs):
        """
        Create a new TradeClientExtensionsModifyTransaction instance
        """
        super(TradeClientExtensionsModifyTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to
        # "TRADE_CLIENT_EXTENSIONS_MODIFY" for a
        # TradeClientExtensionsModifyTransaction.
        #
        self.type = kwargs.get("type", "TRADE_CLIENT_EXTENSIONS_MODIFY")
 
        #
        # The ID of the Trade who's client extensions are to be modified.
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The original Client ID of the Trade who's client extensions are to be
        # modified.
        #
        self.clientTradeID = kwargs.get("clientTradeID")
 
        #
        # The new Client Extensions for the Trade.
        #
        self.tradeClientExtensionsModify = kwargs.get("tradeClientExtensionsModify")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TradeClientExtensionsModifyTransaction from a dict
        (generally from loading a JSON response). The data used to instantiate
        the TradeClientExtensionsModifyTransaction is a shallow copy of the
        dict passed in, with any complex child types instantiated
        appropriately.
        """

        data = data.copy()

        if data.get('tradeClientExtensionsModify') is not None:
            data['tradeClientExtensionsModify'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensionsModify'], ctx
                )

        return TradeClientExtensionsModifyTransaction(**data)


class TradeClientExtensionsModifyRejectTransaction(BaseEntity):
    """
    A TradeClientExtensionsModifyRejectTransaction represents the rejection of
    the modification of a Trade's Client Extensions.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Reject Modify Trade {tradeID} Client Extensions"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_TradeClientExtensionsModifyRejectTransaction

    def __init__(self, **kwargs):
        """
        Create a new TradeClientExtensionsModifyRejectTransaction instance
        """
        super(TradeClientExtensionsModifyRejectTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to
        # "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT" for a
        # TradeClientExtensionsModifyRejectTransaction.
        #
        self.type = kwargs.get("type", "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT")
 
        #
        # The ID of the Trade who's client extensions are to be modified.
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The original Client ID of the Trade who's client extensions are to be
        # modified.
        #
        self.clientTradeID = kwargs.get("clientTradeID")
 
        #
        # The new Client Extensions for the Trade.
        #
        self.tradeClientExtensionsModify = kwargs.get("tradeClientExtensionsModify")
 
        #
        # The reason that the Reject Transaction was created
        #
        self.rejectReason = kwargs.get("rejectReason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TradeClientExtensionsModifyRejectTransaction from a
        dict (generally from loading a JSON response). The data used to
        instantiate the TradeClientExtensionsModifyRejectTransaction is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('tradeClientExtensionsModify') is not None:
            data['tradeClientExtensionsModify'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['tradeClientExtensionsModify'], ctx
                )

        return TradeClientExtensionsModifyRejectTransaction(**data)


class MarginCallEnterTransaction(BaseEntity):
    """
    A MarginCallEnterTransaction is created when an Account enters the margin
    call state.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Margin Call Enter"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_MarginCallEnterTransaction

    def __init__(self, **kwargs):
        """
        Create a new MarginCallEnterTransaction instance
        """
        super(MarginCallEnterTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "MARGIN_CALL_ENTER" for an
        # MarginCallEnterTransaction.
        #
        self.type = kwargs.get("type", "MARGIN_CALL_ENTER")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarginCallEnterTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        MarginCallEnterTransaction is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        return MarginCallEnterTransaction(**data)


class MarginCallExtendTransaction(BaseEntity):
    """
    A MarginCallExtendTransaction is created when the margin call state for an
    Account has been extended.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Margin Call Enter"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_MarginCallExtendTransaction

    def __init__(self, **kwargs):
        """
        Create a new MarginCallExtendTransaction instance
        """
        super(MarginCallExtendTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "MARGIN_CALL_EXTEND" for
        # an MarginCallExtendTransaction.
        #
        self.type = kwargs.get("type", "MARGIN_CALL_EXTEND")
 
        #
        # The number of the extensions to the Account's current margin call
        # that have been applied. This value will be set to 1 for the first
        # MarginCallExtend Transaction
        #
        self.extensionNumber = kwargs.get("extensionNumber")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarginCallExtendTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        MarginCallExtendTransaction is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        return MarginCallExtendTransaction(**data)


class MarginCallExitTransaction(BaseEntity):
    """
    A MarginCallExitnterTransaction is created when an Account leaves the
    margin call state.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Margin Call Exit"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_MarginCallExitTransaction

    def __init__(self, **kwargs):
        """
        Create a new MarginCallExitTransaction instance
        """
        super(MarginCallExitTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "MARGIN_CALL_EXIT" for an
        # MarginCallExitTransaction.
        #
        self.type = kwargs.get("type", "MARGIN_CALL_EXIT")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarginCallExitTransaction from a dict (generally from
        loading a JSON response). The data used to instantiate the
        MarginCallExitTransaction is a shallow copy of the dict passed in, with
        any complex child types instantiated appropriately.
        """

        data = data.copy()

        return MarginCallExitTransaction(**data)


class DelayedTradeClosureTransaction(BaseEntity):
    """
    A DelayedTradeClosure Transaction is created administratively to indicate
    open trades that should have been closed but weren't because the open
    trades' instruments were untradeable at the time. Open trades listed in
    this transaction will be closed once their respective instruments become
    tradeable.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Delayed Trade Closure"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_DelayedTradeClosureTransaction

    def __init__(self, **kwargs):
        """
        Create a new DelayedTradeClosureTransaction instance
        """
        super(DelayedTradeClosureTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "DELAYED_TRADE_CLOSURE"
        # for an DelayedTradeClosureTransaction.
        #
        self.type = kwargs.get("type", "DELAYED_TRADE_CLOSURE")
 
        #
        # The reason for the delayed trade closure
        #
        self.reason = kwargs.get("reason")
 
        #
        # List of Trade ID's identifying the open trades that will be closed
        # when their respective instruments become tradeable
        #
        self.tradeIDs = kwargs.get("tradeIDs")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new DelayedTradeClosureTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        DelayedTradeClosureTransaction is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        return DelayedTradeClosureTransaction(**data)


class DailyFinancingTransaction(BaseEntity):
    """
    A DailyFinancingTransaction represents the daily payment/collection of
    financing for an Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Daily Account Financing ({financing})"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_DailyFinancingTransaction

    def __init__(self, **kwargs):
        """
        Create a new DailyFinancingTransaction instance
        """
        super(DailyFinancingTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "DAILY_FINANCING" for a
        # DailyFinancingTransaction.
        #
        self.type = kwargs.get("type", "DAILY_FINANCING")
 
        #
        # The amount of financing paid/collected for the Account.
        #
        self.financing = kwargs.get("financing")
 
        #
        # The Account's balance after daily financing.
        #
        self.accountBalance = kwargs.get("accountBalance")
 
        #
        # The account financing mode at the time of the daily financing.
        #
        self.accountFinancingMode = kwargs.get("accountFinancingMode")
 
        #
        # The financing paid/collected for each Position in the Account.
        #
        self.positionFinancings = kwargs.get("positionFinancings")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new DailyFinancingTransaction from a dict (generally from
        loading a JSON response). The data used to instantiate the
        DailyFinancingTransaction is a shallow copy of the dict passed in, with
        any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('financing') is not None:
            data['financing'] = ctx.convert_decimal_number(
                data.get('financing')
            )

        if data.get('accountBalance') is not None:
            data['accountBalance'] = ctx.convert_decimal_number(
                data.get('accountBalance')
            )

        if data.get('positionFinancings') is not None:
            data['positionFinancings'] = [
                ctx.transaction.PositionFinancing.from_dict(d, ctx)
                for d in data.get('positionFinancings')
            ]

        return DailyFinancingTransaction(**data)


class ResetResettablePLTransaction(BaseEntity):
    """
    A ResetResettablePLTransaction represents the resetting of the Account's
    resettable PL counters.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "PL Reset"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Transaction {id}"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_ResetResettablePLTransaction

    def __init__(self, **kwargs):
        """
        Create a new ResetResettablePLTransaction instance
        """
        super(ResetResettablePLTransaction, self).__init__()
 
        #
        # The Transaction's Identifier.
        #
        self.id = kwargs.get("id")
 
        #
        # The date/time when the Transaction was created.
        #
        self.time = kwargs.get("time")
 
        #
        # The ID of the user that initiated the creation of the Transaction.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The ID of the Account the Transaction was created for.
        #
        self.accountID = kwargs.get("accountID")
 
        #
        # The ID of the "batch" that the Transaction belongs to. Transactions
        # in the same batch are applied to the Account simultaneously.
        #
        self.batchID = kwargs.get("batchID")
 
        #
        # The Request ID of the request which generated the transaction.
        #
        self.requestID = kwargs.get("requestID")
 
        #
        # The Type of the Transaction. Always set to "RESET_RESETTABLE_PL" for
        # a ResetResettablePLTransaction.
        #
        self.type = kwargs.get("type", "RESET_RESETTABLE_PL")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new ResetResettablePLTransaction from a dict (generally
        from loading a JSON response). The data used to instantiate the
        ResetResettablePLTransaction is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        return ResetResettablePLTransaction(**data)


class ClientExtensions(BaseEntity):
    """
    A ClientExtensions object allows a client to attach a clientID, tag and
    comment to Orders and Trades in their Account.  Do not set, modify, or
    delete this field if your account is associated with MT4.
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
    _properties = spec_properties.transaction_ClientExtensions

    def __init__(self, **kwargs):
        """
        Create a new ClientExtensions instance
        """
        super(ClientExtensions, self).__init__()
 
        #
        # The Client ID of the Order/Trade
        #
        self.id = kwargs.get("id")
 
        #
        # A tag associated with the Order/Trade
        #
        self.tag = kwargs.get("tag")
 
        #
        # A comment associated with the Order/Trade
        #
        self.comment = kwargs.get("comment")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new ClientExtensions from a dict (generally from loading
        a JSON response). The data used to instantiate the ClientExtensions is
        a shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        return ClientExtensions(**data)


class TakeProfitDetails(BaseEntity):
    """
    TakeProfitDetails specifies the details of a Take Profit Order to be
    created on behalf of a client. This may happen when an Order is filled that
    opens a Trade requiring a Take Profit, or when a Trade's dependent Take
    Profit Order is modified directly through the Trade.
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
    _properties = spec_properties.transaction_TakeProfitDetails

    def __init__(self, **kwargs):
        """
        Create a new TakeProfitDetails instance
        """
        super(TakeProfitDetails, self).__init__()
 
        #
        # The price that the Take Profit Order will be triggered at. Only one
        # of the price and distance fields may be specified.
        #
        self.price = kwargs.get("price")
 
        #
        # The time in force for the created Take Profit Order. This may only be
        # GTC, GTD or GFD.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date when the Take Profit Order will be cancelled on if
        # timeInForce is GTD.
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # The Client Extensions to add to the Take Profit Order when created.
        #
        self.clientExtensions = kwargs.get("clientExtensions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TakeProfitDetails from a dict (generally from loading
        a JSON response). The data used to instantiate the TakeProfitDetails is
        a shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
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

        return TakeProfitDetails(**data)


class StopLossDetails(BaseEntity):
    """
    StopLossDetails specifies the details of a Stop Loss Order to be created on
    behalf of a client. This may happen when an Order is filled that opens a
    Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is
    modified directly through the Trade.
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
    _properties = spec_properties.transaction_StopLossDetails

    def __init__(self, **kwargs):
        """
        Create a new StopLossDetails instance
        """
        super(StopLossDetails, self).__init__()
 
        #
        # The price that the Stop Loss Order will be triggered at. Only one of
        # the price and distance fields may be specified.
        #
        self.price = kwargs.get("price")
 
        #
        # Specifies the distance (in price units) from the Trade's open price
        # to use as the Stop Loss Order price. Only one of the distance and
        # price fields may be specified.
        #
        self.distance = kwargs.get("distance")
 
        #
        # The time in force for the created Stop Loss Order. This may only be
        # GTC, GTD or GFD.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date when the Stop Loss Order will be cancelled on if timeInForce
        # is GTD.
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # The Client Extensions to add to the Stop Loss Order when created.
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # Flag indicating that the price for the Stop Loss Order is guaranteed.
        # The default value depends on the GuaranteedStopLossOrderMode of the
        # account, if it is REQUIRED, the default will be true, for DISABLED or
        # ENABLED the default is false.
        #
        self.guaranteed = kwargs.get("guaranteed")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new StopLossDetails from a dict (generally from loading a
        JSON response). The data used to instantiate the StopLossDetails is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
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

        return StopLossDetails(**data)


class TrailingStopLossDetails(BaseEntity):
    """
    TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order
    to be created on behalf of a client. This may happen when an Order is
    filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's
    dependent Trailing Stop Loss Order is modified directly through the Trade.
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
    _properties = spec_properties.transaction_TrailingStopLossDetails

    def __init__(self, **kwargs):
        """
        Create a new TrailingStopLossDetails instance
        """
        super(TrailingStopLossDetails, self).__init__()
 
        #
        # The distance (in price units) from the Trade's fill price that the
        # Trailing Stop Loss Order will be triggered at.
        #
        self.distance = kwargs.get("distance")
 
        #
        # The time in force for the created Trailing Stop Loss Order. This may
        # only be GTC, GTD or GFD.
        #
        self.timeInForce = kwargs.get("timeInForce", "GTC")
 
        #
        # The date when the Trailing Stop Loss Order will be cancelled on if
        # timeInForce is GTD.
        #
        self.gtdTime = kwargs.get("gtdTime")
 
        #
        # The Client Extensions to add to the Trailing Stop Loss Order when
        # created.
        #
        self.clientExtensions = kwargs.get("clientExtensions")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TrailingStopLossDetails from a dict (generally from
        loading a JSON response). The data used to instantiate the
        TrailingStopLossDetails is a shallow copy of the dict passed in, with
        any complex child types instantiated appropriately.
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

        return TrailingStopLossDetails(**data)


class TradeOpen(BaseEntity):
    """
    A TradeOpen object represents a Trade for an instrument that was opened in
    an Account. It is found embedded in Transactions that affect the position
    of an instrument in the Account, specifically the OrderFill Transaction.
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
    _properties = spec_properties.transaction_TradeOpen

    def __init__(self, **kwargs):
        """
        Create a new TradeOpen instance
        """
        super(TradeOpen, self).__init__()
 
        #
        # The ID of the Trade that was opened
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The number of units opened by the Trade
        #
        self.units = kwargs.get("units")
 
        #
        # The average price that the units were opened at.
        #
        self.price = kwargs.get("price")
 
        #
        # This is the fee charged for opening the trade if it has a guaranteed
        # Stop Loss Order attached to it.
        #
        self.guaranteedExecutionFee = kwargs.get("guaranteedExecutionFee")
 
        #
        # The client extensions for the newly opened Trade
        #
        self.clientExtensions = kwargs.get("clientExtensions")
 
        #
        # The half spread cost for the trade open. This can be a positive or
        # negative value and is represented in the home currency of the
        # Account.
        #
        self.halfSpreadCost = kwargs.get("halfSpreadCost")
 
        #
        # The margin required at the time the Trade was created. Note, this is
        # the 'pure' margin required, it is not the 'effective' margin used
        # that factors in the trade risk if a GSLO is attached to the trade.
        #
        self.initialMarginRequired = kwargs.get("initialMarginRequired")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TradeOpen from a dict (generally from loading a JSON
        response). The data used to instantiate the TradeOpen is a shallow copy
        of the dict passed in, with any complex child types instantiated
        appropriately.
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

        if data.get('guaranteedExecutionFee') is not None:
            data['guaranteedExecutionFee'] = ctx.convert_decimal_number(
                data.get('guaranteedExecutionFee')
            )

        if data.get('clientExtensions') is not None:
            data['clientExtensions'] = \
                ctx.transaction.ClientExtensions.from_dict(
                    data['clientExtensions'], ctx
                )

        if data.get('halfSpreadCost') is not None:
            data['halfSpreadCost'] = ctx.convert_decimal_number(
                data.get('halfSpreadCost')
            )

        if data.get('initialMarginRequired') is not None:
            data['initialMarginRequired'] = ctx.convert_decimal_number(
                data.get('initialMarginRequired')
            )

        return TradeOpen(**data)


class TradeReduce(BaseEntity):
    """
    A TradeReduce object represents a Trade for an instrument that was reduced
    (either partially or fully) in an Account. It is found embedded in
    Transactions that affect the position of an instrument in the account,
    specifically the OrderFill Transaction.
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
    _properties = spec_properties.transaction_TradeReduce

    def __init__(self, **kwargs):
        """
        Create a new TradeReduce instance
        """
        super(TradeReduce, self).__init__()
 
        #
        # The ID of the Trade that was reduced or closed
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The number of units that the Trade was reduced by
        #
        self.units = kwargs.get("units")
 
        #
        # The average price that the units were closed at. This price may be
        # clamped for guaranteed Stop Loss Orders.
        #
        self.price = kwargs.get("price")
 
        #
        # The PL realized when reducing the Trade
        #
        self.realizedPL = kwargs.get("realizedPL")
 
        #
        # The financing paid/collected when reducing the Trade
        #
        self.financing = kwargs.get("financing")
 
        #
        # This is the fee that is charged for closing the Trade if it has a
        # guaranteed Stop Loss Order attached to it.
        #
        self.guaranteedExecutionFee = kwargs.get("guaranteedExecutionFee")
 
        #
        # The half spread cost for the trade reduce/close. This can be a
        # positive or negative value and is represented in the home currency of
        # the Account.
        #
        self.halfSpreadCost = kwargs.get("halfSpreadCost")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TradeReduce from a dict (generally from loading a
        JSON response). The data used to instantiate the TradeReduce is a
        shallow copy of the dict passed in, with any complex child types
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

        if data.get('realizedPL') is not None:
            data['realizedPL'] = ctx.convert_decimal_number(
                data.get('realizedPL')
            )

        if data.get('financing') is not None:
            data['financing'] = ctx.convert_decimal_number(
                data.get('financing')
            )

        if data.get('guaranteedExecutionFee') is not None:
            data['guaranteedExecutionFee'] = ctx.convert_decimal_number(
                data.get('guaranteedExecutionFee')
            )

        if data.get('halfSpreadCost') is not None:
            data['halfSpreadCost'] = ctx.convert_decimal_number(
                data.get('halfSpreadCost')
            )

        return TradeReduce(**data)


class MarketOrderTradeClose(BaseEntity):
    """
    A MarketOrderTradeClose specifies the extensions to a Market Order that has
    been created specifically to close a Trade.
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
    _properties = spec_properties.transaction_MarketOrderTradeClose

    def __init__(self, **kwargs):
        """
        Create a new MarketOrderTradeClose instance
        """
        super(MarketOrderTradeClose, self).__init__()
 
        #
        # The ID of the Trade requested to be closed
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The client ID of the Trade requested to be closed
        #
        self.clientTradeID = kwargs.get("clientTradeID")
 
        #
        # Indication of how much of the Trade to close. Either "ALL", or a
        # DecimalNumber reflection a partial close of the Trade.
        #
        self.units = kwargs.get("units")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarketOrderTradeClose from a dict (generally from
        loading a JSON response). The data used to instantiate the
        MarketOrderTradeClose is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
        """

        data = data.copy()

        return MarketOrderTradeClose(**data)


class MarketOrderMarginCloseout(BaseEntity):
    """
    Details for the Market Order extensions specific to a Market Order placed
    that is part of a Market Order Margin Closeout in a client's account
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
    _properties = spec_properties.transaction_MarketOrderMarginCloseout

    def __init__(self, **kwargs):
        """
        Create a new MarketOrderMarginCloseout instance
        """
        super(MarketOrderMarginCloseout, self).__init__()
 
        #
        # The reason the Market Order was created to perform a margin closeout
        #
        self.reason = kwargs.get("reason")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarketOrderMarginCloseout from a dict (generally from
        loading a JSON response). The data used to instantiate the
        MarketOrderMarginCloseout is a shallow copy of the dict passed in, with
        any complex child types instantiated appropriately.
        """

        data = data.copy()

        return MarketOrderMarginCloseout(**data)


class MarketOrderDelayedTradeClose(BaseEntity):
    """
    Details for the Market Order extensions specific to a Market Order placed
    with the intent of fully closing a specific open trade that should have
    already been closed but wasn't due to halted market conditions
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
    _properties = spec_properties.transaction_MarketOrderDelayedTradeClose

    def __init__(self, **kwargs):
        """
        Create a new MarketOrderDelayedTradeClose instance
        """
        super(MarketOrderDelayedTradeClose, self).__init__()
 
        #
        # The ID of the Trade being closed
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The Client ID of the Trade being closed
        #
        self.clientTradeID = kwargs.get("clientTradeID")
 
        #
        # The Transaction ID of the DelayedTradeClosure transaction to which
        # this Delayed Trade Close belongs to
        #
        self.sourceTransactionID = kwargs.get("sourceTransactionID")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarketOrderDelayedTradeClose from a dict (generally
        from loading a JSON response). The data used to instantiate the
        MarketOrderDelayedTradeClose is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        return MarketOrderDelayedTradeClose(**data)


class MarketOrderPositionCloseout(BaseEntity):
    """
    A MarketOrderPositionCloseout specifies the extensions to a Market Order
    when it has been created to closeout a specific Position.
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
    _properties = spec_properties.transaction_MarketOrderPositionCloseout

    def __init__(self, **kwargs):
        """
        Create a new MarketOrderPositionCloseout instance
        """
        super(MarketOrderPositionCloseout, self).__init__()
 
        #
        # The instrument of the Position being closed out.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # Indication of how much of the Position to close. Either "ALL", or a
        # DecimalNumber reflection a partial close of the Trade. The
        # DecimalNumber must always be positive, and represent a number that
        # doesn't exceed the absolute size of the Position.
        #
        self.units = kwargs.get("units")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new MarketOrderPositionCloseout from a dict (generally
        from loading a JSON response). The data used to instantiate the
        MarketOrderPositionCloseout is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        return MarketOrderPositionCloseout(**data)


class LiquidityRegenerationSchedule(BaseEntity):
    """
    A LiquidityRegenerationSchedule indicates how liquidity that is used when
    filling an Order for an instrument is regenerated following the fill.  A
    liquidity regeneration schedule will be in effect until the timestamp of
    its final step, but may be replaced by a schedule created for an Order of
    the same instrument that is filled while it is still in effect.
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
    _properties = spec_properties.transaction_LiquidityRegenerationSchedule

    def __init__(self, **kwargs):
        """
        Create a new LiquidityRegenerationSchedule instance
        """
        super(LiquidityRegenerationSchedule, self).__init__()
 
        #
        # The steps in the Liquidity Regeneration Schedule
        #
        self.steps = kwargs.get("steps")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new LiquidityRegenerationSchedule from a dict (generally
        from loading a JSON response). The data used to instantiate the
        LiquidityRegenerationSchedule is a shallow copy of the dict passed in,
        with any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('steps') is not None:
            data['steps'] = [
                ctx.transaction.LiquidityRegenerationScheduleStep.from_dict(d, ctx)
                for d in data.get('steps')
            ]

        return LiquidityRegenerationSchedule(**data)


class LiquidityRegenerationScheduleStep(BaseEntity):
    """
    A liquidity regeneration schedule Step indicates the amount of bid and ask
    liquidity that is used by the Account at a certain time. These amounts will
    only change at the timestamp of the following step.
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
    _properties = spec_properties.transaction_LiquidityRegenerationScheduleStep

    def __init__(self, **kwargs):
        """
        Create a new LiquidityRegenerationScheduleStep instance
        """
        super(LiquidityRegenerationScheduleStep, self).__init__()
 
        #
        # The timestamp of the schedule step.
        #
        self.timestamp = kwargs.get("timestamp")
 
        #
        # The amount of bid liquidity used at this step in the schedule.
        #
        self.bidLiquidityUsed = kwargs.get("bidLiquidityUsed")
 
        #
        # The amount of ask liquidity used at this step in the schedule.
        #
        self.askLiquidityUsed = kwargs.get("askLiquidityUsed")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new LiquidityRegenerationScheduleStep from a dict
        (generally from loading a JSON response). The data used to instantiate
        the LiquidityRegenerationScheduleStep is a shallow copy of the dict
        passed in, with any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('bidLiquidityUsed') is not None:
            data['bidLiquidityUsed'] = ctx.convert_decimal_number(
                data.get('bidLiquidityUsed')
            )

        if data.get('askLiquidityUsed') is not None:
            data['askLiquidityUsed'] = ctx.convert_decimal_number(
                data.get('askLiquidityUsed')
            )

        return LiquidityRegenerationScheduleStep(**data)


class OpenTradeFinancing(BaseEntity):
    """
    OpenTradeFinancing is used to pay/collect daily financing charge for an
    open Trade within an Account
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
    _properties = spec_properties.transaction_OpenTradeFinancing

    def __init__(self, **kwargs):
        """
        Create a new OpenTradeFinancing instance
        """
        super(OpenTradeFinancing, self).__init__()
 
        #
        # The ID of the Trade that financing is being paid/collected for.
        #
        self.tradeID = kwargs.get("tradeID")
 
        #
        # The amount of financing paid/collected for the Trade.
        #
        self.financing = kwargs.get("financing")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new OpenTradeFinancing from a dict (generally from
        loading a JSON response). The data used to instantiate the
        OpenTradeFinancing is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('financing') is not None:
            data['financing'] = ctx.convert_decimal_number(
                data.get('financing')
            )

        return OpenTradeFinancing(**data)


class PositionFinancing(BaseEntity):
    """
    OpenTradeFinancing is used to pay/collect daily financing charge for a
    Position within an Account
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
    _properties = spec_properties.transaction_PositionFinancing

    def __init__(self, **kwargs):
        """
        Create a new PositionFinancing instance
        """
        super(PositionFinancing, self).__init__()
 
        #
        # The instrument of the Position that financing is being paid/collected
        # for.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The amount of financing paid/collected for the Position.
        #
        self.financing = kwargs.get("financing")
 
        #
        # The financing paid/collecte for each open Trade within the Position.
        #
        self.openTradeFinancings = kwargs.get("openTradeFinancings")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new PositionFinancing from a dict (generally from loading
        a JSON response). The data used to instantiate the PositionFinancing is
        a shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('financing') is not None:
            data['financing'] = ctx.convert_decimal_number(
                data.get('financing')
            )

        if data.get('openTradeFinancings') is not None:
            data['openTradeFinancings'] = [
                ctx.transaction.OpenTradeFinancing.from_dict(d, ctx)
                for d in data.get('openTradeFinancings')
            ]

        return PositionFinancing(**data)


class TransactionHeartbeat(BaseEntity):
    """
    A TransactionHeartbeat object is injected into the Transaction stream to
    ensure that the HTTP connection remains active.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "Transaction Heartbeat {time}"

    #
    # Format string used when generating a name for this object
    #
    _name_format = ""

    #
    # Property metadata for this object
    #
    _properties = spec_properties.transaction_TransactionHeartbeat

    def __init__(self, **kwargs):
        """
        Create a new TransactionHeartbeat instance
        """
        super(TransactionHeartbeat, self).__init__()
 
        #
        # The string "HEARTBEAT"
        #
        self.type = kwargs.get("type", "HEARTBEAT")
 
        #
        # The ID of the most recent Transaction created for the Account
        #
        self.lastTransactionID = kwargs.get("lastTransactionID")
 
        #
        # The date/time when the TransactionHeartbeat was created.
        #
        self.time = kwargs.get("time")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new TransactionHeartbeat from a dict (generally from
        loading a JSON response). The data used to instantiate the
        TransactionHeartbeat is a shallow copy of the dict passed in, with any
        complex child types instantiated appropriately.
        """

        data = data.copy()

        return TransactionHeartbeat(**data)


class EntitySpec(object):
    """
    The transaction.EntitySpec wraps the transaction module's type definitions
    and API methods so they can be easily accessed through an instance of a v20
    Context.
    """

    Transaction = Transaction
    CreateTransaction = CreateTransaction
    CloseTransaction = CloseTransaction
    ReopenTransaction = ReopenTransaction
    ClientConfigureTransaction = ClientConfigureTransaction
    ClientConfigureRejectTransaction = ClientConfigureRejectTransaction
    TransferFundsTransaction = TransferFundsTransaction
    TransferFundsRejectTransaction = TransferFundsRejectTransaction
    MarketOrderTransaction = MarketOrderTransaction
    MarketOrderRejectTransaction = MarketOrderRejectTransaction
    FixedPriceOrderTransaction = FixedPriceOrderTransaction
    LimitOrderTransaction = LimitOrderTransaction
    LimitOrderRejectTransaction = LimitOrderRejectTransaction
    StopOrderTransaction = StopOrderTransaction
    StopOrderRejectTransaction = StopOrderRejectTransaction
    MarketIfTouchedOrderTransaction = MarketIfTouchedOrderTransaction
    MarketIfTouchedOrderRejectTransaction = MarketIfTouchedOrderRejectTransaction
    TakeProfitOrderTransaction = TakeProfitOrderTransaction
    TakeProfitOrderRejectTransaction = TakeProfitOrderRejectTransaction
    StopLossOrderTransaction = StopLossOrderTransaction
    StopLossOrderRejectTransaction = StopLossOrderRejectTransaction
    TrailingStopLossOrderTransaction = TrailingStopLossOrderTransaction
    TrailingStopLossOrderRejectTransaction = TrailingStopLossOrderRejectTransaction
    OrderFillTransaction = OrderFillTransaction
    OrderCancelTransaction = OrderCancelTransaction
    OrderCancelRejectTransaction = OrderCancelRejectTransaction
    OrderClientExtensionsModifyTransaction = OrderClientExtensionsModifyTransaction
    OrderClientExtensionsModifyRejectTransaction = OrderClientExtensionsModifyRejectTransaction
    TradeClientExtensionsModifyTransaction = TradeClientExtensionsModifyTransaction
    TradeClientExtensionsModifyRejectTransaction = TradeClientExtensionsModifyRejectTransaction
    MarginCallEnterTransaction = MarginCallEnterTransaction
    MarginCallExtendTransaction = MarginCallExtendTransaction
    MarginCallExitTransaction = MarginCallExitTransaction
    DelayedTradeClosureTransaction = DelayedTradeClosureTransaction
    DailyFinancingTransaction = DailyFinancingTransaction
    ResetResettablePLTransaction = ResetResettablePLTransaction
    ClientExtensions = ClientExtensions
    TakeProfitDetails = TakeProfitDetails
    StopLossDetails = StopLossDetails
    TrailingStopLossDetails = TrailingStopLossDetails
    TradeOpen = TradeOpen
    TradeReduce = TradeReduce
    MarketOrderTradeClose = MarketOrderTradeClose
    MarketOrderMarginCloseout = MarketOrderMarginCloseout
    MarketOrderDelayedTradeClose = MarketOrderDelayedTradeClose
    MarketOrderPositionCloseout = MarketOrderPositionCloseout
    LiquidityRegenerationSchedule = LiquidityRegenerationSchedule
    LiquidityRegenerationScheduleStep = LiquidityRegenerationScheduleStep
    OpenTradeFinancing = OpenTradeFinancing
    PositionFinancing = PositionFinancing
    TransactionHeartbeat = TransactionHeartbeat

    def __init__(self, ctx):
        self.ctx = ctx


    def list(
        self,
        accountID,
        **kwargs
    ):
        """
        Get a list of Transactions pages that satisfy a time-based Transaction
        query.

        Args:
            accountID:
                Account Identifier
            fromTime:
                The starting time (inclusive) of the time range for the
                Transactions being queried.
            toTime:
                The ending time (inclusive) of the time range for the
                Transactions being queried.
            pageSize:
                The number of Transactions to include in each page of the
                results.
            type:
                A filter for restricting the types of Transactions to retreive.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/accounts/{accountID}/transactions'
        )

        request.set_path_param(
            'accountID',
            accountID
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
            'pageSize',
            kwargs.get('pageSize')
        )

        request.set_param(
            'type',
            kwargs.get('type')
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
            if jbody.get('from') is not None:
                parsed_body['from'] = \
                    jbody.get('from')

            if jbody.get('to') is not None:
                parsed_body['to'] = \
                    jbody.get('to')

            if jbody.get('pageSize') is not None:
                parsed_body['pageSize'] = \
                    jbody.get('pageSize')

            if jbody.get('type') is not None:
                parsed_body['type'] = \
                    jbody.get('type')

            if jbody.get('count') is not None:
                parsed_body['count'] = \
                    jbody.get('count')

            if jbody.get('pages') is not None:
                parsed_body['pages'] = \
                    jbody.get('pages')

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

        elif str(response.status) == "403":
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


    def get(
        self,
        accountID,
        transactionID,
        **kwargs
    ):
        """
        Get the details of a single Account Transaction.

        Args:
            accountID:
                Account Identifier
            transactionID:
                A Transaction ID

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/accounts/{accountID}/transactions/{transactionID}'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'transactionID',
            transactionID
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
            if jbody.get('transaction') is not None:
                parsed_body['transaction'] = \
                    self.ctx.transaction.Transaction.from_dict(
                        jbody['transaction'],
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


    def range(
        self,
        accountID,
        **kwargs
    ):
        """
        Get a range of Transactions for an Account based on the Transaction
        IDs.

        Args:
            accountID:
                Account Identifier
            fromID:
                The starting Transacion ID (inclusive) to fetch.
            toID:
                The ending Transaction ID (inclusive) to fetch.
            type:
                The filter that restricts the types of Transactions to
                retreive.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/accounts/{accountID}/transactions/idrange'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_param(
            'from',
            kwargs.get('fromID')
        )

        request.set_param(
            'to',
            kwargs.get('toID')
        )

        request.set_param(
            'type',
            kwargs.get('type')
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
            if jbody.get('transactions') is not None:
                parsed_body['transactions'] = [
                    self.ctx.transaction.Transaction.from_dict(d, self.ctx)
                    for d in jbody.get('transactions')
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


    def since(
        self,
        accountID,
        **kwargs
    ):
        """
        Get a range of Transactions for an Account starting at (but not
        including) a provided Transaction ID.

        Args:
            accountID:
                Account Identifier
            id:
                The ID of the last Transacion fetched. This query will return
                all Transactions newer than the TransactionID.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/accounts/{accountID}/transactions/sinceid'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_param(
            'id',
            kwargs.get('id')
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
            if jbody.get('transactions') is not None:
                parsed_body['transactions'] = [
                    self.ctx.transaction.Transaction.from_dict(d, self.ctx)
                    for d in jbody.get('transactions')
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


    def stream(
        self,
        accountID,
        **kwargs
    ):
        """
        Get a stream of Transactions for an Account starting from when the
        request is made.

        Args:
            accountID:
                Account Identifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/accounts/{accountID}/transactions/stream'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_stream(True)

        class Parser():
            def __init__(self, ctx):
                self.ctx = ctx

            def __call__(self, line):
                j = json.loads(line.decode('utf-8'))

                type = j.get("type")

                if type is None:
                    return ("unknown", j)
                elif type == "HEARTBEAT":
                    return (
                        "transaction.TransactionHeartbeat",
                        self.ctx.transaction.TransactionHeartbeat.from_dict(
                            j,
                            self.ctx
                        )
                    )

                transaction = self.ctx.transaction.Transaction.from_dict(
                    j, self.ctx
                )

                return (
                    "transaction.Transaction",
                    transaction
                )

                
        request.set_line_parser(
            Parser(self.ctx)
        )

        response = self.ctx.request(request)


        return response

