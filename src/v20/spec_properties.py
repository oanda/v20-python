from v20.base_entity import Property

"""
Following are the list of properties (metadata) for each complex type defined
by the v20 library.
"""

instrument_Candlestick = [
    Property(
        "time",
        "time",
        "The start time of the candlestick",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "bid",
        "bid",
        "The candlestick data based on bids. Only provided if bid-based candles were requested.",
        "object",
        "instrument.CandlestickData",
        None,
        None
    ),
    Property(
        "ask",
        "ask",
        "The candlestick data based on asks. Only provided if ask-based candles were requested.",
        "object",
        "instrument.CandlestickData",
        None,
        None
    ),
    Property(
        "mid",
        "mid",
        "The candlestick data based on midpoints. Only provided if midpoint-based candles were requested.",
        "object",
        "instrument.CandlestickData",
        None,
        None
    ),
    Property(
        "volume",
        "volume",
        "The number of prices created during the time-range represented by the candlestick.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "complete",
        "complete",
        "A flag indicating if the candlestick is complete. A complete candlestick is one whose ending time is not in the future.",
        "primitive",
        "boolean",
        None,
        None
    ),
]

instrument_CandlestickData = [
    Property(
        "o",
        "o",
        "The first (open) price in the time-range represented by the candlestick.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "h",
        "h",
        "The highest price in the time-range represented by the candlestick.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "l",
        "l",
        "The lowest price in the time-range represented by the candlestick.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "c",
        "c",
        "The last (closing) price in the time-range represented by the candlestick.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
]

instrument_OrderBook = [
    Property(
        "instrument",
        "instrument",
        "The order book's instrument",
        "primitive",
        "primitives.InstrumentName",
        None,
        None
    ),
    Property(
        "time",
        "time",
        "The time when the order book snapshot was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "price",
        "price",
        "The price (midpoint) for the order book's instrument at the time of the order book snapshot",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "bucketWidth",
        "bucketWidth",
        "The price width for each bucket. Each bucket covers the price range from the bucket's price to the bucket's price + bucketWidth.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "buckets",
        "buckets",
        "The partitioned order book, divided into buckets using a default bucket width. These buckets are only provided for price ranges which actually contain order or position data.",
        "array_object",
        "OrderBookBucket",
        None,
        None
    ),
]

instrument_OrderBookBucket = [
    Property(
        "price",
        "price",
        "The lowest price (inclusive) covered by the bucket. The bucket covers the price range from the price to price + the order book's bucketWidth.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "longCountPercent",
        "longCountPercent",
        "The percentage of the total number of orders represented by the long orders found in this bucket.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "shortCountPercent",
        "shortCountPercent",
        "The percentage of the total number of orders represented by the short orders found in this bucket.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
]

instrument_PositionBook = [
    Property(
        "instrument",
        "instrument",
        "The position book's instrument",
        "primitive",
        "primitives.InstrumentName",
        None,
        None
    ),
    Property(
        "time",
        "time",
        "The time when the position book snapshot was created",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "price",
        "price",
        "The price (midpoint) for the position book's instrument at the time of the position book snapshot",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "bucketWidth",
        "bucketWidth",
        "The price width for each bucket. Each bucket covers the price range from the bucket's price to the bucket's price + bucketWidth.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "buckets",
        "buckets",
        "The partitioned position book, divided into buckets using a default bucket width. These buckets are only provided for price ranges which actually contain order or position data.",
        "array_object",
        "PositionBookBucket",
        None,
        None
    ),
]

instrument_PositionBookBucket = [
    Property(
        "price",
        "price",
        "The lowest price (inclusive) covered by the bucket. The bucket covers the price range from the price to price + the position book's bucketWidth.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "longCountPercent",
        "longCountPercent",
        "The percentage of the total number of positions represented by the long positions found in this bucket.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "shortCountPercent",
        "shortCountPercent",
        "The percentage of the total number of positions represented by the short positions found in this bucket.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
]

position_Position = [
    Property(
        "instrument",
        "Instrument",
        "The Position's Instrument.",
        "primitive",
        "primitives.InstrumentName",
        None,
        None
    ),
    Property(
        "pl",
        "Profit/Loss",
        "Profit/loss realized by the Position over the lifetime of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "unrealizedPL",
        "Unrealized Profit/Loss",
        "The unrealized profit/loss of all open Trades that contribute to this Position.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginUsed",
        "Margin Used",
        "Margin currently used by the Position.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "resettablePL",
        "Resettable Profit/Loss",
        "Profit/loss realized by the Position since the Account's resettablePL was last reset by the client.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "financing",
        "Financing",
        "The total amount of financing paid/collected for this instrument over the lifetime of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "commission",
        "Commission",
        "The total amount of commission paid for this instrument over the lifetime of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "guaranteedExecutionFees",
        "Guranteed Execution Fee",
        "The total amount of fees charged over the lifetime of the Account for the execution of guaranteed Stop Loss Orders for this instrument.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "long",
        "Long Side",
        "The details of the long side of the Position.",
        "object",
        "position.PositionSide",
        None,
        None
    ),
    Property(
        "short",
        "Short Side",
        "The details of the short side of the Position.",
        "object",
        "position.PositionSide",
        None,
        None
    ),
]

position_PositionSide = [
    Property(
        "units",
        "Units",
        "Number of units in the position (negative value indicates short position, positive indicates long position).",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "averagePrice",
        "Average Price",
        "Volume-weighted average of the underlying Trade open prices for the Position.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "tradeIDs",
        "Trade IDs",
        "List of the open Trade IDs which contribute to the open Position.",
        "array_primitive",
        "TradeID",
        None,
        None
    ),
    Property(
        "pl",
        "Profit/Loss",
        "Profit/loss realized by the PositionSide over the lifetime of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "unrealizedPL",
        "Unrealized Profit/Loss",
        "The unrealized profit/loss of all open Trades that contribute to this PositionSide.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "resettablePL",
        "Resettable Profit/Loss",
        "Profit/loss realized by the PositionSide since the Account's resettablePL was last reset by the client.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "financing",
        "Financing",
        "The total amount of financing paid/collected for this PositionSide over the lifetime of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "guaranteedExecutionFees",
        "Guranteed Execution Fees",
        "The total amount of fees charged over the lifetime of the Account for the execution of guaranteed Stop Loss Orders attached to Trades for this PositionSide.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
]

position_CalculatedPositionState = [
    Property(
        "instrument",
        "Instrument",
        "The Position's Instrument.",
        "primitive",
        "primitives.InstrumentName",
        None,
        None
    ),
    Property(
        "netUnrealizedPL",
        "Net Unrealized Profit/Loss",
        "The Position's net unrealized profit/loss",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "longUnrealizedPL",
        "Long Unrealized Profit/Loss",
        "The unrealized profit/loss of the Position's long open Trades",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "shortUnrealizedPL",
        "Short Unrealized Profit/Loss",
        "The unrealized profit/loss of the Position's short open Trades",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginUsed",
        "Margin Used",
        "Margin currently used by the Position.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
]

trade_Trade = [
    Property(
        "id",
        "Trade ID",
        "The Trade's identifier, unique within the Trade's Account.",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "instrument",
        "Instrument",
        "The Trade's Instrument.",
        "primitive",
        "primitives.InstrumentName",
        None,
        None
    ),
    Property(
        "price",
        "Fill Price",
        "The execution price of the Trade.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "openTime",
        "Open Time",
        "The date/time when the Trade was opened.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "state",
        "State",
        "The current state of the Trade.",
        "primitive",
        "trade.TradeState",
        None,
        None
    ),
    Property(
        "initialUnits",
        "Initial Trade Units",
        "The initial size of the Trade. Negative values indicate a short Trade, and positive values indicate a long Trade.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "initialMarginRequired",
        "Initial Margin Required",
        "The margin required at the time the Trade was created. Note, this is the 'pure' margin required, it is not the 'effective' margin used that factors in the trade risk if a GSLO is attached to the trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "currentUnits",
        "Current Open Trade Units",
        "The number of units currently open for the Trade. This value is reduced to 0.0 as the Trade is closed.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "realizedPL",
        "Realized Profit/Loss",
        "The total profit/loss realized on the closed portion of the Trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "unrealizedPL",
        "Unrealized Profit/Loss",
        "The unrealized profit/loss on the open portion of the Trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginUsed",
        "Margin Used",
        "Margin currently used by the Trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "averageClosePrice",
        "Average Close Price",
        "The average closing price of the Trade. Only present if the Trade has been closed or reduced at least once.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "closingTransactionIDs",
        "Closing Transaction IDs",
        "The IDs of the Transactions that have closed portions of this Trade.",
        "array_primitive",
        "TransactionID",
        None,
        None
    ),
    Property(
        "financing",
        "Financing",
        "The financing paid/collected for this Trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "closeTime",
        "Close Time",
        "The date/time when the Trade was fully closed. Only provided for Trades whose state is CLOSED.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions of the Trade.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOrder",
        "Take Profit Order",
        "Full representation of the Trade's Take Profit Order, only provided if such an Order exists.",
        "object",
        "order.TakeProfitOrder",
        None,
        None
    ),
    Property(
        "stopLossOrder",
        "Stop Loss Order",
        "Full representation of the Trade's Stop Loss Order, only provided if such an Order exists.",
        "object",
        "order.StopLossOrder",
        None,
        None
    ),
    Property(
        "trailingStopLossOrder",
        "Trailing Stop Loss Order",
        "Full representation of the Trade's Trailing Stop Loss Order, only provided if such an Order exists.",
        "object",
        "order.TrailingStopLossOrder",
        None,
        None
    ),
]

trade_TradeSummary = [
    Property(
        "id",
        "Trade ID",
        "The Trade's identifier, unique within the Trade's Account.",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "instrument",
        "Instrument",
        "The Trade's Instrument.",
        "primitive",
        "primitives.InstrumentName",
        None,
        None
    ),
    Property(
        "price",
        "Fill Price",
        "The execution price of the Trade.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "openTime",
        "Open Time",
        "The date/time when the Trade was opened.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "state",
        "State",
        "The current state of the Trade.",
        "primitive",
        "trade.TradeState",
        None,
        None
    ),
    Property(
        "initialUnits",
        "Initial Trade Units",
        "The initial size of the Trade. Negative values indicate a short Trade, and positive values indicate a long Trade.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "initialMarginRequired",
        "Initial Margin Required",
        "The margin required at the time the Trade was created. Note, this is the 'pure' margin required, it is not the 'effective' margin used that factors in the trade risk if a GSLO is attached to the trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "currentUnits",
        "Current Open Trade Units",
        "The number of units currently open for the Trade. This value is reduced to 0.0 as the Trade is closed.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "realizedPL",
        "Realized Profit/Loss",
        "The total profit/loss realized on the closed portion of the Trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "unrealizedPL",
        "Unrealized Profit/Loss",
        "The unrealized profit/loss on the open portion of the Trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginUsed",
        "Margin Used",
        "Margin currently used by the Trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "averageClosePrice",
        "Average Close Price",
        "The average closing price of the Trade. Only present if the Trade has been closed or reduced at least once.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "closingTransactionIDs",
        "Closing Transaction IDs",
        "The IDs of the Transactions that have closed portions of this Trade.",
        "array_primitive",
        "TransactionID",
        None,
        None
    ),
    Property(
        "financing",
        "Financing",
        "The financing paid/collected for this Trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "closeTime",
        "Close Time",
        "The date/time when the Trade was fully closed. Only provided for Trades whose state is CLOSED.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions of the Trade.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOrderID",
        "Take Profit Order ID",
        "ID of the Trade's Take Profit Order, only provided if such an Order exists.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "stopLossOrderID",
        "Stop Loss Order ID",
        "ID of the Trade's Stop Loss Order, only provided if such an Order exists.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "trailingStopLossOrderID",
        "Trailing Stop Loss Order ID",
        "ID of the Trade's Trailing Stop Loss Order, only provided if such an Order exists.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
]

trade_CalculatedTradeState = [
    Property(
        "id",
        "Trade ID",
        "The Trade's ID.",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "unrealizedPL",
        "Trade UPL",
        "The Trade's unrealized profit/loss.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginUsed",
        "Margin Used",
        "Margin currently used by the Trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
]

site_MT4TransactionHeartbeat = [
    Property(
        "type",
        "type",
        "The string \"HEARTBEAT\"",
        "primitive",
        "string",
        None,
        "HEARTBEAT"
    ),
    Property(
        "time",
        "time",
        "The date/time when the TransactionHeartbeat was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
]

primitives_Instrument = [
    Property(
        "name",
        "name",
        "The name of the Instrument",
        "primitive",
        "primitives.InstrumentName",
        None,
        None
    ),
    Property(
        "type",
        "type",
        "The type of the Instrument",
        "primitive",
        "primitives.InstrumentType",
        None,
        None
    ),
    Property(
        "displayName",
        "displayName",
        "The display name of the Instrument",
        "primitive",
        "string",
        None,
        None
    ),
    Property(
        "pipLocation",
        "pipLocation",
        "The location of the \"pip\" for this instrument. The decimal position of the pip in this Instrument's price can be found at 10 ^ pipLocation (e.g. -4 pipLocation results in a decimal pip position of 10 ^ -4 = 0.0001).",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "displayPrecision",
        "displayPrecision",
        "The number of decimal places that should be used to display prices for this instrument. (e.g. a displayPrecision of 5 would result in a price of \"1\" being displayed as \"1.00000\")",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "tradeUnitsPrecision",
        "tradeUnitsPrecision",
        "The amount of decimal places that may be provided when specifying the number of units traded for this instrument.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "minimumTradeSize",
        "minimumTradeSize",
        "The smallest number of units allowed to be traded for this instrument.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "maximumTrailingStopDistance",
        "maximumTrailingStopDistance",
        "The maximum trailing stop distance allowed for a trailing stop loss created for this instrument. Specified in price units.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "minimumTrailingStopDistance",
        "minimumTrailingStopDistance",
        "The minimum trailing stop distance allowed for a trailing stop loss created for this instrument. Specified in price units.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "maximumPositionSize",
        "maximumPositionSize",
        "The maximum position size allowed for this instrument. Specified in units.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "maximumOrderUnits",
        "maximumOrderUnits",
        "The maximum units allowed for an Order placed for this instrument. Specified in units.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "marginRate",
        "marginRate",
        "The margin rate for this instrument.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "commission",
        "commission",
        "The commission structure for this instrument.",
        "object",
        "primitives.InstrumentCommission",
        None,
        None
    ),
]

primitives_InstrumentCommission = [
    Property(
        "commission",
        "commission",
        "The commission amount (in the Account's home currency) charged per unitsTraded of the instrument",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "unitsTraded",
        "unitsTraded",
        "The number of units traded that the commission amount is based on.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "minimumCommission",
        "minimumCommission",
        "The minimum commission amount (in the Account's home currency) that is charged when an Order is filled for this instrument.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
]

primitives_GuaranteedStopLossOrderLevelRestriction = [
    Property(
        "volume",
        "volume",
        "Applies to Trades with a guaranteed Stop Loss Order attached for the specified Instrument. This is the total allowed Trade volume that can exist within the priceRange based on the trigger prices of the guaranteed Stop Loss Orders.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "priceRange",
        "priceRange",
        "The price range the volume applies to. This value is in price units.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
]

account_Account = [
    Property(
        "id",
        "Account ID",
        "The Account's identifier",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "alias",
        "Alias",
        "Client-assigned alias for the Account. Only provided if the Account has an alias set",
        "primitive",
        "string",
        None,
        None
    ),
    Property(
        "currency",
        "Home Currency",
        "The home currency of the Account",
        "primitive",
        "primitives.Currency",
        None,
        None
    ),
    Property(
        "balance",
        "Balance",
        "The current balance of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "createdByUserID",
        "Created by User ID",
        "ID of the user that created the Account.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "createdTime",
        "Create Time",
        "The date/time when the Account was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "guaranteedStopLossOrderMode",
        "Guaranteed Stop Loss Order Mode",
        "The current guaranteed Stop Loss Order mode of the Account.",
        "primitive",
        "account.GuaranteedStopLossOrderMode",
        None,
        None
    ),
    Property(
        "pl",
        "Profit/Loss",
        "The total profit/loss realized over the lifetime of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "resettablePL",
        "Resettable Profit/Loss",
        "The total realized profit/loss for the Account since it was last reset by the client.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "resettablePLTime",
        "Profit/Loss Reset Time",
        "The date/time that the Account's resettablePL was last reset.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "financing",
        "Financing",
        "The total amount of financing paid/collected over the lifetime of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "commission",
        "Commission",
        "The total amount of commission paid over the lifetime of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "guaranteedExecutionFees",
        "Guaranteed Execution Fees",
        "The total amount of fees charged over the lifetime of the Account for the execution of guaranteed Stop Loss Orders.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginRate",
        "Margin Rate",
        "Client-provided margin rate override for the Account. The effective margin rate of the Account is the lesser of this value and the OANDA margin rate for the Account's division. This value is only provided if a margin rate override exists for the Account.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "marginCallEnterTime",
        "Margin Call Enter Time",
        "The date/time when the Account entered a margin call state. Only provided if the Account is in a margin call.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "marginCallExtensionCount",
        "Margin Call Extension Count",
        "The number of times that the Account's current margin call was extended.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "lastMarginCallExtensionTime",
        "Last Margin Call Extension Time",
        "The date/time of the Account's last margin call extension.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "openTradeCount",
        "Open Trade Count",
        "The number of Trades currently open in the Account.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "openPositionCount",
        "Open Position Count",
        "The number of Positions currently open in the Account.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "pendingOrderCount",
        "Pending Order Count",
        "The number of Orders currently pending in the Account.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "hedgingEnabled",
        "Hedging Enabled",
        "Flag indicating that the Account has hedging enabled.",
        "primitive",
        "boolean",
        None,
        None
    ),
    Property(
        "lastOrderFillTimestamp",
        "Last Order Fill timestamp.",
        "The date/time of the last order that was filled for this account.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "unrealizedPL",
        "Unrealized Profit/Loss",
        "The total unrealized profit/loss for all Trades currently open in the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "NAV",
        "Net Asset Value",
        "The net asset value of the Account. Equal to Account balance + unrealizedPL.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginUsed",
        "Margin Used",
        "Margin currently used for the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginAvailable",
        "Margin Available",
        "Margin available for Account currency.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "positionValue",
        "Position Value",
        "The value of the Account's open positions represented in the Account's home currency.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutUnrealizedPL",
        "Closeout UPL",
        "The Account's margin closeout unrealized PL.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutNAV",
        "Closeout NAV",
        "The Account's margin closeout NAV.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutMarginUsed",
        "Closeout Margin Used",
        "The Account's margin closeout margin used.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutPercent",
        "Margin Closeout Percentage",
        "The Account's margin closeout percentage. When this value is 1.0 or above the Account is in a margin closeout situation.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "marginCloseoutPositionValue",
        "Margin Closeout Position Value",
        "The value of the Account's open positions as used for margin closeout calculations represented in the Account's home currency.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "withdrawalLimit",
        "Withdrawal Limit",
        "The current WithdrawalLimit for the account which will be zero or a positive value indicating how much can be withdrawn from the account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCallMarginUsed",
        "Margin Call Margin Used",
        "The Account's margin call margin used.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCallPercent",
        "Margin Call Percentage",
        "The Account's margin call percentage. When this value is 1.0 or above the Account is in a margin call situation.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "lastTransactionID",
        "Last Transaction ID",
        "The ID of the last Transaction created for the Account.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "trades",
        "Open Trades",
        "The details of the Trades currently open in the Account.",
        "array_object",
        "TradeSummary",
        None,
        None
    ),
    Property(
        "positions",
        "Positions",
        "The details all Account Positions.",
        "array_object",
        "Position",
        None,
        None
    ),
    Property(
        "orders",
        "Pending Orders",
        "The details of the Orders currently pending in the Account.",
        "array_object",
        "Order",
        None,
        None
    ),
]

account_AccountChangesState = [
    Property(
        "unrealizedPL",
        "Unrealized Profit/Loss",
        "The total unrealized profit/loss for all Trades currently open in the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "NAV",
        "Net Asset Value",
        "The net asset value of the Account. Equal to Account balance + unrealizedPL.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginUsed",
        "Margin Used",
        "Margin currently used for the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginAvailable",
        "Margin Available",
        "Margin available for Account currency.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "positionValue",
        "Position Value",
        "The value of the Account's open positions represented in the Account's home currency.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutUnrealizedPL",
        "Closeout UPL",
        "The Account's margin closeout unrealized PL.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutNAV",
        "Closeout NAV",
        "The Account's margin closeout NAV.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutMarginUsed",
        "Closeout Margin Used",
        "The Account's margin closeout margin used.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutPercent",
        "Margin Closeout Percentage",
        "The Account's margin closeout percentage. When this value is 1.0 or above the Account is in a margin closeout situation.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "marginCloseoutPositionValue",
        "Margin Closeout Position Value",
        "The value of the Account's open positions as used for margin closeout calculations represented in the Account's home currency.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "withdrawalLimit",
        "Withdrawal Limit",
        "The current WithdrawalLimit for the account which will be zero or a positive value indicating how much can be withdrawn from the account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCallMarginUsed",
        "Margin Call Margin Used",
        "The Account's margin call margin used.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCallPercent",
        "Margin Call Percentage",
        "The Account's margin call percentage. When this value is 1.0 or above the Account is in a margin call situation.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "orders",
        "Order States",
        "The price-dependent state of each pending Order in the Account.",
        "array_object",
        "DynamicOrderState",
        None,
        None
    ),
    Property(
        "trades",
        "Trade States",
        "The price-dependent state for each open Trade in the Account.",
        "array_object",
        "CalculatedTradeState",
        None,
        None
    ),
    Property(
        "positions",
        "Position States",
        "The price-dependent state for each open Position in the Account.",
        "array_object",
        "CalculatedPositionState",
        None,
        None
    ),
]

account_AccountProperties = [
    Property(
        "id",
        "ID",
        "The Account's identifier",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "mt4AccountID",
        "MT4 Account ID",
        "The Account's associated MT4 Account ID. This field will not be present if the Account is not an MT4 account.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "tags",
        "Account Tags",
        "The Account's tags",
        "array_primitive",
        "string",
        None,
        None
    ),
]

account_AccountSummary = [
    Property(
        "id",
        "Account ID",
        "The Account's identifier",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "alias",
        "Alias",
        "Client-assigned alias for the Account. Only provided if the Account has an alias set",
        "primitive",
        "string",
        None,
        None
    ),
    Property(
        "currency",
        "Home Currency",
        "The home currency of the Account",
        "primitive",
        "primitives.Currency",
        None,
        None
    ),
    Property(
        "balance",
        "Balance",
        "The current balance of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "createdByUserID",
        "Created by User ID",
        "ID of the user that created the Account.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "createdTime",
        "Create Time",
        "The date/time when the Account was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "guaranteedStopLossOrderMode",
        "Guaranteed Stop Loss Order Mode",
        "The current guaranteed Stop Loss Order mode of the Account.",
        "primitive",
        "account.GuaranteedStopLossOrderMode",
        None,
        None
    ),
    Property(
        "pl",
        "Profit/Loss",
        "The total profit/loss realized over the lifetime of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "resettablePL",
        "Resettable Profit/Loss",
        "The total realized profit/loss for the Account since it was last reset by the client.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "resettablePLTime",
        "Profit/Loss Reset Time",
        "The date/time that the Account's resettablePL was last reset.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "financing",
        "Financing",
        "The total amount of financing paid/collected over the lifetime of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "commission",
        "Commission",
        "The total amount of commission paid over the lifetime of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "guaranteedExecutionFees",
        "Guaranteed Execution Fees",
        "The total amount of fees charged over the lifetime of the Account for the execution of guaranteed Stop Loss Orders.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginRate",
        "Margin Rate",
        "Client-provided margin rate override for the Account. The effective margin rate of the Account is the lesser of this value and the OANDA margin rate for the Account's division. This value is only provided if a margin rate override exists for the Account.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "marginCallEnterTime",
        "Margin Call Enter Time",
        "The date/time when the Account entered a margin call state. Only provided if the Account is in a margin call.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "marginCallExtensionCount",
        "Margin Call Extension Count",
        "The number of times that the Account's current margin call was extended.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "lastMarginCallExtensionTime",
        "Last Margin Call Extension Time",
        "The date/time of the Account's last margin call extension.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "openTradeCount",
        "Open Trade Count",
        "The number of Trades currently open in the Account.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "openPositionCount",
        "Open Position Count",
        "The number of Positions currently open in the Account.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "pendingOrderCount",
        "Pending Order Count",
        "The number of Orders currently pending in the Account.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "hedgingEnabled",
        "Hedging Enabled",
        "Flag indicating that the Account has hedging enabled.",
        "primitive",
        "boolean",
        None,
        None
    ),
    Property(
        "lastOrderFillTimestamp",
        "Last Order Fill timestamp.",
        "The date/time of the last order that was filled for this account.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "unrealizedPL",
        "Unrealized Profit/Loss",
        "The total unrealized profit/loss for all Trades currently open in the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "NAV",
        "Net Asset Value",
        "The net asset value of the Account. Equal to Account balance + unrealizedPL.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginUsed",
        "Margin Used",
        "Margin currently used for the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginAvailable",
        "Margin Available",
        "Margin available for Account currency.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "positionValue",
        "Position Value",
        "The value of the Account's open positions represented in the Account's home currency.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutUnrealizedPL",
        "Closeout UPL",
        "The Account's margin closeout unrealized PL.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutNAV",
        "Closeout NAV",
        "The Account's margin closeout NAV.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutMarginUsed",
        "Closeout Margin Used",
        "The Account's margin closeout margin used.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutPercent",
        "Margin Closeout Percentage",
        "The Account's margin closeout percentage. When this value is 1.0 or above the Account is in a margin closeout situation.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "marginCloseoutPositionValue",
        "Margin Closeout Position Value",
        "The value of the Account's open positions as used for margin closeout calculations represented in the Account's home currency.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "withdrawalLimit",
        "Withdrawal Limit",
        "The current WithdrawalLimit for the account which will be zero or a positive value indicating how much can be withdrawn from the account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCallMarginUsed",
        "Margin Call Margin Used",
        "The Account's margin call margin used.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCallPercent",
        "Margin Call Percentage",
        "The Account's margin call percentage. When this value is 1.0 or above the Account is in a margin call situation.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "lastTransactionID",
        "Last Transaction ID",
        "The ID of the last Transaction created for the Account.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
]

account_CalculatedAccountState = [
    Property(
        "unrealizedPL",
        "Unrealized Profit/Loss",
        "The total unrealized profit/loss for all Trades currently open in the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "NAV",
        "Net Asset Value",
        "The net asset value of the Account. Equal to Account balance + unrealizedPL.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginUsed",
        "Margin Used",
        "Margin currently used for the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginAvailable",
        "Margin Available",
        "Margin available for Account currency.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "positionValue",
        "Position Value",
        "The value of the Account's open positions represented in the Account's home currency.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutUnrealizedPL",
        "Closeout UPL",
        "The Account's margin closeout unrealized PL.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutNAV",
        "Closeout NAV",
        "The Account's margin closeout NAV.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutMarginUsed",
        "Closeout Margin Used",
        "The Account's margin closeout margin used.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCloseoutPercent",
        "Margin Closeout Percentage",
        "The Account's margin closeout percentage. When this value is 1.0 or above the Account is in a margin closeout situation.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "marginCloseoutPositionValue",
        "Margin Closeout Position Value",
        "The value of the Account's open positions as used for margin closeout calculations represented in the Account's home currency.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "withdrawalLimit",
        "Withdrawal Limit",
        "The current WithdrawalLimit for the account which will be zero or a positive value indicating how much can be withdrawn from the account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCallMarginUsed",
        "Margin Call Margin Used",
        "The Account's margin call margin used.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "marginCallPercent",
        "Margin Call Percentage",
        "The Account's margin call percentage. When this value is 1.0 or above the Account is in a margin call situation.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
]

account_AccountChanges = [
    Property(
        "ordersCreated",
        "Orders Created",
        "The Orders created. These Orders may have been filled, cancelled or triggered in the same period.",
        "array_object",
        "Order",
        None,
        None
    ),
    Property(
        "ordersCancelled",
        "Orders Cancelled",
        "The Orders cancelled.",
        "array_object",
        "Order",
        None,
        None
    ),
    Property(
        "ordersFilled",
        "Orders Filled",
        "The Orders filled.",
        "array_object",
        "Order",
        None,
        None
    ),
    Property(
        "ordersTriggered",
        "Orders Triggered",
        "The Orders triggered.",
        "array_object",
        "Order",
        None,
        None
    ),
    Property(
        "tradesOpened",
        "Trades Opened",
        "The Trades opened.",
        "array_object",
        "TradeSummary",
        None,
        None
    ),
    Property(
        "tradesReduced",
        "Trades Reduced",
        "The Trades reduced.",
        "array_object",
        "TradeSummary",
        None,
        None
    ),
    Property(
        "tradesClosed",
        "Trades Closed",
        "The Trades closed.",
        "array_object",
        "TradeSummary",
        None,
        None
    ),
    Property(
        "positions",
        "Positions",
        "The Positions changed.",
        "array_object",
        "Position",
        None,
        None
    ),
    Property(
        "transactions",
        "Transactions",
        "The Transactions that have been generated.",
        "array_object",
        "Transaction",
        None,
        None
    ),
]

transaction_Transaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
]

transaction_CreateTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"CREATE\" in a CreateTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "CREATE"
    ),
    Property(
        "divisionID",
        "Division ID",
        "The ID of the Division that the Account is in",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "siteID",
        "Site ID",
        "The ID of the Site that the Account was created at",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountUserID",
        "Account User ID",
        "The ID of the user that the Account was created for",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountNumber",
        "Account Number",
        "The number of the Account within the site/division/user",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "homeCurrency",
        "Home Currency",
        "The home currency of the Account",
        "primitive",
        "primitives.Currency",
        None,
        None
    ),
]

transaction_CloseTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"CLOSE\" in a CloseTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "CLOSE"
    ),
]

transaction_ReopenTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"REOPEN\" in a ReopenTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "REOPEN"
    ),
]

transaction_ClientConfigureTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"CLIENT_CONFIGURE\" in a ClientConfigureTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "CLIENT_CONFIGURE"
    ),
    Property(
        "alias",
        "Account Alias",
        "The client-provided alias for the Account.",
        "primitive",
        "string",
        None,
        None
    ),
    Property(
        "marginRate",
        "Margin Rate",
        "The margin rate override for the Account.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
]

transaction_ClientConfigureRejectTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"CLIENT_CONFIGURE_REJECT\" in a ClientConfigureRejectTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "CLIENT_CONFIGURE_REJECT"
    ),
    Property(
        "alias",
        "Account Alias",
        "The client-provided alias for the Account.",
        "primitive",
        "string",
        None,
        None
    ),
    Property(
        "marginRate",
        "Margin Rate",
        "The margin rate override for the Account.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "rejectReason",
        "Reject Reason",
        "The reason that the Reject Transaction was created",
        "primitive",
        "transaction.TransactionRejectReason",
        None,
        None
    ),
]

transaction_TransferFundsTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"TRANSFER_FUNDS\" in a TransferFundsTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "TRANSFER_FUNDS"
    ),
    Property(
        "amount",
        "Transfer Amount",
        "The amount to deposit/withdraw from the Account in the Account's home currency. A positive value indicates a deposit, a negative value indicates a withdrawal.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "fundingReason",
        "Reason",
        "The reason that an Account is being funded.",
        "primitive",
        "transaction.FundingReason",
        None,
        None
    ),
    Property(
        "comment",
        "Comment",
        "An optional comment that may be attached to a fund transfer for audit purposes",
        "primitive",
        "string",
        None,
        None
    ),
    Property(
        "accountBalance",
        "Account Balance",
        "The Account's balance after funds are transferred.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
]

transaction_TransferFundsRejectTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"TRANSFER_FUNDS_REJECT\" in a TransferFundsRejectTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "TRANSFER_FUNDS_REJECT"
    ),
    Property(
        "amount",
        "Transfer Amount",
        "The amount to deposit/withdraw from the Account in the Account's home currency. A positive value indicates a deposit, a negative value indicates a withdrawal.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "fundingReason",
        "Reason",
        "The reason that an Account is being funded.",
        "primitive",
        "transaction.FundingReason",
        None,
        None
    ),
    Property(
        "comment",
        "Comment",
        "An optional comment that may be attached to a fund transfer for audit purposes",
        "primitive",
        "string",
        None,
        None
    ),
    Property(
        "rejectReason",
        "Reject Reason",
        "The reason that the Reject Transaction was created",
        "primitive",
        "transaction.TransactionRejectReason",
        None,
        None
    ),
]

