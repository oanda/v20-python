import json
from v20.base_entity import BaseEntity
from v20.base_entity import Property
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import transaction



class Position(BaseEntity):
    _summary_format = "{instrument}, {pl} PL {unrealizedPL} UPL"
    _name_format = "Position"

    _properties = [
        Property(
            "instrument",
            "instrument",
            "The Position's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            False,
            None
        ),
        Property(
            "pl",
            "pl",
            "Profit/loss realized by the Position over the lifetime of the Account.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "unrealizedPL",
            "unrealizedPL",
            "The unrealized profit/loss of all open Trades that contribute to this Position.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "resettablePL",
            "resettablePL",
            "Profit/loss realized by the Position since the Account's resettablePL was last reset by the client.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "long",
            "long",
            "The details of the long side of the Position.",
            "object",
            "position.PositionSide",
            False,
            None
        ),
        Property(
            "short",
            "short",
            "The details of the short side of the Position.",
            "object",
            "position.PositionSide",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(Position, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('pl') is not None:
            body['pl'] = \
                data.get('pl')

        if data.get('unrealizedPL') is not None:
            body['unrealizedPL'] = \
                data.get('unrealizedPL')

        if data.get('resettablePL') is not None:
            body['resettablePL'] = \
                data.get('resettablePL')

        if data.get('long') is not None:
            body['long'] = \
                PositionSide.from_dict(
                    data['long']
                )

        if data.get('short') is not None:
            body['short'] = \
                PositionSide.from_dict(
                    data['short']
                )

        self = Position(**body)

        return self


class PositionSide(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "units",
            "units",
            "Number of units in the position (negative value indicates short position, positive indicates long position).",
            "primitive",
            "primitives.DecimalNumber",
            False,
            None
        ),
        Property(
            "averagePrice",
            "averagePrice",
            "Volume-weighted average of the underlying Trade open prices for the Position.",
            "primitive",
            "pricing.PriceValue",
            False,
            None
        ),
        Property(
            "tradeIDs",
            "tradeIDs",
            "List of the open Trade IDs which contribute to the open Position.",
            "array_primitive",
            "TradeID",
            False,
            None
        ),
        Property(
            "pl",
            "pl",
            "Profit/loss realized by the PositionSide over the lifetime of the Account.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "unrealizedPL",
            "unrealizedPL",
            "The unrealized profit/loss of all open Trades that contribute to this PositionSide.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "resettablePL",
            "resettablePL",
            "Profit/loss realized by the PositionSide since the Account's resettablePL was last reset by the client.",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(PositionSide, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('units') is not None:
            body['units'] = \
                data.get('units')

        if data.get('averagePrice') is not None:
            body['averagePrice'] = \
                data.get('averagePrice')

        if data.get('tradeIDs') is not None:
            body['tradeIDs'] = \
                data.get('tradeIDs')

        if data.get('pl') is not None:
            body['pl'] = \
                data.get('pl')

        if data.get('unrealizedPL') is not None:
            body['unrealizedPL'] = \
                data.get('unrealizedPL')

        if data.get('resettablePL') is not None:
            body['resettablePL'] = \
                data.get('resettablePL')

        self = PositionSide(**body)

        return self


class CalculatedPositionState(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "instrument",
            "instrument",
            "The Position's Instrument.",
            "primitive",
            "primitives.InstrumentName",
            False,
            None
        ),
        Property(
            "netUnrealizedPL",
            "netUnrealizedPL",
            "The Position's net unrealized profit/loss",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "longUnrealizedPL",
            "longUnrealizedPL",
            "The unrealized profit/loss of the Position's long open Trades",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
        Property(
            "shortUnrealizedPL",
            "shortUnrealizedPL",
            "The unrealized profit/loss of the Position's short open Trades",
            "primitive",
            "primitives.AccountUnits",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(CalculatedPositionState, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('instrument') is not None:
            body['instrument'] = \
                data.get('instrument')

        if data.get('netUnrealizedPL') is not None:
            body['netUnrealizedPL'] = \
                data.get('netUnrealizedPL')

        if data.get('longUnrealizedPL') is not None:
            body['longUnrealizedPL'] = \
                data.get('longUnrealizedPL')

        if data.get('shortUnrealizedPL') is not None:
            body['shortUnrealizedPL'] = \
                data.get('shortUnrealizedPL')

        self = CalculatedPositionState(**body)

        return self

class EntitySpec(object):
    Position = Position
    PositionSide = PositionSide
    CalculatedPositionState = CalculatedPositionState

    def __init__(self, ctx):
        self.ctx = ctx


    def list(
        self,
        accountID,
        **kwargs
    ):
        """List Positions

        List all Positions for an Account. The Positions returned are for every
        instrument that has had a position during the lifetime of an the
        Account.

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch Positions for.
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/positions'
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
            if jbody.get('positions') is not None:
                parsed_body['positions'] = [
                    Position.from_dict(d)
                    for d in jbody.get('positions')
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
        """Open Positions

        List all open Positions for an Account. An open Position is a Position
        in an Account that currently has a Trade opened for it.

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch open Positions for.
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/openPositions'
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
            if jbody.get('positions') is not None:
                parsed_body['positions'] = [
                    Position.from_dict(d)
                    for d in jbody.get('positions')
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
        instrument,
        **kwargs
    ):
        """Instrument Position

        Get the details of a single Instrument's Position in an Account. The
        Position may by open or not.

        Parameters
        ----------
        accountID : 
            ID of the Account to fetch Positions for.
        instrument : 
            Name of the Instrument fetch the Position of.
        """


        request = Request(
            'GET',
            '/v3/accounts/{accountID}/positions/{instrument}'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'instrument',
            instrument
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('position') is not None:
                parsed_body['position'] = \
                    Position.from_dict(
                        jbody['position']
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
        instrument,
        **kwargs
    ):
        """Close Position

        Closeout the open Position for a specific instrument in an Account.

        Parameters
        ----------
        accountID : 
            ID of the Account to close a Position in.
        instrument : 
            Name of the Instrument to close the Positon of.
        longUnits : string, optional
            Indication of how much of the long Position to closeout. Either the
            string "ALL", the string "NONE", or a DecimalNumber representing
            how many units of the long position to close using a
            PositionCloseout MarketOrder. The units specified must always be
            positive.
        longClientExtensions : None, optional
            The client extensions to add to the MarketOrder used to close the
            long position.
        shortUnits : string, optional
            Indication of how much of the short Position to closeout. Either
            the string "ALL", the string "NONE", or a DecimalNumber
            representing how many units of the short position to close using a
            PositionCloseout MarketOrder. The units specified must always be
            positive.
        shortClientExtensions : None, optional
            The client extensions to add to the MarketOrder used to close the
            short position.
        """


        request = Request(
            'PUT',
            '/v3/accounts/{accountID}/positions/{instrument}/close'
        )

        request.set_path_param(
            'accountID',
            accountID
        )

        request.set_path_param(
            'instrument',
            instrument
        )

        body = EntityDict()

        body.set('longUnits', kwargs.get('longUnits'))

        body.set('longClientExtensions', kwargs.get('longClientExtensions'))

        body.set('shortUnits', kwargs.get('shortUnits'))

        body.set('shortClientExtensions', kwargs.get('shortClientExtensions'))

        request.set_body_dict(body.dict)

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('longOrderCreateTransaction') is not None:
                parsed_body['longOrderCreateTransaction'] = \
                    transaction.MarketOrderTransaction.from_dict(
                        jbody['longOrderCreateTransaction']
                    )

            if jbody.get('longOrderFillTransaction') is not None:
                parsed_body['longOrderFillTransaction'] = \
                    transaction.OrderFillTransaction.from_dict(
                        jbody['longOrderFillTransaction']
                    )

            if jbody.get('longOrderCancelTransaction') is not None:
                parsed_body['longOrderCancelTransaction'] = \
                    transaction.OrderCancelTransaction.from_dict(
                        jbody['longOrderCancelTransaction']
                    )

            if jbody.get('shortOrderCreateTransaction') is not None:
                parsed_body['shortOrderCreateTransaction'] = \
                    transaction.MarketOrderTransaction.from_dict(
                        jbody['shortOrderCreateTransaction']
                    )

            if jbody.get('shortOrderFillTransaction') is not None:
                parsed_body['shortOrderFillTransaction'] = \
                    transaction.OrderFillTransaction.from_dict(
                        jbody['shortOrderFillTransaction']
                    )

            if jbody.get('shortOrderCancelTransaction') is not None:
                parsed_body['shortOrderCancelTransaction'] = \
                    transaction.OrderCancelTransaction.from_dict(
                        jbody['shortOrderCancelTransaction']
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')


        if str(response.status) == "400":
            if jbody.get('longOrderRejectTransaction') is not None:
                parsed_body['longOrderRejectTransaction'] = \
                    transaction.MarketOrderRejectTransaction.from_dict(
                        jbody['longOrderRejectTransaction']
                    )

            if jbody.get('shortOrderRejectTransaction') is not None:
                parsed_body['shortOrderRejectTransaction'] = \
                    transaction.MarketOrderRejectTransaction.from_dict(
                        jbody['shortOrderRejectTransaction']
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

