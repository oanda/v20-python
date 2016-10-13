import json
from v20.base_entity import BaseEntity
from v20.base_entity import Property
from v20.base_entity import EntityDict
from v20.request import Request



class Transaction(BaseEntity):
    _summary_format = ""
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(Transaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):
        type = data.get("type")

        if type == "CREATE":
            return CreateTransaction.from_dict(data)
        if type == "CLOSE":
            return CloseTransaction.from_dict(data)
        if type == "REOPEN":
            return ReopenTransaction.from_dict(data)
        if type == "CLIENT_CONFIGURE":
            return ClientConfigureTransaction.from_dict(data)
        if type == "CLIENT_CONFIGURE_REJECT":
            return ClientConfigureRejectTransaction.from_dict(data)
        if type == "TRANSFER_FUNDS":
            return TransferFundsTransaction.from_dict(data)
        if type == "TRANSFER_FUNDS_REJECT":
            return TransferFundsRejectTransaction.from_dict(data)
        if type == "MARKET_ORDER":
            return MarketOrderTransaction.from_dict(data)
        if type == "MARKET_ORDER_REJECT":
            return MarketOrderRejectTransaction.from_dict(data)
        if type == "LIMIT_ORDER":
            return LimitOrderTransaction.from_dict(data)
        if type == "LIMIT_ORDER_REJECT":
            return LimitOrderRejectTransaction.from_dict(data)
        if type == "STOP_ORDER":
            return StopOrderTransaction.from_dict(data)
        if type == "STOP_ORDER_REJECT":
            return StopOrderRejectTransaction.from_dict(data)
        if type == "MARKET_IF_TOUCHED_ORDER":
            return MarketIfTouchedOrderTransaction.from_dict(data)
        if type == "MARKET_IF_TOUCHED_ORDER_REJECT":
            return MarketIfTouchedOrderRejectTransaction.from_dict(data)
        if type == "TAKE_PROFIT_ORDER":
            return TakeProfitOrderTransaction.from_dict(data)
        if type == "TAKE_PROFIT_ORDER_REJECT":
            return TakeProfitOrderRejectTransaction.from_dict(data)
        if type == "STOP_LOSS_ORDER":
            return StopLossOrderTransaction.from_dict(data)
        if type == "STOP_LOSS_ORDER_REJECT":
            return StopLossOrderRejectTransaction.from_dict(data)
        if type == "TRAILING_STOP_LOSS_ORDER":
            return TrailingStopLossOrderTransaction.from_dict(data)
        if type == "TRAILING_STOP_LOSS_ORDER_REJECT":
            return TrailingStopLossOrderRejectTransaction.from_dict(data)
        if type == "ORDER_FILL":
            return OrderFillTransaction.from_dict(data)
        if type == "ORDER_CANCEL":
            return OrderCancelTransaction.from_dict(data)
        if type == "ORDER_CANCEL_REJECT":
            return OrderCancelRejectTransaction.from_dict(data)
        if type == "ORDER_CLIENT_EXTENSIONS_MODIFY":
            return OrderClientExtensionsModifyTransaction.from_dict(data)
        if type == "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT":
            return OrderClientExtensionsModifyRejectTransaction.from_dict(data)
        if type == "TRADE_CLIENT_EXTENSIONS_MODIFY":
            return TradeClientExtensionsModifyTransaction.from_dict(data)
        if type == "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT":
            return TradeClientExtensionsModifyRejectTransaction.from_dict(data)
        if type == "MARGIN_CALL_ENTER":
            return MarginCallEnterTransaction.from_dict(data)
        if type == "MARGIN_CALL_EXTEND":
            return MarginCallExtendTransaction.from_dict(data)
        if type == "MARGIN_CALL_EXIT":
            return MarginCallExitTransaction.from_dict(data)
        if type == "DAILY_FINANCING":
            return DailyFinancingTransaction.from_dict(data)
        if type == "RESET_RESETTABLE_PL":
            return ResetResettablePLTransaction.from_dict(data)

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        self = Transaction(**body)

        return self