transaction_MarketOrderTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"MARKET_ORDER\" in a MarketOrderTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        "pricing_common.PriceValue",
        None,
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
        None,
        None
    ),
    Property(
        "longPositionCloseout",
        "Long Position Close Details",
        "Details of the long Position requested to be closed out, only provided when a Market Order is being used to explicitly closeout a long Position.",
        "object",
        "transaction.MarketOrderPositionCloseout",
        None,
        None
    ),
    Property(
        "shortPositionCloseout",
        "Short Position Close Details",
        "Details of the short Position requested to be closed out, only provided when a Market Order is being used to explicitly closeout a short Position.",
        "object",
        "transaction.MarketOrderPositionCloseout",
        None,
        None
    ),
    Property(
        "marginCloseout",
        "Margin Closeout Details",
        "Details of the Margin Closeout that this Market Order was created for",
        "object",
        "transaction.MarketOrderMarginCloseout",
        None,
        None
    ),
    Property(
        "delayedTradeClose",
        "Delayed Trade Close Details",
        "Details of the delayed Trade close that this Market Order was created for",
        "object",
        "transaction.MarketOrderDelayedTradeClose",
        None,
        None
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Market Order was created",
        "primitive",
        "transaction.MarketOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

transaction_MarketOrderRejectTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"MARKET_ORDER_REJECT\" in a MarketOrderRejectTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        "pricing_common.PriceValue",
        None,
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
        None,
        None
    ),
    Property(
        "longPositionCloseout",
        "Long Position Close Details",
        "Details of the long Position requested to be closed out, only provided when a Market Order is being used to explicitly closeout a long Position.",
        "object",
        "transaction.MarketOrderPositionCloseout",
        None,
        None
    ),
    Property(
        "shortPositionCloseout",
        "Short Position Close Details",
        "Details of the short Position requested to be closed out, only provided when a Market Order is being used to explicitly closeout a short Position.",
        "object",
        "transaction.MarketOrderPositionCloseout",
        None,
        None
    ),
    Property(
        "marginCloseout",
        "Margin Closeout Details",
        "Details of the Margin Closeout that this Market Order was created for",
        "object",
        "transaction.MarketOrderMarginCloseout",
        None,
        None
    ),
    Property(
        "delayedTradeClose",
        "Delayed Trade Close Details",
        "Details of the delayed Trade close that this Market Order was created for",
        "object",
        "transaction.MarketOrderDelayedTradeClose",
        None,
        None
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Market Order was created",
        "primitive",
        "transaction.MarketOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "rejectReason",
        "Reject Reason",
        "The reason that the Reject Transaction was created",
        "primitive",
        "transaction.TransactionRejectReason",
        None,
        None
    ),
]

transaction_FixedPriceOrderTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"FIXED_PRICE_ORDER\" in a FixedPriceOrderTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "FIXED_PRICE_ORDER"
    ),
    Property(
        "instrument",
        "Instrument",
        "The Fixed Price Order's Instrument.",
        "primitive",
        "primitives.InstrumentName",
        True,
        None
    ),
    Property(
        "units",
        "Amount",
        "The quantity requested to be filled by the Fixed Price Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.",
        "primitive",
        "primitives.DecimalNumber",
        True,
        None
    ),
    Property(
        "price",
        "Price",
        "The price specified for the Fixed Price Order. This price is the exact price that the Fixed Price Order will be filled at.",
        "primitive",
        "pricing_common.PriceValue",
        True,
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
        "tradeState",
        "TradeState",
        "The state that the trade resulting from the Fixed Price Order should be set to.",
        "primitive",
        "string",
        True,
        None
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Fixed Price Order was created",
        "primitive",
        "transaction.FixedPriceOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions for the Fixed Price Order.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

transaction_LimitOrderTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"LIMIT_ORDER\" in a LimitOrderTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        "pricing_common.PriceValue",
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
        None,
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
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Limit Order was initiated",
        "primitive",
        "transaction.LimitOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "replacesOrderID",
        "Replaces Order ID",
        "The ID of the Order that this Order replaces (only provided if this Order replaces an existing Order).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Replaces Order Cancel Transaction ID",
        "The ID of the Transaction that cancels the replaced Order (only provided if this Order replaces an existing Order).",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
]