class CreateTransaction(BaseEntity):
    _summary_format = "Create Account {accountID}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"CREATE\" in a CreateTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "CREATE"
        ),
        Property(
            "divisionID",
            "Division ID",
            "The ID of the Division that the Account is in",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "siteID",
            "Site ID",
            "The ID of the Site that the Account was created at",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountUserID",
            "Account User ID",
            "The ID of the user that the Account was created for",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountNumber",
            "Account Number",
            "The number of the Account within the site/division/user",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "homeCurrency",
            "Home Currency",
            "The home currency of the Account",
            "primitive",
            "primitives.Currency",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(CreateTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('divisionID') is not None:
            body['divisionID'] = \
                data.get('divisionID')

        if data.get('siteID') is not None:
            body['siteID'] = \
                data.get('siteID')

        if data.get('accountUserID') is not None:
            body['accountUserID'] = \
                data.get('accountUserID')

        if data.get('accountNumber') is not None:
            body['accountNumber'] = \
                data.get('accountNumber')

        if data.get('homeCurrency') is not None:
            body['homeCurrency'] = \
                data.get('homeCurrency')

        self = CreateTransaction(**body)

        return self


class CloseTransaction(BaseEntity):
    _summary_format = "Close Account {accountID}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"CLOSE\" in a CloseTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "CLOSE"
        ),
    ]

    def __init__(self, **kwargs):
        super(CloseTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        self = CloseTransaction(**body)

        return self


class ReopenTransaction(BaseEntity):
    _summary_format = "Reopen Account {accountID}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"REOPEN\" in a ReopenTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "REOPEN"
        ),
    ]

    def __init__(self, **kwargs):
        super(ReopenTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        self = ReopenTransaction(**body)

        return self


class ClientConfigureTransaction(BaseEntity):
    _summary_format = "Client Configure"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"CLIENT_CONFIGURE\" in a ClientConfigureTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "CLIENT_CONFIGURE"
        ),
        Property(
            "alias",
            "Account Alias",
            "The client-provided alias for the Account.",
            "primitive",
            "string",
            False,
            None
        ),
        Property(
            "marginRate",
            "Margin Rate",
            "The margin rate override for the Account.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(ClientConfigureTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('alias') is not None:
            body['alias'] = \
                data.get('alias')

        if data.get('marginRate') is not None:
            body['marginRate'] = \
                data.get('marginRate')

        self = ClientConfigureTransaction(**body)

        return self


class ClientConfigureRejectTransaction(BaseEntity):
    _summary_format = "Client Configure Reject"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"CLIENT_CONFIGURE_REJECT\" in a ClientConfigureRejectTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "CLIENT_CONFIGURE_REJECT"
        ),
        Property(
            "alias",
            "Account Alias",
            "The client-provided alias for the Account.",
            "primitive",
            "string",
            False,
            None
        ),
        Property(
            "marginRate",
            "Margin Rate",
            "The margin rate override for the Account.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "rejectReason",
            "Reject Reason",
            "The reason that the Reject Transaction was created",
            "primitive",
            "transaction.TransactionRejectReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(ClientConfigureRejectTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('alias') is not None:
            body['alias'] = \
                data.get('alias')

        if data.get('marginRate') is not None:
            body['marginRate'] = \
                data.get('marginRate')

        if data.get('rejectReason') is not None:
            body['rejectReason'] = \
                data.get('rejectReason')

        self = ClientConfigureRejectTransaction(**body)

        return self


class TransferFundsTransaction(BaseEntity):
    _summary_format = "Account Transfer of {amount}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"TRANSFER_FUNDS\" in a TransferFundsTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "TRANSFER_FUNDS"
        ),
        Property(
            "amount",
            "Transfer Amount",
            "The amount to deposit/withdraw from the Account in the Account's home currency. A positive value indicates a deposit, a negative value indicates a withdrawal.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "fundingReason",
            "Reason",
            "The reason that an Account is being funded.",
            "primitive",
            "transaction.FundingReason",
            False,
            None
        ),
        Property(
            "accountBalance",
            "Account Balance",
            "The Account's balance after funds are transferred.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TransferFundsTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('amount') is not None:
            body['amount'] = \
                data.get('amount')

        if data.get('fundingReason') is not None:
            body['fundingReason'] = \
                data.get('fundingReason')

        if data.get('accountBalance') is not None:
            body['accountBalance'] = \
                data.get('accountBalance')

        self = TransferFundsTransaction(**body)

        return self


class TransferFundsRejectTransaction(BaseEntity):
    _summary_format = "Account Reject Transfer of {amount}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"TRANSFER_FUNDS_REJECT\" in a TransferFundsRejectTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "TRANSFER_FUNDS_REJECT"
        ),
        Property(
            "amount",
            "Transfer Amount",
            "The amount to deposit/withdraw from the Account in the Account's home currency. A positive value indicates a deposit, a negative value indicates a withdrawal.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "fundingReason",
            "Reason",
            "The reason that an Account is being funded.",
            "primitive",
            "transaction.FundingReason",
            False,
            None
        ),
        Property(
            "rejectReason",
            "Reject Reason",
            "The reason that the Reject Transaction was created",
            "primitive",
            "transaction.TransactionRejectReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TransferFundsRejectTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('amount') is not None:
            body['amount'] = \
                data.get('amount')

        if data.get('fundingReason') is not None:
            body['fundingReason'] = \
                data.get('fundingReason')

        if data.get('rejectReason') is not None:
            body['rejectReason'] = \
                data.get('rejectReason')

        self = TransferFundsRejectTransaction(**body)

        return self


class MarketOrderTransaction(BaseEntity):
    _summary_format = "Create Market Order {id} ({reason}): {units} of {instrument}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"MARKET_ORDER\" in a MarketOrderTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "MARKET_ORDER"
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
            "reason",
            "Reason",
            "The reason that the Market Order was created",
            "primitive",
            "transaction.MarketOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarketOrderTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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
                MarketOrderTradeClose.from_dict(
                    data['tradeClose']
                )

        if data.get('longPositionCloseout') is not None:
            body['longPositionCloseout'] = \
                MarketOrderPositionCloseout.from_dict(
                    data['longPositionCloseout']
                )

        if data.get('shortPositionCloseout') is not None:
            body['shortPositionCloseout'] = \
                MarketOrderPositionCloseout.from_dict(
                    data['shortPositionCloseout']
                )

        if data.get('marginCloseout') is not None:
            body['marginCloseout'] = \
                MarketOrderMarginCloseout.from_dict(
                    data['marginCloseout']
                )

        if data.get('delayedTradeClose') is not None:
            body['delayedTradeClose'] = \
                MarketOrderDelayedTradeClose.from_dict(
                    data['delayedTradeClose']
                )

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        self = MarketOrderTransaction(**body)

        return self


class MarketOrderRejectTransaction(BaseEntity):
    _summary_format = "Reject Market Order ({reason}): {units} of {instrument}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"MARKET_ORDER_REJECT\" in a MarketOrderRejectTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "MARKET_ORDER_REJECT"
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
            "reason",
            "Reason",
            "The reason that the Market Order was created",
            "primitive",
            "transaction.MarketOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "rejectReason",
            "Reject Reason",
            "The reason that the Reject Transaction was created",
            "primitive",
            "transaction.TransactionRejectReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarketOrderRejectTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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
                MarketOrderTradeClose.from_dict(
                    data['tradeClose']
                )

        if data.get('longPositionCloseout') is not None:
            body['longPositionCloseout'] = \
                MarketOrderPositionCloseout.from_dict(
                    data['longPositionCloseout']
                )

        if data.get('shortPositionCloseout') is not None:
            body['shortPositionCloseout'] = \
                MarketOrderPositionCloseout.from_dict(
                    data['shortPositionCloseout']
                )

        if data.get('marginCloseout') is not None:
            body['marginCloseout'] = \
                MarketOrderMarginCloseout.from_dict(
                    data['marginCloseout']
                )

        if data.get('delayedTradeClose') is not None:
            body['delayedTradeClose'] = \
                MarketOrderDelayedTradeClose.from_dict(
                    data['delayedTradeClose']
                )

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        if data.get('rejectReason') is not None:
            body['rejectReason'] = \
                data.get('rejectReason')

        self = MarketOrderRejectTransaction(**body)

        return self


class LimitOrderTransaction(BaseEntity):
    _summary_format = "Create Limit Order {id} ({reason}): {units} of {instrument} @ {price}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"LIMIT_ORDER\" in a LimitOrderTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "LIMIT_ORDER"
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
            "reason",
            "Reason",
            "The reason that the Limit Order was initiated",
            "primitive",
            "transaction.LimitOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "replacesOrderID",
            "Replaces Order ID",
            "The ID of the Order that this Order replaces (only provided if this Order replaces an existing Order).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "replacedOrderCancelTransactionID",
            "Replaces Order Cancel Transaction ID",
            "The ID of the Transaction that cancels the replaced Order (only provided if this Order replaces an existing Order).",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(LimitOrderTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        if data.get('replacesOrderID') is not None:
            body['replacesOrderID'] = \
                data.get('replacesOrderID')

        if data.get('replacedOrderCancelTransactionID') is not None:
            body['replacedOrderCancelTransactionID'] = \
                data.get('replacedOrderCancelTransactionID')

        self = LimitOrderTransaction(**body)

        return self


class LimitOrderRejectTransaction(BaseEntity):
    _summary_format = "Reject Limit Order ({reason}): {units} of {instrument} @ {price}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"LIMIT_ORDER_REJECT\" in a LimitOrderRejectTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "LIMIT_ORDER_REJECT"
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
            "reason",
            "Reason",
            "The reason that the Limit Order was initiated",
            "primitive",
            "transaction.LimitOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "intendedReplacesOrderID",
            "Order ID to Replace",
            "The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "rejectReason",
            "Reject Reason",
            "The reason that the Reject Transaction was created",
            "primitive",
            "transaction.TransactionRejectReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(LimitOrderRejectTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        if data.get('intendedReplacesOrderID') is not None:
            body['intendedReplacesOrderID'] = \
                data.get('intendedReplacesOrderID')

        if data.get('rejectReason') is not None:
            body['rejectReason'] = \
                data.get('rejectReason')

        self = LimitOrderRejectTransaction(**body)

        return self


class StopOrderTransaction(BaseEntity):
    _summary_format = "Create Stop Order {id} ({reason}): {units} of {instrument} @ {price}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"STOP_ORDER\" in a StopOrderTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "STOP_ORDER"
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
            "reason",
            "Reason",
            "The reason that the Stop Order was initiated",
            "primitive",
            "transaction.StopOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "replacesOrderID",
            "Replaces Order ID",
            "The ID of the Order that this Order replaces (only provided if this Order replaces an existing Order).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "replacedOrderCancelTransactionID",
            "Replaces Order Cancel Transaction ID",
            "The ID of the Transaction that cancels the replaced Order (only provided if this Order replaces an existing Order).",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(StopOrderTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        if data.get('replacesOrderID') is not None:
            body['replacesOrderID'] = \
                data.get('replacesOrderID')

        if data.get('replacedOrderCancelTransactionID') is not None:
            body['replacedOrderCancelTransactionID'] = \
                data.get('replacedOrderCancelTransactionID')

        self = StopOrderTransaction(**body)

        return self


class StopOrderRejectTransaction(BaseEntity):
    _summary_format = "Reject Stop Order ({reason}): {units} of {instrument} @ {price}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"STOP_ORDER_REJECT\" in a StopOrderRejectTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "STOP_ORDER_REJECT"
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
            "reason",
            "Reason",
            "The reason that the Stop Order was initiated",
            "primitive",
            "transaction.StopOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "intendedReplacesOrderID",
            "Order ID to Replace",
            "The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "rejectReason",
            "Reject Reason",
            "The reason that the Reject Transaction was created",
            "primitive",
            "transaction.TransactionRejectReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(StopOrderRejectTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        if data.get('intendedReplacesOrderID') is not None:
            body['intendedReplacesOrderID'] = \
                data.get('intendedReplacesOrderID')

        if data.get('rejectReason') is not None:
            body['rejectReason'] = \
                data.get('rejectReason')

        self = StopOrderRejectTransaction(**body)

        return self


class MarketIfTouchedOrderTransaction(BaseEntity):
    _summary_format = "Create MIT Order {id} ({reason}): {units} of {instrument} @ {price}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"MARKET_IF_TOUCHED_ORDER\" in a MarketIfTouchedOrderTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "MARKET_IF_TOUCHED_ORDER"
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
            "reason",
            "Reason",
            "The reason that the Market-if-touched Order was initiated",
            "primitive",
            "transaction.MarketIfTouchedOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "replacesOrderID",
            "Replaces Order ID",
            "The ID of the Order that this Order replaces (only provided if this Order replaces an existing Order).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "replacedOrderCancelTransactionID",
            "Replaces Order Cancel Transaction ID",
            "The ID of the Transaction that cancels the replaced Order (only provided if this Order replaces an existing Order).",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarketIfTouchedOrderTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        if data.get('replacesOrderID') is not None:
            body['replacesOrderID'] = \
                data.get('replacesOrderID')

        if data.get('replacedOrderCancelTransactionID') is not None:
            body['replacedOrderCancelTransactionID'] = \
                data.get('replacedOrderCancelTransactionID')

        self = MarketIfTouchedOrderTransaction(**body)

        return self


class MarketIfTouchedOrderRejectTransaction(BaseEntity):
    _summary_format = "Reject MIT Order ({reason}): {units} of {instrument} @ {price}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"MARKET_IF_TOUCHED_ORDER_REJECT\" in a MarketIfTouchedOrderRejectTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "MARKET_IF_TOUCHED_ORDER_REJECT"
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
            "reason",
            "Reason",
            "The reason that the Market-if-touched Order was initiated",
            "primitive",
            "transaction.MarketIfTouchedOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "takeProfitOnFill",
            "Take Profit On Fill",
            "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TakeProfitDetails",
            False,
            None
        ),
        Property(
            "stopLossOnFill",
            "Stop Loss On Fill",
            "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.StopLossDetails",
            False,
            None
        ),
        Property(
            "trailingStopLossOnFill",
            "Trailing Stop Loss On Fill",
            "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
            "object",
            "transaction.TrailingStopLossDetails",
            False,
            None
        ),
        Property(
            "tradeClientExtensions",
            "Trade Client Extensions",
            "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "intendedReplacesOrderID",
            "Order ID to Replace",
            "The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "rejectReason",
            "Reject Reason",
            "The reason that the Reject Transaction was created",
            "primitive",
            "transaction.TransactionRejectReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarketIfTouchedOrderRejectTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('takeProfitOnFill') is not None:
            body['takeProfitOnFill'] = \
                TakeProfitDetails.from_dict(
                    data['takeProfitOnFill']
                )

        if data.get('stopLossOnFill') is not None:
            body['stopLossOnFill'] = \
                StopLossDetails.from_dict(
                    data['stopLossOnFill']
                )

        if data.get('trailingStopLossOnFill') is not None:
            body['trailingStopLossOnFill'] = \
                TrailingStopLossDetails.from_dict(
                    data['trailingStopLossOnFill']
                )

        if data.get('tradeClientExtensions') is not None:
            body['tradeClientExtensions'] = \
                ClientExtensions.from_dict(
                    data['tradeClientExtensions']
                )

        if data.get('intendedReplacesOrderID') is not None:
            body['intendedReplacesOrderID'] = \
                data.get('intendedReplacesOrderID')

        if data.get('rejectReason') is not None:
            body['rejectReason'] = \
                data.get('rejectReason')

        self = MarketIfTouchedOrderRejectTransaction(**body)

        return self


class TakeProfitOrderTransaction(BaseEntity):
    _summary_format = "Create Take Profit Order {id} ({reason}): Close Trade {tradeID} @ {price}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"TAKE_PROFIT_ORDER\" in a TakeProfitOrderTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "TAKE_PROFIT_ORDER"
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
            "reason",
            "Reason",
            "The reason that the Take Profit Order was initiated",
            "primitive",
            "transaction.TakeProfitOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "orderFillTransactionID",
            "Order Fill Transaction ID",
            "The ID of the OrderFill Transaction that caused this Order to be created (only provided if this Order was created automatically when another Order was filled).",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "replacesOrderID",
            "Replaces Order ID",
            "The ID of the Order that this Order replaces (only provided if this Order replaces an existing Order).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "replacedOrderCancelTransactionID",
            "Replaces Order Cancel Transaction ID",
            "The ID of the Transaction that cancels the replaced Order (only provided if this Order replaces an existing Order).",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TakeProfitOrderTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('orderFillTransactionID') is not None:
            body['orderFillTransactionID'] = \
                data.get('orderFillTransactionID')

        if data.get('replacesOrderID') is not None:
            body['replacesOrderID'] = \
                data.get('replacesOrderID')

        if data.get('replacedOrderCancelTransactionID') is not None:
            body['replacedOrderCancelTransactionID'] = \
                data.get('replacedOrderCancelTransactionID')

        self = TakeProfitOrderTransaction(**body)

        return self


class TakeProfitOrderRejectTransaction(BaseEntity):
    _summary_format = "Reject Take Profit Order ({reason}): Close Trade {tradeID} @ {price}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"TAKE_PROFIT_ORDER_REJECT\" in a TakeProfitOrderRejectTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "TAKE_PROFIT_ORDER_REJECT"
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
            "reason",
            "Reason",
            "The reason that the Take Profit Order was initiated",
            "primitive",
            "transaction.TakeProfitOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "orderFillTransactionID",
            "Order Fill Transaction ID",
            "The ID of the OrderFill Transaction that caused this Order to be created (only provided if this Order was created automatically when another Order was filled).",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "intendedReplacesOrderID",
            "Order ID to Replace",
            "The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "rejectReason",
            "Reject Reason",
            "The reason that the Reject Transaction was created",
            "primitive",
            "transaction.TransactionRejectReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TakeProfitOrderRejectTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('orderFillTransactionID') is not None:
            body['orderFillTransactionID'] = \
                data.get('orderFillTransactionID')

        if data.get('intendedReplacesOrderID') is not None:
            body['intendedReplacesOrderID'] = \
                data.get('intendedReplacesOrderID')

        if data.get('rejectReason') is not None:
            body['rejectReason'] = \
                data.get('rejectReason')

        self = TakeProfitOrderRejectTransaction(**body)

        return self


class StopLossOrderTransaction(BaseEntity):
    _summary_format = "Create Stop Loss Order {id} ({reason}): Close Trade {tradeID} @ {price}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"STOP_LOSS_ORDER\" in a StopLossOrderTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "STOP_LOSS_ORDER"
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
            "reason",
            "Reason",
            "The reason that the Stop Loss Order was initiated",
            "primitive",
            "transaction.StopLossOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "orderFillTransactionID",
            "Order Fill Transaction ID",
            "The ID of the OrderFill Transaction that caused this Order to be created (only provided if this Order was created automatically when another Order was filled).",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "replacesOrderID",
            "Replaces Order ID",
            "The ID of the Order that this Order replaces (only provided if this Order replaces an existing Order).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "replacedOrderCancelTransactionID",
            "Replaces Order Cancel Transaction ID",
            "The ID of the Transaction that cancels the replaced Order (only provided if this Order replaces an existing Order).",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(StopLossOrderTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('orderFillTransactionID') is not None:
            body['orderFillTransactionID'] = \
                data.get('orderFillTransactionID')

        if data.get('replacesOrderID') is not None:
            body['replacesOrderID'] = \
                data.get('replacesOrderID')

        if data.get('replacedOrderCancelTransactionID') is not None:
            body['replacedOrderCancelTransactionID'] = \
                data.get('replacedOrderCancelTransactionID')

        self = StopLossOrderTransaction(**body)

        return self


class StopLossOrderRejectTransaction(BaseEntity):
    _summary_format = "Reject Stop Loss Order ({reason}): Close Trade {tradeID} @ {price}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"STOP_LOSS_ORDER_REJECT\" in a StopLossOrderRejectTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "STOP_LOSS_ORDER_REJECT"
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
            "reason",
            "Reason",
            "The reason that the Stop Loss Order was initiated",
            "primitive",
            "transaction.StopLossOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "orderFillTransactionID",
            "Order Fill Transaction ID",
            "The ID of the OrderFill Transaction that caused this Order to be created (only provided if this Order was created automatically when another Order was filled).",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "intendedReplacesOrderID",
            "Order ID to Replace",
            "The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "rejectReason",
            "Reject Reason",
            "The reason that the Reject Transaction was created",
            "primitive",
            "transaction.TransactionRejectReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(StopLossOrderRejectTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('orderFillTransactionID') is not None:
            body['orderFillTransactionID'] = \
                data.get('orderFillTransactionID')

        if data.get('intendedReplacesOrderID') is not None:
            body['intendedReplacesOrderID'] = \
                data.get('intendedReplacesOrderID')

        if data.get('rejectReason') is not None:
            body['rejectReason'] = \
                data.get('rejectReason')

        self = StopLossOrderRejectTransaction(**body)

        return self


class TrailingStopLossOrderTransaction(BaseEntity):
    _summary_format = "Create Trailing Stop Loss Order {id} ({reason}): Close Trade {tradeID}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"TRAILING_STOP_LOSS_ORDER\" in a TrailingStopLossOrderTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "TRAILING_STOP_LOSS_ORDER"
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
            "reason",
            "Reason",
            "The reason that the Trailing Stop Loss Order was initiated",
            "primitive",
            "transaction.TrailingStopLossOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "orderFillTransactionID",
            "Order Fill Transaction ID",
            "The ID of the OrderFill Transaction that caused this Order to be created (only provided if this Order was created automatically when another Order was filled).",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "replacesOrderID",
            "Replaces Order ID",
            "The ID of the Order that this Order replaces (only provided if this Order replaces an existing Order).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "replacedOrderCancelTransactionID",
            "Replaces Order Cancel Transaction ID",
            "The ID of the Transaction that cancels the replaced Order (only provided if this Order replaces an existing Order).",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TrailingStopLossOrderTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('orderFillTransactionID') is not None:
            body['orderFillTransactionID'] = \
                data.get('orderFillTransactionID')

        if data.get('replacesOrderID') is not None:
            body['replacesOrderID'] = \
                data.get('replacesOrderID')

        if data.get('replacedOrderCancelTransactionID') is not None:
            body['replacedOrderCancelTransactionID'] = \
                data.get('replacedOrderCancelTransactionID')

        self = TrailingStopLossOrderTransaction(**body)

        return self


class TrailingStopLossOrderRejectTransaction(BaseEntity):
    _summary_format = "Reject Trailing Stop Loss Order ({reason}): Close Trade {tradeID}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"TRAILING_STOP_LOSS_ORDER_REJECT\" in a TrailingStopLossOrderRejectTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "TRAILING_STOP_LOSS_ORDER_REJECT"
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
            "reason",
            "Reason",
            "The reason that the Trailing Stop Loss Order was initiated",
            "primitive",
            "transaction.TrailingStopLossOrderReason",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Order Client Extensions",
            "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "orderFillTransactionID",
            "Order Fill Transaction ID",
            "The ID of the OrderFill Transaction that caused this Order to be created (only provided if this Order was created automatically when another Order was filled).",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "intendedReplacesOrderID",
            "Order ID to Replace",
            "The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "rejectReason",
            "Reject Reason",
            "The reason that the Reject Transaction was created",
            "primitive",
            "transaction.TransactionRejectReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TrailingStopLossOrderRejectTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

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

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        if data.get('orderFillTransactionID') is not None:
            body['orderFillTransactionID'] = \
                data.get('orderFillTransactionID')

        if data.get('intendedReplacesOrderID') is not None:
            body['intendedReplacesOrderID'] = \
                data.get('intendedReplacesOrderID')

        if data.get('rejectReason') is not None:
            body['rejectReason'] = \
                data.get('rejectReason')

        self = TrailingStopLossOrderRejectTransaction(**body)

        return self


class OrderFillTransaction(BaseEntity):
    _summary_format = "Fill Order {orderID} ({reason}): {units} of {instrument} @ {price}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"ORDER_FILL\" for an OrderFillTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "ORDER_FILL"
        ),
        Property(
            "orderID",
            "Filled Order ID",
            "The ID of the Order filled.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "clientOrderID",
            "Filled Client Order ID",
            "The client Order ID of the Order filled (only provided if the client has assigned one).",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
        Property(
            "instrument",
            "Fill Instrument",
            "The name of the filled Order's instrument.",
            "primitive",
            "primitives.InstrumentName",
            False,
            None
        ),
        Property(
            "units",
            "Fill Units",
            "The number of units filled by the Order.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "price",
            "Fill Price",
            "The average market price that the Order was filled at.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "reason",
            "Fill Reason",
            "The reason that an Order was filled",
            "primitive",
            "transaction.OrderFillReason",
            False,
            None
        ),
        Property(
            "pl",
            "Profit/Loss",
            "The profit or loss incurred when the Order was filled.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "financing",
            "Financing",
            "The financing paid or collected when the Order was filled.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "accountBalance",
            "Account Balance",
            "The Account's balance after the Order was filled.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "tradeOpened",
            "Trade Opened",
            "The Trade that was opened when the Order was filled (only provided if filling the Order resulted in a new Trade).",
            "object",
            "transaction.TradeOpen",
            False,
            None
        ),
        Property(
            "tradesClosed",
            "Trades Closed",
            "The Trades that were closed when the Order was filled (only provided if filling the Order resulted in a closing open Trades).",
            "array_object",
            "TradeReduce",
            False,
            None
        ),
        Property(
            "tradeReduced",
            "Trade Reduced",
            "The Trade that was reduced when the Order was filled (only provided if filling the Order resulted in reducing an open Trade).",
            "object",
            "transaction.TradeReduce",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(OrderFillTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('orderID') is not None:
            body['orderID'] = \
                data.get('orderID')

        if data.get('clientOrderID') is not None:
            body['clientOrderID'] = \
                data.get('clientOrderID')

        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('pl') is not None:
            body['pl'] = \
                data.get('pl')

        if data.get('financing') is not None:
            body['financing'] = \
                data.get('financing')

        if data.get('accountBalance') is not None:
            body['accountBalance'] = \
                data.get('accountBalance')

        if data.get('tradeOpened') is not None:
            body['tradeOpened'] = \
                TradeOpen.from_dict(
                    data['tradeOpened']
                )

        if data.get('tradesClosed') is not None:
            body['tradesClosed'] = [
                TradeReduce.from_dict(d)
                for d in data.get('tradesClosed')
            ]

        if data.get('tradeReduced') is not None:
            body['tradeReduced'] = \
                TradeReduce.from_dict(
                    data['tradeReduced']
                )

        self = OrderFillTransaction(**body)

        return self


class OrderCancelTransaction(BaseEntity):
    _summary_format = "Cancel Order {orderID}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"ORDER_CANCEL\" for an OrderCancelTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "ORDER_CANCEL"
        ),
        Property(
            "orderID",
            "Cancelled Order ID",
            "The ID of the Order cancelled",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "clientOrderID",
            "Cancelled Client Order ID",
            "The client ID of the Order cancelled (only provided if the Order has a client Order ID).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "reason",
            "Cancel Reason",
            "The reason that the Order was cancelled.",
            "primitive",
            "transaction.OrderCancelReason",
            False,
            None
        ),
        Property(
            "replacedByOrderID",
            "Replaced By Order ID",
            "The ID of the Order that replaced this Order (only provided if this Order was cancelled for replacement).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(OrderCancelTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('orderID') is not None:
            body['orderID'] = \
                data.get('orderID')

        if data.get('clientOrderID') is not None:
            body['clientOrderID'] = \
                data.get('clientOrderID')

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('replacedByOrderID') is not None:
            body['replacedByOrderID'] = \
                data.get('replacedByOrderID')

        self = OrderCancelTransaction(**body)

        return self


class OrderCancelRejectTransaction(BaseEntity):
    _summary_format = "Order Cancel Reject {orderID}"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"ORDER_CANCEL_REJECT\" for an OrderCancelRejectTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "ORDER_CANCEL_REJECT"
        ),
        Property(
            "orderID",
            "Order ID",
            "The ID of the Order intended to be cancelled",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "clientOrderID",
            "Client Order ID",
            "The client ID of the Order intended to be cancelled (only provided if the Order has a client Order ID).",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "reason",
            "Cancel Reason",
            "The reason that the Order was to be cancelled.",
            "primitive",
            "transaction.OrderCancelReason",
            False,
            None
        ),
        Property(
            "rejectReason",
            "Reject Reason",
            "The reason that the Reject Transaction was created",
            "primitive",
            "transaction.TransactionRejectReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(OrderCancelRejectTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('orderID') is not None:
            body['orderID'] = \
                data.get('orderID')

        if data.get('clientOrderID') is not None:
            body['clientOrderID'] = \
                data.get('clientOrderID')

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('rejectReason') is not None:
            body['rejectReason'] = \
                data.get('rejectReason')

        self = OrderCancelRejectTransaction(**body)

        return self


class OrderClientExtensionsModifyTransaction(BaseEntity):
    _summary_format = "Modify Order {orderID} Client Extensions"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"ORDER_CLIENT_EXTENSIONS_MODIFY\" for a OrderClienteExtensionsModifyTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "ORDER_CLIENT_EXTENSIONS_MODIFY"
        ),
        Property(
            "orderID",
            "Order ID",
            "The ID of the Order who's client extensions are to be modified.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "clientOrderID",
            "Client Order ID",
            "The original Client ID of the Order who's client extensions are to be modified.",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
        Property(
            "orderClientExtensionsModify",
            "Order Extensions",
            "The new Client Extensions for the Order.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "tradeClientExtensionsModify",
            "Trade Extensions",
            "The new Client Extensions for the Order's Trade on fill.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(OrderClientExtensionsModifyTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('orderID') is not None:
            body['orderID'] = \
                data.get('orderID')

        if data.get('clientOrderID') is not None:
            body['clientOrderID'] = \
                data.get('clientOrderID')

        if data.get('orderClientExtensionsModify') is not None:
            body['orderClientExtensionsModify'] = \
                ClientExtensions.from_dict(
                    data['orderClientExtensionsModify']
                )

        if data.get('tradeClientExtensionsModify') is not None:
            body['tradeClientExtensionsModify'] = \
                ClientExtensions.from_dict(
                    data['tradeClientExtensionsModify']
                )

        self = OrderClientExtensionsModifyTransaction(**body)

        return self


class OrderClientExtensionsModifyRejectTransaction(BaseEntity):
    _summary_format = "Reject Modify Order {orderID} Client Extensions"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT\" for a OrderClientExtensionsModifyRejectTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT"
        ),
        Property(
            "orderID",
            "Order ID",
            "The ID of the Order who's client extensions are to be modified.",
            "primitive",
            "order.OrderID",
            False,
            None
        ),
        Property(
            "clientOrderID",
            "Client Order ID",
            "The original Client ID of the Order who's client extensions are to be modified.",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
        Property(
            "orderClientExtensionsModify",
            "Order Extensions",
            "The new Client Extensions for the Order.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "tradeClientExtensionsModify",
            "Trade Extensions",
            "The new Client Extensions for the Order's Trade on fill.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "rejectReason",
            "Reject Reason",
            "The reason that the Reject Transaction was created",
            "primitive",
            "transaction.TransactionRejectReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(OrderClientExtensionsModifyRejectTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('orderID') is not None:
            body['orderID'] = \
                data.get('orderID')

        if data.get('clientOrderID') is not None:
            body['clientOrderID'] = \
                data.get('clientOrderID')

        if data.get('orderClientExtensionsModify') is not None:
            body['orderClientExtensionsModify'] = \
                ClientExtensions.from_dict(
                    data['orderClientExtensionsModify']
                )

        if data.get('tradeClientExtensionsModify') is not None:
            body['tradeClientExtensionsModify'] = \
                ClientExtensions.from_dict(
                    data['tradeClientExtensionsModify']
                )

        if data.get('rejectReason') is not None:
            body['rejectReason'] = \
                data.get('rejectReason')

        self = OrderClientExtensionsModifyRejectTransaction(**body)

        return self


class TradeClientExtensionsModifyTransaction(BaseEntity):
    _summary_format = "Modify Trade {tradeID} Client Extensions"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"TRADE_CLIENT_EXTENSIONS_MODIFY\" for a TradeClientExtensionsModifyTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "TRADE_CLIENT_EXTENSIONS_MODIFY"
        ),
        Property(
            "tradeID",
            "Trade ID",
            "The ID of the Trade who's client extensions are to be modified.",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "clientTradeID",
            "Client Trade ID",
            "The original Client ID of the Trade who's client extensions are to be modified.",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
        Property(
            "tradeClientExtensionsModify",
            "Extensions",
            "The new Client Extensions for the Trade.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TradeClientExtensionsModifyTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('clientTradeID') is not None:
            body['clientTradeID'] = \
                data.get('clientTradeID')

        if data.get('tradeClientExtensionsModify') is not None:
            body['tradeClientExtensionsModify'] = \
                ClientExtensions.from_dict(
                    data['tradeClientExtensionsModify']
                )

        self = TradeClientExtensionsModifyTransaction(**body)

        return self


class TradeClientExtensionsModifyRejectTransaction(BaseEntity):
    _summary_format = "Reject Modify Trade {tradeID} Client Extensions"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT\" for a TradeClientExtensionsModifyRejectTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT"
        ),
        Property(
            "tradeID",
            "Trade ID",
            "The ID of the Trade who's client extensions are to be modified.",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "clientTradeID",
            "Client Trade ID",
            "The original Client ID of the Trade who's client extensions are to be modified.",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
        Property(
            "tradeClientExtensionsModify",
            "Extensions",
            "The new Client Extensions for the Trade.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
        Property(
            "rejectReason",
            "Reject Reason",
            "The reason that the Reject Transaction was created",
            "primitive",
            "transaction.TransactionRejectReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TradeClientExtensionsModifyRejectTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('clientTradeID') is not None:
            body['clientTradeID'] = \
                data.get('clientTradeID')

        if data.get('tradeClientExtensionsModify') is not None:
            body['tradeClientExtensionsModify'] = \
                ClientExtensions.from_dict(
                    data['tradeClientExtensionsModify']
                )

        if data.get('rejectReason') is not None:
            body['rejectReason'] = \
                data.get('rejectReason')

        self = TradeClientExtensionsModifyRejectTransaction(**body)

        return self


class MarginCallEnterTransaction(BaseEntity):
    _summary_format = "Margin Call Enter"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"MARGIN_CALL_ENTER\" for an MarginCallEnterTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "MARGIN_CALL_ENTER"
        ),
    ]

    def __init__(self, **kwargs):
        super(MarginCallEnterTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        self = MarginCallEnterTransaction(**body)

        return self


class MarginCallExtendTransaction(BaseEntity):
    _summary_format = "Margin Call Enter"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"MARGIN_CALL_EXTEND\" for an MarginCallExtendTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "MARGIN_CALL_EXTEND"
        ),
        Property(
            "extensionNumber",
            "Extension Number",
            "The number of the extensions to the Account's current margin call that have been applied. This value will be set to 1 for the first MarginCallExtend Transaction",
            "primitive",
            "integer",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarginCallExtendTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('extensionNumber') is not None:
            body['extensionNumber'] = \
                data.get('extensionNumber')

        self = MarginCallExtendTransaction(**body)

        return self


class MarginCallExitTransaction(BaseEntity):
    _summary_format = "Margin Call Exit"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"MARGIN_CALL_EXIT\" for an MarginCallExitTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "MARGIN_CALL_EXIT"
        ),
    ]

    def __init__(self, **kwargs):
        super(MarginCallExitTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        self = MarginCallExitTransaction(**body)

        return self


class DelayedTradeClosureTransaction(BaseEntity):
    _summary_format = "Delayed Trade Closure"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "reason",
            "Reason",
            "The reason for the delayed trade closure",
            "primitive",
            "transaction.MarketOrderReason",
            False,
            None
        ),
        Property(
            "tradeIDs",
            "Trade ID's",
            "List of Trade ID's identifying the open trades that will be closed when their respective instruments become tradeable",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(DelayedTradeClosureTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        if data.get('tradeIDs') is not None:
            body['tradeIDs'] = \
                data.get('tradeIDs')

        self = DelayedTradeClosureTransaction(**body)

        return self


class DailyFinancingTransaction(BaseEntity):
    _summary_format = "Daily Account Financing ({financing})"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"DAILY_FINANCING\" for a DailyFinancingTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "DAILY_FINANCING"
        ),
        Property(
            "financing",
            "Financing",
            "The amount of financing paid/collected for the Account.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "accountBalance",
            "Account Balance",
            "The Account's balance after daily financing.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "accountFinancingMode",
            "Account Financing Mode",
            "The account financing mode at the time of the daily financing.",
            "primitive",
            "account.AccountFinancingMode",
            False,
            None
        ),
        Property(
            "positionFinancings",
            "Per-Position Financing",
            "The financing paid/collected for each Position in the Account.",
            "array_object",
            "PositionFinancing",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(DailyFinancingTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('financing') is not None:
            body['financing'] = \
                data.get('financing')

        if data.get('accountBalance') is not None:
            body['accountBalance'] = \
                data.get('accountBalance')

        if data.get('accountFinancingMode') is not None:
            body['accountFinancingMode'] = \
                data.get('accountFinancingMode')

        if data.get('positionFinancings') is not None:
            body['positionFinancings'] = [
                PositionFinancing.from_dict(d)
                for d in data.get('positionFinancings')
            ]

        self = DailyFinancingTransaction(**body)

        return self


class ResetResettablePLTransaction(BaseEntity):
    _summary_format = "PL Reset"
    _name_format = "Transaction {id}"

    _properties = [
        Property(
            "id",
            "Transaction ID",
            "The Transaction's Identifier.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "Time",
            "The date/time when the Transaction was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "userID",
            "User ID",
            "The ID of the user that initiated the creation of the Transaction.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "accountID",
            "Account ID",
            "The ID of the Account the Transaction was created for.",
            "primitive",
            "account.AccountID",
            False,
            None
        ),
        Property(
            "batchID",
            "Transaction Batch ID",
            "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "type",
            "Type",
            "The Type of the Transaction. Always set to \"RESET_RESETTABLE_PL\" for a ResetResettablePLTransaction.",
            "primitive",
            "transaction.TransactionType",
            False,
            "RESET_RESETTABLE_PL"
        ),
    ]

    def __init__(self, **kwargs):
        super(ResetResettablePLTransaction, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('accountID') is not None:
            body['accountID'] = \
                data.get('accountID')

        if data.get('batchID') is not None:
            body['batchID'] = \
                data.get('batchID')

        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        self = ResetResettablePLTransaction(**body)

        return self


class ClientExtensions(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "id",
            "Client ID",
            "The Client ID of the Order/Trade",
            "primitive",
            "transaction.ClientID",
            False,
            None
        ),
        Property(
            "tag",
            "Tag",
            "A tag associated with the Order/Trade",
            "primitive",
            "transaction.ClientTag",
            False,
            None
        ),
        Property(
            "comment",
            "Comment",
            "A comment associated with the Order/Trade",
            "primitive",
            "transaction.ClientComment",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(ClientExtensions, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('id') is not None:
            body['id'] = \
                data.get('id')

        if data.get('tag') is not None:
            body['tag'] = \
                data.get('tag')

        if data.get('comment') is not None:
            body['comment'] = \
                data.get('comment')

        self = ClientExtensions(**body)

        return self


class TakeProfitDetails(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "price",
            "Price",
            "The price that the Take Profit Order will be triggered at.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time in force for the created Take Profit Order. This may only be GTC, GTD or GFD.",
            "primitive",
            "order.TimeInForce",
            False,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date when the Take Profit Order will be cancelled on if timeInForce is GTD.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The Client Extensions to add to the Take Profit Order when created.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TakeProfitDetails, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
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
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        self = TakeProfitDetails(**body)

        return self


class StopLossDetails(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "price",
            "Price",
            "The price that the Stop Loss Order will be triggered at.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time in force for the created Stop Loss Order. This may only be GTC, GTD or GFD.",
            "primitive",
            "order.TimeInForce",
            False,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date when the Stop Loss Order will be cancelled on if timeInForce is GTD.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The Client Extensions to add to the Stop Loss Order when created.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(StopLossDetails, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
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
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        self = StopLossDetails(**body)

        return self


class TrailingStopLossDetails(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "distance",
            "Trailing Price Distance",
            "The distance (in price units) from the Trade's fill price that the Trailing Stop Loss Order will be triggered at.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "timeInForce",
            "Time In Force",
            "The time in force for the created Trailing Stop Loss Order. This may only be GTC, GTD or GFD.",
            "primitive",
            "order.TimeInForce",
            False,
            "GTC"
        ),
        Property(
            "gtdTime",
            "GTD Time",
            "The date when the Trailing Stop Loss Order will be cancelled on if timeInForce is GTD.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The Client Extensions to add to the Trailing Stop Loss Order when created.",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TrailingStopLossDetails, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
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
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        self = TrailingStopLossDetails(**body)

        return self


class TradeOpen(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "tradeID",
            "Trade ID",
            "The ID of the Trade that was opened",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "units",
            "Amount",
            "The number of units opened by the Trade",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "clientExtensions",
            "Client Extensions",
            "The client extensions for the newly opened Trade",
            "object",
            "transaction.ClientExtensions",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TradeOpen, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('clientExtensions') is not None:
            body['clientExtensions'] = \
                ClientExtensions.from_dict(
                    data['clientExtensions']
                )

        self = TradeOpen(**body)

        return self


class TradeReduce(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "tradeID",
            "Trade ID",
            "The ID of the Trade that was reduced or closed",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "units",
            "Amount",
            "The number of units that the Trade was reduced by",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "realizedPL",
            "Profit/Loss",
            "The PL realized when reducing the Trade",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "financing",
            "Financing",
            "The financing paid/collected when reducing the Trade",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(TradeReduce, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('realizedPL') is not None:
            body['realizedPL'] = \
                data.get('realizedPL')

        if data.get('financing') is not None:
            body['financing'] = \
                data.get('financing')

        self = TradeReduce(**body)

        return self


class MarketOrderTradeClose(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "tradeID",
            "Trade ID",
            "The ID of the Trade requested to be closed",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "clientTradeID",
            "Client Trade ID",
            "The client ID of the Trade requested to be closed",
            "primitive",
            "string",
            False,
            None
        ),
        Property(
            "units",
            "Amount",
            "Indication of how much of the Trade to close. Either \"ALL\", or a DecimalNumber reflection a partial close of the Trade.",
            "primitive",
            "string",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarketOrderTradeClose, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('clientTradeID') is not None:
            body['clientTradeID'] = \
                data.get('clientTradeID')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        self = MarketOrderTradeClose(**body)

        return self


class MarketOrderMarginCloseout(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "reason",
            "Reason",
            "The reason the Market Order was created to perform a margin closeout",
            "primitive",
            "transaction.MarketOrderMarginCloseoutReason",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarketOrderMarginCloseout, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('reason') is not None:
            body['reason'] = \
                data.get('reason')

        self = MarketOrderMarginCloseout(**body)

        return self


class MarketOrderDelayedTradeClose(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "tradeID",
            "Trade ID",
            "The ID of the Trade being closed",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "clientTradeID",
            "Client Trade ID",
            "The Client ID of the Trade being closed",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "sourceTransactionID",
            "Source Transaction ID",
            "The Transaction ID of the DelayedTradeClosure transaction to which this Delayed Trade Close belongs to",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarketOrderDelayedTradeClose, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('clientTradeID') is not None:
            body['clientTradeID'] = \
                data.get('clientTradeID')

        if data.get('sourceTransactionID') is not None:
            body['sourceTransactionID'] = \
                data.get('sourceTransactionID')

        self = MarketOrderDelayedTradeClose(**body)

        return self


class MarketOrderPositionCloseout(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "instrument",
            "Instrument",
            "The instrument of the Position being closed out.",
            "primitive",
            "primitives.InstrumentName",
            False,
            None
        ),
        Property(
            "units",
            "Amount",
            "Indication of how much of the Position to close. Either \"ALL\", or a DecimalNumber reflection a partial close of the Trade. The DecimalNumber must always be positive, and represent a number that doesn't exceed the absolute size of the Position.",
            "primitive",
            "string",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(MarketOrderPositionCloseout, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        self = MarketOrderPositionCloseout(**body)

        return self


class VWAPReceipt(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "units",
            "Fill Amount",
            "The number of units filled",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "price",
            "Fill Price",
            "The price at which the units were filled",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(VWAPReceipt, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('price') is not None:
            body['price'] = \
                data.get('price')

        self = VWAPReceipt(**body)

        return self


class LiquidityRegenerationSchedule(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "steps",
            "Steps",
            "The steps in the Liquidity Regeneration Schedule",
            "array_object",
            "LiquidityRegenerationScheduleStep",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(LiquidityRegenerationSchedule, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('steps') is not None:
            body['steps'] = [
                LiquidityRegenerationScheduleStep.from_dict(d)
                for d in data.get('steps')
            ]

        self = LiquidityRegenerationSchedule(**body)

        return self


class LiquidityRegenerationScheduleStep(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "timestamp",
            "Time",
            "The timestamp of the schedule step.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
        Property(
            "bidLiquidityUsed",
            "Bid Liquidity Used",
            "The amount of bid liquidity used at this step in the schedule.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "askLiquidityUsed",
            "Ask Liquidity Used",
            "The amount of ask liquidity used at this step in the schedule.",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(LiquidityRegenerationScheduleStep, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('timestamp') is not None:
            body['timestamp'] = \
                data.get('timestamp')

        if data.get('bidLiquidityUsed') is not None:
            body['bidLiquidityUsed'] = \
                data.get('bidLiquidityUsed')

        if data.get('askLiquidityUsed') is not None:
            body['askLiquidityUsed'] = \
                data.get('askLiquidityUsed')

        self = LiquidityRegenerationScheduleStep(**body)

        return self


class OpenTradeFinancing(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "tradeID",
            "tradeID",
            "The ID of the Trade that financing is being paid/collected for.",
            "primitive",
            "trade.TradeID",
            False,
            None
        ),
        Property(
            "financing",
            "Financing",
            "The amount of financing paid/collected for the Trade.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(OpenTradeFinancing, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('tradeID') is not None:
            body['tradeID'] = \
                data.get('tradeID')

        if data.get('financing') is not None:
            body['financing'] = \
                data.get('financing')

        self = OpenTradeFinancing(**body)

        return self


class PositionFinancing(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "instrumentID",
            "Instrument",
            "The instrument of the Position that financing is being paid/collected for.",
            "primitive",
            "primitives.InstrumentName",
            False,
            None
        ),
        Property(
            "financing",
            "Financing",
            "The amount of financing paid/collected for the Position.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "openTradeFinancings",
            "Trade Financings",
            "The financing paid/collecte for each open Trade within the Position.",
            "array_object",
            "OpenTradeFinancing",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(PositionFinancing, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('instrumentID') is not None:
            body['instrumentID'] = \
                data.get('instrumentID')

        if data.get('financing') is not None:
            body['financing'] = \
                data.get('financing')

        if data.get('openTradeFinancings') is not None:
            body['openTradeFinancings'] = [
                OpenTradeFinancing.from_dict(d)
                for d in data.get('openTradeFinancings')
            ]

        self = PositionFinancing(**body)

        return self


class Heartbeat(BaseEntity):
    _summary_format = "Transaction Heartbeat {time}"
    _name_format = ""

    _properties = [
        Property(
            "type",
            "type",
            "The string \"HEARTBEAT\"",
            "primitive",
            "string",
            False,
            "HEARTBEAT"
        ),
        Property(
            "lastTransactionID",
            "lastTransactionID",
            "The ID of the most recent Transaction created for the Account",
            "primitive",
            "transaction.TransactionID",
            False,
            None
        ),
        Property(
            "time",
            "time",
            "The date/time when the Heartbeat was created.",
            "primitive",
            "primitives.DateTime",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(Heartbeat, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('type') is not None:
            body['type'] = \
                data.get('type')

        if data.get('lastTransactionID') is not None:
            body['lastTransactionID'] = \
                data.get('lastTransactionID')

        if data.get('time') is not None:
            body['time'] = \
                data.get('time')

        self = Heartbeat(**body)

        return self

class EntitySpec(object):
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
    VWAPReceipt = VWAPReceipt
    LiquidityRegenerationSchedule = LiquidityRegenerationSchedule
    LiquidityRegenerationScheduleStep = LiquidityRegenerationScheduleStep
    OpenTradeFinancing = OpenTradeFinancing
    PositionFinancing = PositionFinancing
    Heartbeat = Heartbeat

    def __init__(self, ctx):
        self.ctx = ctx


    def list(
        self,
        accountID,
        **kwargs
    ):
        """List Transactions

        Get a list of Transactions pages that satisfy a time-based Transaction
        query.

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch Transactions for.
        fromTime : , optional
            The starting time (inclusive) of the time range for the
            Transactions being queried.
        toTime : , optional
            The ending time (inclusive) of the time range for the Transactions
            being queried.
        pageSize : integer, optional
            The number of Transactions to include in each page of the results.
        type : array, optional
            A filter for restricting the types of Transactions to retreive.
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


        if str(response.status) == "416":
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
        transactionID,
        **kwargs
    ):
        """Transaction Details

        Get the details of a single Account Transaction.

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch a Transaction for.
        transactionID : 
            ID of the Transaction to fetch
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

        if str(response.status) == "200":
            if jbody.get('transaction') is not None:
                parsed_body['transaction'] = \
                    Transaction.from_dict(
                        jbody['transaction']
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


    def range(
        self,
        accountID,
        **kwargs
    ):
        """Transaction ID Range

        Get a range of Transactions for an Account based on the Transaction
        IDs.

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch a range of Transactions for.
        fromID : , optional
            The starting Transacion ID (inclusive) to fetch.
        toID : , optional
            The ending Transaction ID (inclusive) to fetch.
        type : array, optional
            The filter that restricts the types of Transactions to retreive.
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

        if str(response.status) == "200":
            if jbody.get('transactions') is not None:
                parsed_body['transactions'] = [
                    Transaction.from_dict(d)
                    for d in jbody.get('transactions')
                ]

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


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


        if str(response.status) == "416":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')


        response.body = parsed_body

        return response


    def since(
        self,
        accountID,
        **kwargs
    ):
        """Transactions Since ID

        Get a range of Transactions for an Account starting at (but not
        including) a provided Transaction ID.

        Parameters
        ----------
        accountID : 
            ID of the Account to Transactions for.
        id : , optional
            The ID of the last Transacion fetched. This query will return all
            Transactions newer than the TransactionID.
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

        if str(response.status) == "200":
            if jbody.get('transactions') is not None:
                parsed_body['transactions'] = [
                    Transaction.from_dict(d)
                    for d in jbody.get('transactions')
                ]

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


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


        if str(response.status) == "416":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')


        response.body = parsed_body

        return response


    def stream(
        self,
        accountID,
        **kwargs
    ):
        """Transaction Stream

        Get a stream of Transactions for an Account starting from when the
        request is made.

        Parameters
        ----------
        accountID : 
            ID of the Account to stream Transactions for
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
                j = json.loads(line)

                type = j.get("type")

                if type is None:
                    return ("unknown", j)
                elif type == "HEARTBEAT":
                    return (
                        "transaction.Heartbeat",
                        self.ctx.transaction.Heartbeat.from_dict(j)
                    )

                transaction = self.ctx.transaction.Transaction.from_dict(j)

                return (
                    "transaction.Transaction",
                    transaction
                )

                
        request.set_line_parser(
            Parser(self.ctx)
        )

        response = self.ctx.request(request)


        return response