transaction_LimitOrderRejectTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"LIMIT_ORDER_REJECT\" in a LimitOrderRejectTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        "pricing_common.PriceValue",
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
        None,
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
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Limit Order was initiated",
        "primitive",
        "transaction.LimitOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "intendedReplacesOrderID",
        "Order ID to Replace",
        "The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "rejectReason",
        "Reject Reason",
        "The reason that the Reject Transaction was created",
        "primitive",
        "transaction.TransactionRejectReason",
        None,
        None
    ),
]

transaction_StopOrderTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"STOP_ORDER\" in a StopOrderTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        "pricing_common.PriceValue",
        True,
        None
    ),
    Property(
        "priceBound",
        "Price Bound",
        "The worst market price that may be used to fill this Stop Order. If the market gaps and crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.",
        "primitive",
        "pricing_common.PriceValue",
        None,
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
        None,
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
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Stop Order was initiated",
        "primitive",
        "transaction.StopOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "replacesOrderID",
        "Replaces Order ID",
        "The ID of the Order that this Order replaces (only provided if this Order replaces an existing Order).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Replaces Order Cancel Transaction ID",
        "The ID of the Transaction that cancels the replaced Order (only provided if this Order replaces an existing Order).",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
]

transaction_StopOrderRejectTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"STOP_ORDER_REJECT\" in a StopOrderRejectTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        "pricing_common.PriceValue",
        True,
        None
    ),
    Property(
        "priceBound",
        "Price Bound",
        "The worst market price that may be used to fill this Stop Order. If the market gaps and crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.",
        "primitive",
        "pricing_common.PriceValue",
        None,
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
        None,
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
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Stop Order was initiated",
        "primitive",
        "transaction.StopOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "intendedReplacesOrderID",
        "Order ID to Replace",
        "The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "rejectReason",
        "Reject Reason",
        "The reason that the Reject Transaction was created",
        "primitive",
        "transaction.TransactionRejectReason",
        None,
        None
    ),
]

transaction_MarketIfTouchedOrderTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"MARKET_IF_TOUCHED_ORDER\" in a MarketIfTouchedOrderTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        "pricing_common.PriceValue",
        True,
        None
    ),
    Property(
        "priceBound",
        "Price Value",
        "The worst market price that may be used to fill this MarketIfTouched Order.",
        "primitive",
        "pricing_common.PriceValue",
        None,
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
        None,
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
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Market-if-touched Order was initiated",
        "primitive",
        "transaction.MarketIfTouchedOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "replacesOrderID",
        "Replaces Order ID",
        "The ID of the Order that this Order replaces (only provided if this Order replaces an existing Order).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Replaces Order Cancel Transaction ID",
        "The ID of the Transaction that cancels the replaced Order (only provided if this Order replaces an existing Order).",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
]

transaction_MarketIfTouchedOrderRejectTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"MARKET_IF_TOUCHED_ORDER_REJECT\" in a MarketIfTouchedOrderRejectTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        "pricing_common.PriceValue",
        True,
        None
    ),
    Property(
        "priceBound",
        "Price Value",
        "The worst market price that may be used to fill this MarketIfTouched Order.",
        "primitive",
        "pricing_common.PriceValue",
        None,
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
        None,
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
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Market-if-touched Order was initiated",
        "primitive",
        "transaction.MarketIfTouchedOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "The specification of the Take Profit Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "The specification of the Stop Loss Order that should be created for a Trade opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "The specification of the Trailing Stop Loss Order that should be created for a Trade that is opened when the Order is filled (if such a Trade is created).",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created).  Do not set, modify, delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "intendedReplacesOrderID",
        "Order ID to Replace",
        "The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "rejectReason",
        "Reject Reason",
        "The reason that the Reject Transaction was created",
        "primitive",
        "transaction.TransactionRejectReason",
        None,
        None
    ),
]

transaction_TakeProfitOrderTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"TAKE_PROFIT_ORDER\" in a TakeProfitOrderTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        None,
        None
    ),
    Property(
        "price",
        "Price",
        "The price threshold specified for the TakeProfit Order. The associated Trade will be closed by a market price that is equal to or better than this threshold.",
        "primitive",
        "pricing_common.PriceValue",
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
        None,
        None
    ),
    Property(
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Take Profit Order was initiated",
        "primitive",
        "transaction.TakeProfitOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "orderFillTransactionID",
        "Order Fill Transaction ID",
        "The ID of the OrderFill Transaction that caused this Order to be created (only provided if this Order was created automatically when another Order was filled).",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "replacesOrderID",
        "Replaces Order ID",
        "The ID of the Order that this Order replaces (only provided if this Order replaces an existing Order).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Replaces Order Cancel Transaction ID",
        "The ID of the Transaction that cancels the replaced Order (only provided if this Order replaces an existing Order).",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
]

transaction_TakeProfitOrderRejectTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"TAKE_PROFIT_ORDER_REJECT\" in a TakeProfitOrderRejectTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        None,
        None
    ),
    Property(
        "price",
        "Price",
        "The price threshold specified for the TakeProfit Order. The associated Trade will be closed by a market price that is equal to or better than this threshold.",
        "primitive",
        "pricing_common.PriceValue",
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
        None,
        None
    ),
    Property(
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Take Profit Order was initiated",
        "primitive",
        "transaction.TakeProfitOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "orderFillTransactionID",
        "Order Fill Transaction ID",
        "The ID of the OrderFill Transaction that caused this Order to be created (only provided if this Order was created automatically when another Order was filled).",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "intendedReplacesOrderID",
        "Order ID to Replace",
        "The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "rejectReason",
        "Reject Reason",
        "The reason that the Reject Transaction was created",
        "primitive",
        "transaction.TransactionRejectReason",
        None,
        None
    ),
]

transaction_StopLossOrderTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"STOP_LOSS_ORDER\" in a StopLossOrderTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        None,
        None
    ),
    Property(
        "price",
        "Price",
        "The price threshold specified for the Stop Loss Order. If the guaranteed flag is false, the associated Trade will be closed by a market price that is equal to or worse than this threshold. If the flag is true the associated Trade will be closed at this price.",
        "primitive",
        "pricing_common.PriceValue",
        True,
        None
    ),
    Property(
        "distance",
        "Price Distance",
        "Specifies the distance (in price units) from the Account's current price to use as the Stop Loss Order price. If the Trade is short the Instrument's bid price is used, and for long Trades the ask is used.",
        "primitive",
        "primitives.DecimalNumber",
        None,
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
        None,
        None
    ),
    Property(
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "guaranteed",
        "Guaranteed",
        "Flag indicating that the Stop Loss Order is guaranteed. The default value depends on the GuaranteedStopLossOrderMode of the account, if it is REQUIRED, the default will be true, for DISABLED or ENABLED the default is false.",
        "primitive",
        "boolean",
        None,
        None
    ),
    Property(
        "guaranteedExecutionPremium",
        "Guaranteed Execution Premium",
        "The fee that will be charged if the Stop Loss Order is guaranteed and the Order is filled at the guaranteed price. The value is determined at Order creation time. It is in price units and is charged for each unit of the Trade.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Stop Loss Order was initiated",
        "primitive",
        "transaction.StopLossOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "orderFillTransactionID",
        "Order Fill Transaction ID",
        "The ID of the OrderFill Transaction that caused this Order to be created (only provided if this Order was created automatically when another Order was filled).",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "replacesOrderID",
        "Replaces Order ID",
        "The ID of the Order that this Order replaces (only provided if this Order replaces an existing Order).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Replaces Order Cancel Transaction ID",
        "The ID of the Transaction that cancels the replaced Order (only provided if this Order replaces an existing Order).",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
]

transaction_StopLossOrderRejectTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"STOP_LOSS_ORDER_REJECT\" in a StopLossOrderRejectTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        None,
        None
    ),
    Property(
        "price",
        "Price",
        "The price threshold specified for the Stop Loss Order. If the guaranteed flag is false, the associated Trade will be closed by a market price that is equal to or worse than this threshold. If the flag is true the associated Trade will be closed at this price.",
        "primitive",
        "pricing_common.PriceValue",
        True,
        None
    ),
    Property(
        "distance",
        "Price Distance",
        "Specifies the distance (in price units) from the Account's current price to use as the Stop Loss Order price. If the Trade is short the Instrument's bid price is used, and for long Trades the ask is used.",
        "primitive",
        "primitives.DecimalNumber",
        None,
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
        None,
        None
    ),
    Property(
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "guaranteed",
        "Guaranteed",
        "Flag indicating that the Stop Loss Order is guaranteed. The default value depends on the GuaranteedStopLossOrderMode of the account, if it is REQUIRED, the default will be true, for DISABLED or ENABLED the default is false.",
        "primitive",
        "boolean",
        None,
        None
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Stop Loss Order was initiated",
        "primitive",
        "transaction.StopLossOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "orderFillTransactionID",
        "Order Fill Transaction ID",
        "The ID of the OrderFill Transaction that caused this Order to be created (only provided if this Order was created automatically when another Order was filled).",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "intendedReplacesOrderID",
        "Order ID to Replace",
        "The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "rejectReason",
        "Reject Reason",
        "The reason that the Reject Transaction was created",
        "primitive",
        "transaction.TransactionRejectReason",
        None,
        None
    ),
]

transaction_TrailingStopLossOrderTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"TRAILING_STOP_LOSS_ORDER\" in a TrailingStopLossOrderTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        None,
        None
    ),
    Property(
        "distance",
        "Price Distance",
        "The price distance (in price units) specified for the TrailingStopLoss Order.",
        "primitive",
        "primitives.DecimalNumber",
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
        None,
        None
    ),
    Property(
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Trailing Stop Loss Order was initiated",
        "primitive",
        "transaction.TrailingStopLossOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "orderFillTransactionID",
        "Order Fill Transaction ID",
        "The ID of the OrderFill Transaction that caused this Order to be created (only provided if this Order was created automatically when another Order was filled).",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "replacesOrderID",
        "Replaces Order ID",
        "The ID of the Order that this Order replaces (only provided if this Order replaces an existing Order).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Replaces Order Cancel Transaction ID",
        "The ID of the Transaction that cancels the replaced Order (only provided if this Order replaces an existing Order).",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
]

transaction_TrailingStopLossOrderRejectTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"TRAILING_STOP_LOSS_ORDER_REJECT\" in a TrailingStopLossOrderRejectTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
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
        None,
        None
    ),
    Property(
        "distance",
        "Price Distance",
        "The price distance (in price units) specified for the TrailingStopLoss Order.",
        "primitive",
        "primitives.DecimalNumber",
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
        None,
        None
    ),
    Property(
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "reason",
        "Reason",
        "The reason that the Trailing Stop Loss Order was initiated",
        "primitive",
        "transaction.TrailingStopLossOrderReason",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Order Client Extensions",
        "Client Extensions to add to the Order (only provided if the Order is being created with client extensions).",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "orderFillTransactionID",
        "Order Fill Transaction ID",
        "The ID of the OrderFill Transaction that caused this Order to be created (only provided if this Order was created automatically when another Order was filled).",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "intendedReplacesOrderID",
        "Order ID to Replace",
        "The ID of the Order that this Order was intended to replace (only provided if this Order was intended to replace an existing Order).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "rejectReason",
        "Reject Reason",
        "The reason that the Reject Transaction was created",
        "primitive",
        "transaction.TransactionRejectReason",
        None,
        None
    ),
]

transaction_OrderFillTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"ORDER_FILL\" for an OrderFillTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "ORDER_FILL"
    ),
    Property(
        "orderID",
        "Filled Order ID",
        "The ID of the Order filled.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "clientOrderID",
        "Filled Client Order ID",
        "The client Order ID of the Order filled (only provided if the client has assigned one).",
        "primitive",
        "transaction.ClientID",
        None,
        None
    ),
    Property(
        "instrument",
        "Fill Instrument",
        "The name of the filled Order's instrument.",
        "primitive",
        "primitives.InstrumentName",
        None,
        None
    ),
    Property(
        "units",
        "Fill Units",
        "The number of units filled by the OrderFill.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "gainQuoteHomeConversionFactor",
        "Gain Quote Home Conversion Factor",
        "This is the conversion factor in effect for the Account at the time of the OrderFill for converting any gains realized in Instrument quote units into units of the Account's home currency.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "lossQuoteHomeConversionFactor",
        "Loss Quote Home Conversion Factor",
        "This is the conversion factor in effect for the Account at the time of the OrderFill for converting any losses realized in Instrument quote units into units of the Account's home currency.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "price",
        "Fill Price",
        "This field is now deprecated and should no longer be used. The individual tradesClosed, tradeReduced and tradeOpened fields contain the exact/official price each unit was filled at.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "fullVWAP",
        "Full VWAP",
        "The price that all of the units of the OrderFill should have been filled at, in the absence of guaranteed price execution. This factors in the Account's current ClientPrice, used liquidity and the units of the OrderFill only. If no Trades were closed with their price clamped for guaranteed stop loss enforcement, then this value will match the price fields of each Trade opened, closed, and reduced, and they will all be the exact same.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "fullPrice",
        "Price",
        "The price in effect for the account at the time of the Order fill.",
        "object",
        "pricing.ClientPrice",
        None,
        None
    ),
    Property(
        "reason",
        "Fill Reason",
        "The reason that an Order was filled",
        "primitive",
        "transaction.OrderFillReason",
        None,
        None
    ),
    Property(
        "pl",
        "Profit/Loss",
        "The profit or loss incurred when the Order was filled.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "financing",
        "Financing",
        "The financing paid or collected when the Order was filled.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "commission",
        "Commission",
        "The commission charged in the Account's home currency as a result of filling the Order. The commission is always represented as a positive quantity of the Account's home currency, however it reduces the balance in the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "guaranteedExecutionFee",
        "Guranteed Execution Fee",
        "The total guaranteed execution fees charged for all Trades opened, closed or reduced with guaranteed Stop Loss Orders.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "accountBalance",
        "Account Balance",
        "The Account's balance after the Order was filled.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "tradeOpened",
        "Trade Opened",
        "The Trade that was opened when the Order was filled (only provided if filling the Order resulted in a new Trade).",
        "object",
        "transaction.TradeOpen",
        None,
        None
    ),
    Property(
        "tradesClosed",
        "Trades Closed",
        "The Trades that were closed when the Order was filled (only provided if filling the Order resulted in a closing open Trades).",
        "array_object",
        "TradeReduce",
        None,
        None
    ),
    Property(
        "tradeReduced",
        "Trade Reduced",
        "The Trade that was reduced when the Order was filled (only provided if filling the Order resulted in reducing an open Trade).",
        "object",
        "transaction.TradeReduce",
        None,
        None
    ),
    Property(
        "halfSpreadCost",
        "Half Spread Cost",
        "The half spread cost for the OrderFill, which is the sum of the halfSpreadCost values in the tradeOpened, tradesClosed and tradeReduced fields. This can be a positive or negative value and is represented in the home currency of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
]

transaction_OrderCancelTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"ORDER_CANCEL\" for an OrderCancelTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "ORDER_CANCEL"
    ),
    Property(
        "orderID",
        "Cancelled Order ID",
        "The ID of the Order cancelled",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "clientOrderID",
        "Cancelled Client Order ID",
        "The client ID of the Order cancelled (only provided if the Order has a client Order ID).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "reason",
        "Cancel Reason",
        "The reason that the Order was cancelled.",
        "primitive",
        "transaction.OrderCancelReason",
        None,
        None
    ),
    Property(
        "replacedByOrderID",
        "Replaced By Order ID",
        "The ID of the Order that replaced this Order (only provided if this Order was cancelled for replacement).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
]

transaction_OrderCancelRejectTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"ORDER_CANCEL_REJECT\" for an OrderCancelRejectTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "ORDER_CANCEL_REJECT"
    ),
    Property(
        "orderID",
        "Order ID",
        "The ID of the Order intended to be cancelled",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "clientOrderID",
        "Client Order ID",
        "The client ID of the Order intended to be cancelled (only provided if the Order has a client Order ID).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "rejectReason",
        "Reject Reason",
        "The reason that the Reject Transaction was created",
        "primitive",
        "transaction.TransactionRejectReason",
        None,
        None
    ),
]

transaction_OrderClientExtensionsModifyTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"ORDER_CLIENT_EXTENSIONS_MODIFY\" for a OrderClienteExtensionsModifyTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "ORDER_CLIENT_EXTENSIONS_MODIFY"
    ),
    Property(
        "orderID",
        "Order ID",
        "The ID of the Order who's client extensions are to be modified.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "clientOrderID",
        "Client Order ID",
        "The original Client ID of the Order who's client extensions are to be modified.",
        "primitive",
        "transaction.ClientID",
        None,
        None
    ),
    Property(
        "clientExtensionsModify",
        "Order Extensions",
        "The new Client Extensions for the Order.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "tradeClientExtensionsModify",
        "Trade Extensions",
        "The new Client Extensions for the Order's Trade on fill.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

transaction_OrderClientExtensionsModifyRejectTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT\" for a OrderClientExtensionsModifyRejectTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "ORDER_CLIENT_EXTENSIONS_MODIFY_REJECT"
    ),
    Property(
        "orderID",
        "Order ID",
        "The ID of the Order who's client extensions are to be modified.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "clientOrderID",
        "Client Order ID",
        "The original Client ID of the Order who's client extensions are to be modified.",
        "primitive",
        "transaction.ClientID",
        None,
        None
    ),
    Property(
        "clientExtensionsModify",
        "Order Extensions",
        "The new Client Extensions for the Order.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "tradeClientExtensionsModify",
        "Trade Extensions",
        "The new Client Extensions for the Order's Trade on fill.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "rejectReason",
        "Reject Reason",
        "The reason that the Reject Transaction was created",
        "primitive",
        "transaction.TransactionRejectReason",
        None,
        None
    ),
]

transaction_TradeClientExtensionsModifyTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"TRADE_CLIENT_EXTENSIONS_MODIFY\" for a TradeClientExtensionsModifyTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "TRADE_CLIENT_EXTENSIONS_MODIFY"
    ),
    Property(
        "tradeID",
        "Trade ID",
        "The ID of the Trade who's client extensions are to be modified.",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "clientTradeID",
        "Client Trade ID",
        "The original Client ID of the Trade who's client extensions are to be modified.",
        "primitive",
        "transaction.ClientID",
        None,
        None
    ),
    Property(
        "tradeClientExtensionsModify",
        "Extensions",
        "The new Client Extensions for the Trade.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

transaction_TradeClientExtensionsModifyRejectTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT\" for a TradeClientExtensionsModifyRejectTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "TRADE_CLIENT_EXTENSIONS_MODIFY_REJECT"
    ),
    Property(
        "tradeID",
        "Trade ID",
        "The ID of the Trade who's client extensions are to be modified.",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "clientTradeID",
        "Client Trade ID",
        "The original Client ID of the Trade who's client extensions are to be modified.",
        "primitive",
        "transaction.ClientID",
        None,
        None
    ),
    Property(
        "tradeClientExtensionsModify",
        "Extensions",
        "The new Client Extensions for the Trade.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "rejectReason",
        "Reject Reason",
        "The reason that the Reject Transaction was created",
        "primitive",
        "transaction.TransactionRejectReason",
        None,
        None
    ),
]

transaction_MarginCallEnterTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"MARGIN_CALL_ENTER\" for an MarginCallEnterTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "MARGIN_CALL_ENTER"
    ),
]

transaction_MarginCallExtendTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"MARGIN_CALL_EXTEND\" for an MarginCallExtendTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "MARGIN_CALL_EXTEND"
    ),
    Property(
        "extensionNumber",
        "Extension Number",
        "The number of the extensions to the Account's current margin call that have been applied. This value will be set to 1 for the first MarginCallExtend Transaction",
        "primitive",
        "integer",
        None,
        None
    ),
]

transaction_MarginCallExitTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"MARGIN_CALL_EXIT\" for an MarginCallExitTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "MARGIN_CALL_EXIT"
    ),
]

transaction_DelayedTradeClosureTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"DELAYED_TRADE_CLOSURE\" for an DelayedTradeClosureTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "DELAYED_TRADE_CLOSURE"
    ),
    Property(
        "reason",
        "Reason",
        "The reason for the delayed trade closure",
        "primitive",
        "transaction.MarketOrderReason",
        None,
        None
    ),
    Property(
        "tradeIDs",
        "Trade ID's",
        "List of Trade ID's identifying the open trades that will be closed when their respective instruments become tradeable",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
]

transaction_DailyFinancingTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"DAILY_FINANCING\" for a DailyFinancingTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "DAILY_FINANCING"
    ),
    Property(
        "financing",
        "Financing",
        "The amount of financing paid/collected for the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "accountBalance",
        "Account Balance",
        "The Account's balance after daily financing.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "accountFinancingMode",
        "Account Financing Mode",
        "The account financing mode at the time of the daily financing.",
        "primitive",
        "account.AccountFinancingMode",
        None,
        None
    ),
    Property(
        "positionFinancings",
        "Per-Position Financing",
        "The financing paid/collected for each Position in the Account.",
        "array_object",
        "PositionFinancing",
        None,
        None
    ),
]

transaction_ResetResettablePLTransaction = [
    Property(
        "id",
        "Transaction ID",
        "The Transaction's Identifier.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Transaction was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "userID",
        "User ID",
        "The ID of the user that initiated the creation of the Transaction.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "accountID",
        "Account ID",
        "The ID of the Account the Transaction was created for.",
        "primitive",
        "account.AccountID",
        None,
        None
    ),
    Property(
        "batchID",
        "Transaction Batch ID",
        "The ID of the \"batch\" that the Transaction belongs to. Transactions in the same batch are applied to the Account simultaneously.",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "requestID",
        "Request ID",
        "The Request ID of the request which generated the transaction.",
        "primitive",
        "transaction.RequestID",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The Type of the Transaction. Always set to \"RESET_RESETTABLE_PL\" for a ResetResettablePLTransaction.",
        "primitive",
        "transaction.TransactionType",
        None,
        "RESET_RESETTABLE_PL"
    ),
]

transaction_ClientExtensions = [
    Property(
        "id",
        "Client ID",
        "The Client ID of the Order/Trade",
        "primitive",
        "transaction.ClientID",
        None,
        None
    ),
    Property(
        "tag",
        "Tag",
        "A tag associated with the Order/Trade",
        "primitive",
        "transaction.ClientTag",
        None,
        None
    ),
    Property(
        "comment",
        "Comment",
        "A comment associated with the Order/Trade",
        "primitive",
        "transaction.ClientComment",
        None,
        None
    ),
]

transaction_TakeProfitDetails = [
    Property(
        "price",
        "Price",
        "The price that the Take Profit Order will be triggered at. Only one of the price and distance fields may be specified.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "timeInForce",
        "Time In Force",
        "The time in force for the created Take Profit Order. This may only be GTC, GTD or GFD.",
        "primitive",
        "order.TimeInForce",
        None,
        "GTC"
    ),
    Property(
        "gtdTime",
        "GTD Time",
        "The date when the Take Profit Order will be cancelled on if timeInForce is GTD.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The Client Extensions to add to the Take Profit Order when created.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

transaction_StopLossDetails = [
    Property(
        "price",
        "Price",
        "The price that the Stop Loss Order will be triggered at. Only one of the price and distance fields may be specified.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "distance",
        "Price Distance",
        "Specifies the distance (in price units) from the Trade's open price to use as the Stop Loss Order price. Only one of the distance and price fields may be specified.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "timeInForce",
        "Time In Force",
        "The time in force for the created Stop Loss Order. This may only be GTC, GTD or GFD.",
        "primitive",
        "order.TimeInForce",
        None,
        "GTC"
    ),
    Property(
        "gtdTime",
        "GTD Time",
        "The date when the Stop Loss Order will be cancelled on if timeInForce is GTD.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The Client Extensions to add to the Stop Loss Order when created.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "guaranteed",
        "Guaranteed",
        "Flag indicating that the price for the Stop Loss Order is guaranteed. The default value depends on the GuaranteedStopLossOrderMode of the account, if it is REQUIRED, the default will be true, for DISABLED or ENABLED the default is false.",
        "primitive",
        "boolean",
        None,
        None
    ),
]

transaction_TrailingStopLossDetails = [
    Property(
        "distance",
        "Trailing Price Distance",
        "The distance (in price units) from the Trade's fill price that the Trailing Stop Loss Order will be triggered at.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "timeInForce",
        "Time In Force",
        "The time in force for the created Trailing Stop Loss Order. This may only be GTC, GTD or GFD.",
        "primitive",
        "order.TimeInForce",
        None,
        "GTC"
    ),
    Property(
        "gtdTime",
        "GTD Time",
        "The date when the Trailing Stop Loss Order will be cancelled on if timeInForce is GTD.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The Client Extensions to add to the Trailing Stop Loss Order when created.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

transaction_TradeOpen = [
    Property(
        "tradeID",
        "Trade ID",
        "The ID of the Trade that was opened",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "units",
        "Amount",
        "The number of units opened by the Trade",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "price",
        "Units Opened Price",
        "The average price that the units were opened at.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "guaranteedExecutionFee",
        "Guranteed Execution Fee",
        "This is the fee charged for opening the trade if it has a guaranteed Stop Loss Order attached to it.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions for the newly opened Trade",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "halfSpreadCost",
        "Half Spread Cost",
        "The half spread cost for the trade open. This can be a positive or negative value and is represented in the home currency of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "initialMarginRequired",
        "Initial Margin Required",
        "The margin required at the time the Trade was created. Note, this is the 'pure' margin required, it is not the 'effective' margin used that factors in the trade risk if a GSLO is attached to the trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
]

transaction_TradeReduce = [
    Property(
        "tradeID",
        "Trade ID",
        "The ID of the Trade that was reduced or closed",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "units",
        "Amount",
        "The number of units that the Trade was reduced by",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "price",
        "Units Closed Price",
        "The average price that the units were closed at. This price may be clamped for guaranteed Stop Loss Orders.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "realizedPL",
        "Profit/Loss",
        "The PL realized when reducing the Trade",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "financing",
        "Financing",
        "The financing paid/collected when reducing the Trade",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "guaranteedExecutionFee",
        "Guranteed Execution Fee",
        "This is the fee that is charged for closing the Trade if it has a guaranteed Stop Loss Order attached to it.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "halfSpreadCost",
        "Half Spread Cost",
        "The half spread cost for the trade reduce/close. This can be a positive or negative value and is represented in the home currency of the Account.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
]

transaction_MarketOrderTradeClose = [
    Property(
        "tradeID",
        "Trade ID",
        "The ID of the Trade requested to be closed",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "clientTradeID",
        "Client Trade ID",
        "The client ID of the Trade requested to be closed",
        "primitive",
        "string",
        None,
        None
    ),
    Property(
        "units",
        "Amount",
        "Indication of how much of the Trade to close. Either \"ALL\", or a DecimalNumber reflection a partial close of the Trade.",
        "primitive",
        "string",
        None,
        None
    ),
]

transaction_MarketOrderMarginCloseout = [
    Property(
        "reason",
        "Reason",
        "The reason the Market Order was created to perform a margin closeout",
        "primitive",
        "transaction.MarketOrderMarginCloseoutReason",
        None,
        None
    ),
]

transaction_MarketOrderDelayedTradeClose = [
    Property(
        "tradeID",
        "Trade ID",
        "The ID of the Trade being closed",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "clientTradeID",
        "Client Trade ID",
        "The Client ID of the Trade being closed",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "sourceTransactionID",
        "Source Transaction ID",
        "The Transaction ID of the DelayedTradeClosure transaction to which this Delayed Trade Close belongs to",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
]

transaction_MarketOrderPositionCloseout = [
    Property(
        "instrument",
        "Instrument",
        "The instrument of the Position being closed out.",
        "primitive",
        "primitives.InstrumentName",
        None,
        None
    ),
    Property(
        "units",
        "Amount",
        "Indication of how much of the Position to close. Either \"ALL\", or a DecimalNumber reflection a partial close of the Trade. The DecimalNumber must always be positive, and represent a number that doesn't exceed the absolute size of the Position.",
        "primitive",
        "string",
        None,
        None
    ),
]

transaction_LiquidityRegenerationSchedule = [
    Property(
        "steps",
        "Steps",
        "The steps in the Liquidity Regeneration Schedule",
        "array_object",
        "LiquidityRegenerationScheduleStep",
        None,
        None
    ),
]

transaction_LiquidityRegenerationScheduleStep = [
    Property(
        "timestamp",
        "Time",
        "The timestamp of the schedule step.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "bidLiquidityUsed",
        "Bid Liquidity Used",
        "The amount of bid liquidity used at this step in the schedule.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "askLiquidityUsed",
        "Ask Liquidity Used",
        "The amount of ask liquidity used at this step in the schedule.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
]

transaction_OpenTradeFinancing = [
    Property(
        "tradeID",
        "tradeID",
        "The ID of the Trade that financing is being paid/collected for.",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "financing",
        "Financing",
        "The amount of financing paid/collected for the Trade.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
]

transaction_PositionFinancing = [
    Property(
        "instrument",
        "Instrument",
        "The instrument of the Position that financing is being paid/collected for.",
        "primitive",
        "primitives.InstrumentName",
        None,
        None
    ),
    Property(
        "financing",
        "Financing",
        "The amount of financing paid/collected for the Position.",
        "primitive",
        "primitives.AccountUnits",
        None,
        None
    ),
    Property(
        "openTradeFinancings",
        "Trade Financings",
        "The financing paid/collecte for each open Trade within the Position.",
        "array_object",
        "OpenTradeFinancing",
        None,
        None
    ),
]

transaction_TransactionHeartbeat = [
    Property(
        "type",
        "type",
        "The string \"HEARTBEAT\"",
        "primitive",
        "string",
        None,
        "HEARTBEAT"
    ),
    Property(
        "lastTransactionID",
        "lastTransactionID",
        "The ID of the most recent Transaction created for the Account",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "time",
        "time",
        "The date/time when the TransactionHeartbeat was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
]

user_UserInfo = [
    Property(
        "username",
        "username",
        "The user-provided username.",
        "primitive",
        "string",
        None,
        None
    ),
    Property(
        "userID",
        "userID",
        "The user's OANDA-assigned user ID.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "country",
        "country",
        "The country that the user is based in.",
        "primitive",
        "string",
        None,
        None
    ),
    Property(
        "emailAddress",
        "emailAddress",
        "The user's email address.",
        "primitive",
        "string",
        None,
        None
    ),
]

user_UserInfoExternal = [
    Property(
        "userID",
        "userID",
        "The user's OANDA-assigned user ID.",
        "primitive",
        "integer",
        None,
        None
    ),
    Property(
        "country",
        "country",
        "The country that the user is based in.",
        "primitive",
        "string",
        None,
        None
    ),
    Property(
        "FIFO",
        "FIFO",
        "Flag indicating if the the user's Accounts adhere to FIFO execution rules.",
        "primitive",
        "boolean",
        None,
        None
    ),
]

pricing_ClientPrice = [
    Property(
        "type",
        "Type",
        "The string \"PRICE\". Used to identify the a Price object when found in a stream.",
        "primitive",
        "string",
        None,
        "PRICE"
    ),
    Property(
        "instrument",
        "Instrument",
        "The Price's Instrument.",
        "primitive",
        "primitives.InstrumentName",
        None,
        None
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Price was created",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "status",
        "Status",
        "The status of the Price.",
        "primitive",
        "pricing.PriceStatus",
        None,
        None
    ),
    Property(
        "tradeable",
        "Is Tradeable",
        "Flag indicating if the Price is tradeable or not",
        "primitive",
        "boolean",
        None,
        None
    ),
    Property(
        "bids",
        "Bids",
        "The list of prices and liquidity available on the Instrument's bid side. It is possible for this list to be empty if there is no bid liquidity currently available for the Instrument in the Account.",
        "array_object",
        "PriceBucket",
        None,
        None
    ),
    Property(
        "asks",
        "Asks",
        "The list of prices and liquidity available on the Instrument's ask side. It is possible for this list to be empty if there is no ask liquidity currently available for the Instrument in the Account.",
        "array_object",
        "PriceBucket",
        None,
        None
    ),
    Property(
        "closeoutBid",
        "Closeout Bid",
        "The closeout bid Price. This Price is used when a bid is required to closeout a Position (margin closeout or manual) yet there is no bid liquidity. The closeout bid is never used to open a new position.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "closeoutAsk",
        "Closeout Ask",
        "The closeout ask Price. This Price is used when a ask is required to closeout a Position (margin closeout or manual) yet there is no ask liquidity. The closeout ask is never used to open a new position.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "quoteHomeConversionFactors",
        "Quote Home Conversions",
        "The factors used to convert quantities of this price's Instrument's quote currency into a quantity of the Account's home currency. When the includeHomeConversions is present in the pricing request (regardless of its value), this field will not be present.",
        "object",
        "pricing.QuoteHomeConversionFactors",
        None,
        None
    ),
    Property(
        "unitsAvailable",
        "Units Available",
        "Representation of how many units of an Instrument are available to be traded by an Order depending on its postionFill option.",
        "object",
        "order.UnitsAvailable",
        None,
        None
    ),
]

pricing_QuoteHomeConversionFactors = [
    Property(
        "positiveUnits",
        "Positive Units",
        "The factor used to convert a positive amount of the Price's Instrument's quote currency into a positive amount of the Account's home currency.  Conversion is performed by multiplying the quote units by the conversion factor.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "negativeUnits",
        "Negative Units",
        "The factor used to convert a negative amount of the Price's Instrument's quote currency into a negative amount of the Account's home currency.  Conversion is performed by multiplying the quote units by the conversion factor.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
]

pricing_HomeConversions = [
    Property(
        "currency",
        "currency",
        "The currency to be converted into the home currency.",
        "primitive",
        "primitives.Currency",
        None,
        None
    ),
    Property(
        "accountGain",
        "Account Gain",
        "The factor used to convert any gains for an Account in the specified currency into the Account's home currency. This would include positive realized P/L and positive financing amounts. Conversion is performed by multiplying the positive P/L by the conversion factor.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "accountLoss",
        "Account Loss The factor used to convert any losses for an Account in the specified currency into the Account's home currency. This would include negative realized P/L and negative financing amounts. Conversion is performed by multiplying the positive P/L by the conversion factor.",
        "The string representation of a decimal number.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "positionValue",
        "Position Value",
        "The factor used to convert a Position or Trade Value in the specified currency into the Account's home currency. Conversion is performed by multiplying the Position or Trade Value by the conversion factor.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
]

pricing_PricingHeartbeat = [
    Property(
        "type",
        "Type",
        "The string \"HEARTBEAT\"",
        "primitive",
        "string",
        None,
        "HEARTBEAT"
    ),
    Property(
        "time",
        "Time",
        "The date/time when the Heartbeat was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
]

order_OrderIdentifier = [
    Property(
        "orderID",
        "orderID",
        "The OANDA-assigned Order ID",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "clientOrderID",
        "clientOrderID",
        "The client-provided client Order ID",
        "primitive",
        "transaction.ClientID",
        None,
        None
    ),
]

order_DynamicOrderState = [
    Property(
        "id",
        "Order ID",
        "The Order's ID.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "trailingStopValue",
        "Trailing Stop Value",
        "The Order's calculated trailing stop value.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "triggerDistance",
        "Trigger Distance",
        "The distance between the Trailing Stop Loss Order's trailingStopValue and the current Market Price. This represents the distance (in price units) of the Order from a triggering price. If the distance could not be determined, this value will not be set.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "isTriggerDistanceExact",
        "Trigger Distance Is Exact",
        "True if an exact trigger distance could be calculated. If false, it means the provided trigger distance is a best estimate. If the distance could not be determined, this value will not be set.",
        "primitive",
        "boolean",
        None,
        None
    ),
]

order_Order = [
    Property(
        "id",
        "Order ID",
        "The Order's identifier, unique within the Order's Account.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "createTime",
        "Create Time",
        "The time when the Order was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "state",
        "State",
        "The current state of the Order.",
        "primitive",
        "order.OrderState",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

order_MarketOrder = [
    Property(
        "id",
        "Order ID",
        "The Order's identifier, unique within the Order's Account.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "createTime",
        "Create Time",
        "The time when the Order was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "state",
        "State",
        "The current state of the Order.",
        "primitive",
        "order.OrderState",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The type of the Order. Always set to \"MARKET\" for Market Orders.",
        "primitive",
        "order.OrderType",
        None,
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
        "pricing_common.PriceValue",
        None,
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
        None,
        None
    ),
    Property(
        "longPositionCloseout",
        "Long Position Close Details",
        "Details of the long Position requested to be closed out, only provided when a Market Order is being used to explicitly closeout a long Position.",
        "object",
        "transaction.MarketOrderPositionCloseout",
        None,
        None
    ),
    Property(
        "shortPositionCloseout",
        "Short Position Close Details",
        "Details of the short Position requested to be closed out, only provided when a Market Order is being used to explicitly closeout a short Position.",
        "object",
        "transaction.MarketOrderPositionCloseout",
        None,
        None
    ),
    Property(
        "marginCloseout",
        "Margin Closeout Details",
        "Details of the Margin Closeout that this Market Order was created for",
        "object",
        "transaction.MarketOrderMarginCloseout",
        None,
        None
    ),
    Property(
        "delayedTradeClose",
        "Delayed Trade Close Details",
        "Details of the delayed Trade close that this Market Order was created for",
        "object",
        "transaction.MarketOrderDelayedTradeClose",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "fillingTransactionID",
        "Filling Transaction ID",
        "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "filledTime",
        "Filled Time",
        "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "tradeOpenedID",
        "Trade Opened ID",
        "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeReducedID",
        "Trade Reduced ID",
        "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeClosedIDs",
        "Trade Closed IDs",
        "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
        "array_primitive",
        "TradeID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Cancelling Transction ID",
        "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "cancelledTime",
        "Cancelled Time",
        "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
]

order_FixedPriceOrder = [
    Property(
        "id",
        "Order ID",
        "The Order's identifier, unique within the Order's Account.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "createTime",
        "Create Time",
        "The time when the Order was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "state",
        "State",
        "The current state of the Order.",
        "primitive",
        "order.OrderState",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The type of the Order. Always set to \"FIXED_PRICE\" for Fixed Price Orders.",
        "primitive",
        "order.OrderType",
        None,
        "FIXED_PRICE"
    ),
    Property(
        "instrument",
        "Instrument",
        "The Fixed Price Order's Instrument.",
        "primitive",
        "primitives.InstrumentName",
        True,
        None
    ),
    Property(
        "units",
        "Amount",
        "The quantity requested to be filled by the Fixed Price Order. A posititive number of units results in a long Order, and a negative number of units results in a short Order.",
        "primitive",
        "primitives.DecimalNumber",
        True,
        None
    ),
    Property(
        "price",
        "Price",
        "The price specified for the Fixed Price Order. This price is the exact price that the Fixed Price Order will be filled at.",
        "primitive",
        "pricing_common.PriceValue",
        True,
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
        "tradeState",
        "TradeState",
        "The state that the trade resulting from the Fixed Price Order should be set to.",
        "primitive",
        "string",
        True,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "fillingTransactionID",
        "Filling Transaction ID",
        "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "filledTime",
        "Filled Time",
        "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "tradeOpenedID",
        "Trade Opened ID",
        "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeReducedID",
        "Trade Reduced ID",
        "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeClosedIDs",
        "Trade Closed IDs",
        "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
        "array_primitive",
        "TradeID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Cancelling Transction ID",
        "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "cancelledTime",
        "Cancelled Time",
        "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
]

order_LimitOrder = [
    Property(
        "id",
        "Order ID",
        "The Order's identifier, unique within the Order's Account.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "createTime",
        "Create Time",
        "The time when the Order was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "state",
        "State",
        "The current state of the Order.",
        "primitive",
        "order.OrderState",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The type of the Order. Always set to \"LIMIT\" for Limit Orders.",
        "primitive",
        "order.OrderType",
        None,
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
        "pricing_common.PriceValue",
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
        None,
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
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "fillingTransactionID",
        "Filling Transaction ID",
        "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "filledTime",
        "Filled Time",
        "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "tradeOpenedID",
        "Trade Opened ID",
        "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeReducedID",
        "Trade Reduced ID",
        "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeClosedIDs",
        "Trade Closed IDs",
        "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
        "array_primitive",
        "TradeID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Cancelling Transction ID",
        "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "cancelledTime",
        "Cancelled Time",
        "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "replacesOrderID",
        "Replaces Order ID",
        "The ID of the Order that was replaced by this Order (only provided if this Order was created as part of a cancel/replace).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "replacedByOrderID",
        "Replaced by Order ID",
        "The ID of the Order that replaced this Order (only provided if this Order was cancelled as part of a cancel/replace).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
]

order_StopOrder = [
    Property(
        "id",
        "Order ID",
        "The Order's identifier, unique within the Order's Account.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "createTime",
        "Create Time",
        "The time when the Order was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "state",
        "State",
        "The current state of the Order.",
        "primitive",
        "order.OrderState",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The type of the Order. Always set to \"STOP\" for Stop Orders.",
        "primitive",
        "order.OrderType",
        None,
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
        "pricing_common.PriceValue",
        True,
        None
    ),
    Property(
        "priceBound",
        "Price Bound",
        "The worst market price that may be used to fill this Stop Order. If the market gaps and crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.",
        "primitive",
        "pricing_common.PriceValue",
        None,
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
        None,
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
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "fillingTransactionID",
        "Filling Transaction ID",
        "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "filledTime",
        "Filled Time",
        "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "tradeOpenedID",
        "Trade Opened ID",
        "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeReducedID",
        "Trade Reduced ID",
        "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeClosedIDs",
        "Trade Closed IDs",
        "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
        "array_primitive",
        "TradeID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Cancelling Transction ID",
        "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "cancelledTime",
        "Cancelled Time",
        "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "replacesOrderID",
        "Replaces Order ID",
        "The ID of the Order that was replaced by this Order (only provided if this Order was created as part of a cancel/replace).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "replacedByOrderID",
        "Replaced by Order ID",
        "The ID of the Order that replaced this Order (only provided if this Order was cancelled as part of a cancel/replace).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
]

order_MarketIfTouchedOrder = [
    Property(
        "id",
        "Order ID",
        "The Order's identifier, unique within the Order's Account.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "createTime",
        "Create Time",
        "The time when the Order was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "state",
        "State",
        "The current state of the Order.",
        "primitive",
        "order.OrderState",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The type of the Order. Always set to \"MARKET_IF_TOUCHED\" for Market If Touched Orders.",
        "primitive",
        "order.OrderType",
        None,
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
        "pricing_common.PriceValue",
        True,
        None
    ),
    Property(
        "priceBound",
        "Price Value",
        "The worst market price that may be used to fill this MarketIfTouched Order.",
        "primitive",
        "pricing_common.PriceValue",
        None,
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
        None,
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
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "initialMarketPrice",
        "Initial Market Price",
        "The Market price at the time when the MarketIfTouched Order was created.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "fillingTransactionID",
        "Filling Transaction ID",
        "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "filledTime",
        "Filled Time",
        "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "tradeOpenedID",
        "Trade Opened ID",
        "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeReducedID",
        "Trade Reduced ID",
        "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeClosedIDs",
        "Trade Closed IDs",
        "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
        "array_primitive",
        "TradeID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Cancelling Transction ID",
        "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "cancelledTime",
        "Cancelled Time",
        "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "replacesOrderID",
        "Replaces Order ID",
        "The ID of the Order that was replaced by this Order (only provided if this Order was created as part of a cancel/replace).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "replacedByOrderID",
        "Replaced by Order ID",
        "The ID of the Order that replaced this Order (only provided if this Order was cancelled as part of a cancel/replace).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
]

order_TakeProfitOrder = [
    Property(
        "id",
        "Order ID",
        "The Order's identifier, unique within the Order's Account.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "createTime",
        "Create Time",
        "The time when the Order was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "state",
        "State",
        "The current state of the Order.",
        "primitive",
        "order.OrderState",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The type of the Order. Always set to \"TAKE_PROFIT\" for Take Profit Orders.",
        "primitive",
        "order.OrderType",
        None,
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
        None,
        None
    ),
    Property(
        "price",
        "Price",
        "The price threshold specified for the TakeProfit Order. The associated Trade will be closed by a market price that is equal to or better than this threshold.",
        "primitive",
        "pricing_common.PriceValue",
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
        None,
        None
    ),
    Property(
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "fillingTransactionID",
        "Filling Transaction ID",
        "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "filledTime",
        "Filled Time",
        "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "tradeOpenedID",
        "Trade Opened ID",
        "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeReducedID",
        "Trade Reduced ID",
        "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeClosedIDs",
        "Trade Closed IDs",
        "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
        "array_primitive",
        "TradeID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Cancelling Transction ID",
        "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "cancelledTime",
        "Cancelled Time",
        "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "replacesOrderID",
        "Replaces Order ID",
        "The ID of the Order that was replaced by this Order (only provided if this Order was created as part of a cancel/replace).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "replacedByOrderID",
        "Replaced by Order ID",
        "The ID of the Order that replaced this Order (only provided if this Order was cancelled as part of a cancel/replace).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
]

order_StopLossOrder = [
    Property(
        "id",
        "Order ID",
        "The Order's identifier, unique within the Order's Account.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "createTime",
        "Create Time",
        "The time when the Order was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "state",
        "State",
        "The current state of the Order.",
        "primitive",
        "order.OrderState",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The type of the Order. Always set to \"STOP_LOSS\" for Stop Loss Orders.",
        "primitive",
        "order.OrderType",
        None,
        "STOP_LOSS"
    ),
    Property(
        "guaranteedExecutionPremium",
        "Guaranteed Execution Fee",
        "The premium that will be charged if the Stop Loss Order is guaranteed and the Order is filled at the guaranteed price. It is in price units and is charged for each unit of the Trade.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
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
        None,
        None
    ),
    Property(
        "price",
        "Price",
        "The price threshold specified for the Stop Loss Order. If the guaranteed flag is false, the associated Trade will be closed by a market price that is equal to or worse than this threshold. If the flag is true the associated Trade will be closed at this price.",
        "primitive",
        "pricing_common.PriceValue",
        True,
        None
    ),
    Property(
        "distance",
        "Price Distance",
        "Specifies the distance (in price units) from the Account's current price to use as the Stop Loss Order price. If the Trade is short the Instrument's bid price is used, and for long Trades the ask is used.",
        "primitive",
        "primitives.DecimalNumber",
        None,
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
        None,
        None
    ),
    Property(
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "guaranteed",
        "Guaranteed",
        "Flag indicating that the Stop Loss Order is guaranteed. The default value depends on the GuaranteedStopLossOrderMode of the account, if it is REQUIRED, the default will be true, for DISABLED or ENABLED the default is false.",
        "primitive",
        "boolean",
        None,
        None
    ),
    Property(
        "fillingTransactionID",
        "Filling Transaction ID",
        "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "filledTime",
        "Filled Time",
        "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "tradeOpenedID",
        "Trade Opened ID",
        "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeReducedID",
        "Trade Reduced ID",
        "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeClosedIDs",
        "Trade Closed IDs",
        "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
        "array_primitive",
        "TradeID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Cancelling Transction ID",
        "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "cancelledTime",
        "Cancelled Time",
        "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "replacesOrderID",
        "Replaces Order ID",
        "The ID of the Order that was replaced by this Order (only provided if this Order was created as part of a cancel/replace).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "replacedByOrderID",
        "Replaced by Order ID",
        "The ID of the Order that replaced this Order (only provided if this Order was cancelled as part of a cancel/replace).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
]

order_TrailingStopLossOrder = [
    Property(
        "id",
        "Order ID",
        "The Order's identifier, unique within the Order's Account.",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "createTime",
        "Create Time",
        "The time when the Order was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "state",
        "State",
        "The current state of the Order.",
        "primitive",
        "order.OrderState",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions of the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "type",
        "Type",
        "The type of the Order. Always set to \"TRAILING_STOP_LOSS\" for Trailing Stop Loss Orders.",
        "primitive",
        "order.OrderType",
        None,
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
        None,
        None
    ),
    Property(
        "distance",
        "Price Distance",
        "The price distance (in price units) specified for the TrailingStopLoss Order.",
        "primitive",
        "primitives.DecimalNumber",
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
        None,
        None
    ),
    Property(
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "trailingStopValue",
        "Trailing Stop Loss Value",
        "The trigger price for the Trailing Stop Loss Order. The trailing stop value will trail (follow) the market price by the TSL order's configured \"distance\" as the market price moves in the winning direction. If the market price moves to a level that is equal to or worse than the trailing stop value, the order will be filled and the Trade will be closed.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "fillingTransactionID",
        "Filling Transaction ID",
        "ID of the Transaction that filled this Order (only provided when the Order's state is FILLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "filledTime",
        "Filled Time",
        "Date/time when the Order was filled (only provided when the Order's state is FILLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "tradeOpenedID",
        "Trade Opened ID",
        "Trade ID of Trade opened when the Order was filled (only provided when the Order's state is FILLED and a Trade was opened as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeReducedID",
        "Trade Reduced ID",
        "Trade ID of Trade reduced when the Order was filled (only provided when the Order's state is FILLED and a Trade was reduced as a result of the fill)",
        "primitive",
        "trade.TradeID",
        None,
        None
    ),
    Property(
        "tradeClosedIDs",
        "Trade Closed IDs",
        "Trade IDs of Trades closed when the Order was filled (only provided when the Order's state is FILLED and one or more Trades were closed as a result of the fill)",
        "array_primitive",
        "TradeID",
        None,
        None
    ),
    Property(
        "cancellingTransactionID",
        "Cancelling Transction ID",
        "ID of the Transaction that cancelled the Order (only provided when the Order's state is CANCELLED)",
        "primitive",
        "transaction.TransactionID",
        None,
        None
    ),
    Property(
        "cancelledTime",
        "Cancelled Time",
        "Date/time when the Order was cancelled (only provided when the state of the Order is CANCELLED)",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "replacesOrderID",
        "Replaces Order ID",
        "The ID of the Order that was replaced by this Order (only provided if this Order was created as part of a cancel/replace).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
    Property(
        "replacedByOrderID",
        "Replaced by Order ID",
        "The ID of the Order that replaced this Order (only provided if this Order was cancelled as part of a cancel/replace).",
        "primitive",
        "order.OrderID",
        None,
        None
    ),
]

order_OrderRequest = [
]

order_MarketOrderRequest = [
    Property(
        "type",
        "Type",
        "The type of the Order to Create. Must be set to \"MARKET\" when creating a Market Order.",
        "primitive",
        "order.OrderType",
        None,
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
        "pricing_common.PriceValue",
        None,
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
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

order_LimitOrderRequest = [
    Property(
        "type",
        "Type",
        "The type of the Order to Create. Must be set to \"LIMIT\" when creating a Market Order.",
        "primitive",
        "order.OrderType",
        None,
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
        "pricing_common.PriceValue",
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
        None,
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
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

order_StopOrderRequest = [
    Property(
        "type",
        "Type",
        "The type of the Order to Create. Must be set to \"STOP\" when creating a Stop Order.",
        "primitive",
        "order.OrderType",
        None,
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
        "pricing_common.PriceValue",
        True,
        None
    ),
    Property(
        "priceBound",
        "Price Bound",
        "The worst market price that may be used to fill this Stop Order. If the market gaps and crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.",
        "primitive",
        "pricing_common.PriceValue",
        None,
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
        None,
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
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

order_MarketIfTouchedOrderRequest = [
    Property(
        "type",
        "Type",
        "The type of the Order to Create. Must be set to \"MARKET_IF_TOUCHED\" when creating a Market If Touched Order.",
        "primitive",
        "order.OrderType",
        None,
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
        "pricing_common.PriceValue",
        True,
        None
    ),
    Property(
        "priceBound",
        "Price Value",
        "The worst market price that may be used to fill this MarketIfTouched Order.",
        "primitive",
        "pricing_common.PriceValue",
        None,
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
        None,
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
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
    Property(
        "takeProfitOnFill",
        "Take Profit On Fill",
        "TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is modified directly through the Trade.",
        "object",
        "transaction.TakeProfitDetails",
        None,
        None
    ),
    Property(
        "stopLossOnFill",
        "Stop Loss On Fill",
        "StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.StopLossDetails",
        None,
        None
    ),
    Property(
        "trailingStopLossOnFill",
        "Trailing Stop Loss On Fill",
        "TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss Order is modified directly through the Trade.",
        "object",
        "transaction.TrailingStopLossDetails",
        None,
        None
    ),
    Property(
        "tradeClientExtensions",
        "Trade Client Extensions",
        "Client Extensions to add to the Trade created when the Order is filled (if such a Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

order_TakeProfitOrderRequest = [
    Property(
        "type",
        "Type",
        "The type of the Order to Create. Must be set to \"TAKE_PROFIT\" when creating a Take Profit Order.",
        "primitive",
        "order.OrderType",
        None,
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
        None,
        None
    ),
    Property(
        "price",
        "Price",
        "The price threshold specified for the TakeProfit Order. The associated Trade will be closed by a market price that is equal to or better than this threshold.",
        "primitive",
        "pricing_common.PriceValue",
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
        None,
        None
    ),
    Property(
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

order_StopLossOrderRequest = [
    Property(
        "type",
        "Type",
        "The type of the Order to Create. Must be set to \"STOP_LOSS\" when creating a Stop Loss Order.",
        "primitive",
        "order.OrderType",
        None,
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
        None,
        None
    ),
    Property(
        "price",
        "Price",
        "The price threshold specified for the Stop Loss Order. If the guaranteed flag is false, the associated Trade will be closed by a market price that is equal to or worse than this threshold. If the flag is true the associated Trade will be closed at this price.",
        "primitive",
        "pricing_common.PriceValue",
        True,
        None
    ),
    Property(
        "distance",
        "Price Distance",
        "Specifies the distance (in price units) from the Account's current price to use as the Stop Loss Order price. If the Trade is short the Instrument's bid price is used, and for long Trades the ask is used.",
        "primitive",
        "primitives.DecimalNumber",
        None,
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
        None,
        None
    ),
    Property(
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "guaranteed",
        "Guaranteed",
        "Flag indicating that the Stop Loss Order is guaranteed. The default value depends on the GuaranteedStopLossOrderMode of the account, if it is REQUIRED, the default will be true, for DISABLED or ENABLED the default is false.",
        "primitive",
        "boolean",
        None,
        None
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

order_TrailingStopLossOrderRequest = [
    Property(
        "type",
        "Type",
        "The type of the Order to Create. Must be set to \"TRAILING_STOP_LOSS\" when creating a Trailng Stop Loss Order.",
        "primitive",
        "order.OrderType",
        None,
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
        None,
        None
    ),
    Property(
        "distance",
        "Price Distance",
        "The price distance (in price units) specified for the TrailingStopLoss Order.",
        "primitive",
        "primitives.DecimalNumber",
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
        None,
        None
    ),
    Property(
        "triggerCondition",
        "Trigger Condition",
        "Specification of which price component should be used when determining if an Order should be triggered and filled. This allows Orders to be triggered based on the bid, ask, mid, default (ask for buy, bid for sell) or inverse (ask for sell, bid for buy) price depending on the desired behaviour. Orders are always filled using their default price component.\nThis feature is only provided through the REST API. Clients who choose to specify a non-default trigger condition will not see it reflected in any of OANDA's proprietary or partner trading platforms, their transaction history or their account statements. OANDA platforms always assume that an Order's trigger condition is set to the default value when indicating the distance from an Order's trigger price, and will always provide the default trigger condition when creating or modifying an Order.\nA special restriction applies when creating a guaranteed Stop Loss Order. In this case the TriggerCondition value must either be \"DEFAULT\", or the \"natural\" trigger side \"DEFAULT\" results in. So for a Stop Loss Order for a long trade valid values are \"DEFAULT\" and \"BID\", and for short trades \"DEFAULT\" and \"ASK\" are valid.",
        "primitive",
        "order.OrderTriggerCondition",
        True,
        "DEFAULT"
    ),
    Property(
        "clientExtensions",
        "Client Extensions",
        "The client extensions to add to the Order. Do not set, modify, or delete clientExtensions if your account is associated with MT4.",
        "object",
        "transaction.ClientExtensions",
        None,
        None
    ),
]

order_UnitsAvailableDetails = [
    Property(
        "long",
        "Long",
        "The units available for long Orders.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "short",
        "Short",
        "The units available for short Orders.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
]

order_UnitsAvailable = [
    Property(
        "default",
        "Default",
        "The number of units that are available to be traded using an Order with a positionFill option of \"DEFAULT\". For an Account with hedging enabled, this value will be the same as the \"OPEN_ONLY\" value. For an Account without hedging enabled, this value will be the same as the \"REDUCE_FIRST\" value.",
        "object",
        "order.UnitsAvailableDetails",
        None,
        None
    ),
    Property(
        "reduceFirst",
        "Reduce First",
        "The number of units that may are available to be traded with an Order with a positionFill option of \"REDUCE_FIRST\".",
        "object",
        "order.UnitsAvailableDetails",
        None,
        None
    ),
    Property(
        "reduceOnly",
        "Reduce Only",
        "The number of units that may are available to be traded with an Order with a positionFill option of \"REDUCE_ONLY\".",
        "object",
        "order.UnitsAvailableDetails",
        None,
        None
    ),
    Property(
        "openOnly",
        "Open Only",
        "The number of units that may are available to be traded with an Order with a positionFill option of \"OPEN_ONLY\".",
        "object",
        "order.UnitsAvailableDetails",
        None,
        None
    ),
]

order_GuaranteedStopLossOrderEntryData = [
    Property(
        "minimumDistance",
        "minimumDistance",
        "The minimum distance allowed between the Trade's fill price and the configured price for guaranteed Stop Loss Orders created for this instrument. Specified in price units.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "premium",
        "premium",
        "The amount that is charged to the account if a guaranteed Stop Loss Order is triggered and filled. The value is in price units and is charged for each unit of the Trade.",
        "primitive",
        "primitives.DecimalNumber",
        None,
        None
    ),
    Property(
        "levelRestriction",
        "levelRestriction",
        "The guaranteed Stop Loss Order level restriction for this instrument.",
        "object",
        "primitives.GuaranteedStopLossOrderLevelRestriction",
        None,
        None
    ),
]

pricing_common_PriceBucket = [
    Property(
        "price",
        "Price",
        "The Price offered by the PriceBucket",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "liquidity",
        "Liquidity",
        "The amount of liquidity offered by the PriceBucket",
        "primitive",
        "integer",
        None,
        None
    ),
]

pricing_common_Price = [
    Property(
        "instrument",
        "Instrument",
        "The Price's Instrument.",
        "primitive",
        "primitives.InstrumentName",
        None,
        None
    ),
    Property(
        "tradeable",
        "Is Tradeable",
        "Flag indicating if the Price is tradeable or not",
        "primitive",
        "boolean",
        None,
        None
    ),
    Property(
        "timestamp",
        "Timestamp",
        "The date/time when the Price was created.",
        "primitive",
        "primitives.DateTime",
        None,
        None
    ),
    Property(
        "baseBid",
        "Base Bid",
        "The base bid price as calculated by pricing.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "baseAsk",
        "Base Ask",
        "The base ask price as calculated by pricing.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "bids",
        "Bids",
        "The list of prices and liquidity available on the Instrument's bid side. It is possible for this list to be empty if there is no bid liquidity currently available for the Instrument in the Account.",
        "array_object",
        "PriceBucket",
        None,
        None
    ),
    Property(
        "asks",
        "Asks",
        "The list of prices and liquidity available on the Instrument's ask side. It is possible for this list to be empty if there is no ask liquidity currently available for the Instrument in the Account.",
        "array_object",
        "PriceBucket",
        None,
        None
    ),
    Property(
        "closeoutBid",
        "Closeout Bid",
        "The closeout bid price. This price is used when a bid is required to closeout a Position (margin closeout or manual) yet there is no bid liquidity. The closeout bid is never used to open a new position.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
    Property(
        "closeoutAsk",
        "Closeout Ask",
        "The closeout ask price. This price is used when an ask is required to closeout a Position (margin closeout or manual) yet there is no ask liquidity. The closeout ask is never used to open a new position.",
        "primitive",
        "pricing_common.PriceValue",
        None,
        None
    ),
]


