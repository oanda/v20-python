import ujson as json
from v20.base_entity import BaseEntity
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import spec_properties



class Position(BaseEntity):
    """
    The specification of a Position within an Account.
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "{instrument}, {pl} PL {unrealizedPL} UPL"

    #
    # Format string used when generating a name for this object
    #
    _name_format = "Position"

    #
    # Property metadata for this object
    #
    _properties = spec_properties.position_Position

    def __init__(self, **kwargs):
        """
        Create a new Position instance
        """
        super(Position, self).__init__()
 
        #
        # The Position's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # Profit/loss realized by the Position over the lifetime of the
        # Account.
        #
        self.pl = kwargs.get("pl")
 
        #
        # The unrealized profit/loss of all open Trades that contribute to this
        # Position.
        #
        self.unrealizedPL = kwargs.get("unrealizedPL")
 
        #
        # Margin currently used by the Position.
        #
        self.marginUsed = kwargs.get("marginUsed")
 
        #
        # Profit/loss realized by the Position since the Account's resettablePL
        # was last reset by the client.
        #
        self.resettablePL = kwargs.get("resettablePL")
 
        #
        # The total amount of financing paid/collected for this instrument over
        # the lifetime of the Account.
        #
        self.financing = kwargs.get("financing")
 
        #
        # The total amount of commission paid for this instrument over the
        # lifetime of the Account.
        #
        self.commission = kwargs.get("commission")
 
        #
        # The total amount of fees charged over the lifetime of the Account for
        # the execution of guaranteed Stop Loss Orders for this instrument.
        #
        self.guaranteedExecutionFees = kwargs.get("guaranteedExecutionFees")
 
        #
        # The details of the long side of the Position.
        #
        self.long = kwargs.get("long")
 
        #
        # The details of the short side of the Position.
        #
        self.short = kwargs.get("short")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new Position from a dict (generally from loading a JSON
        response). The data used to instantiate the Position is a shallow copy
        of the dict passed in, with any complex child types instantiated
        appropriately.
        """

        data = data.copy()

        if data.get('pl') is not None:
            data['pl'] = ctx.convert_decimal_number(
                data.get('pl')
            )

        if data.get('unrealizedPL') is not None:
            data['unrealizedPL'] = ctx.convert_decimal_number(
                data.get('unrealizedPL')
            )

        if data.get('marginUsed') is not None:
            data['marginUsed'] = ctx.convert_decimal_number(
                data.get('marginUsed')
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

        if data.get('long') is not None:
            data['long'] = \
                ctx.position.PositionSide.from_dict(
                    data['long'], ctx
                )

        if data.get('short') is not None:
            data['short'] = \
                ctx.position.PositionSide.from_dict(
                    data['short'], ctx
                )

        return Position(**data)


class PositionSide(BaseEntity):
    """
    The representation of a Position for a single direction (long or short).
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = "{units} @ {averagePrice}, {pl} PL {unrealizedPL} UPL"

    #
    # Format string used when generating a name for this object
    #
    _name_format = ""

    #
    # Property metadata for this object
    #
    _properties = spec_properties.position_PositionSide

    def __init__(self, **kwargs):
        """
        Create a new PositionSide instance
        """
        super(PositionSide, self).__init__()
 
        #
        # Number of units in the position (negative value indicates short
        # position, positive indicates long position).
        #
        self.units = kwargs.get("units")
 
        #
        # Volume-weighted average of the underlying Trade open prices for the
        # Position.
        #
        self.averagePrice = kwargs.get("averagePrice")
 
        #
        # List of the open Trade IDs which contribute to the open Position.
        #
        self.tradeIDs = kwargs.get("tradeIDs")
 
        #
        # Profit/loss realized by the PositionSide over the lifetime of the
        # Account.
        #
        self.pl = kwargs.get("pl")
 
        #
        # The unrealized profit/loss of all open Trades that contribute to this
        # PositionSide.
        #
        self.unrealizedPL = kwargs.get("unrealizedPL")
 
        #
        # Profit/loss realized by the PositionSide since the Account's
        # resettablePL was last reset by the client.
        #
        self.resettablePL = kwargs.get("resettablePL")
 
        #
        # The total amount of financing paid/collected for this PositionSide
        # over the lifetime of the Account.
        #
        self.financing = kwargs.get("financing")
 
        #
        # The total amount of fees charged over the lifetime of the Account for
        # the execution of guaranteed Stop Loss Orders attached to Trades for
        # this PositionSide.
        #
        self.guaranteedExecutionFees = kwargs.get("guaranteedExecutionFees")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new PositionSide from a dict (generally from loading a
        JSON response). The data used to instantiate the PositionSide is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('units') is not None:
            data['units'] = ctx.convert_decimal_number(
                data.get('units')
            )

        if data.get('averagePrice') is not None:
            data['averagePrice'] = ctx.convert_decimal_number(
                data.get('averagePrice')
            )


        if data.get('pl') is not None:
            data['pl'] = ctx.convert_decimal_number(
                data.get('pl')
            )

        if data.get('unrealizedPL') is not None:
            data['unrealizedPL'] = ctx.convert_decimal_number(
                data.get('unrealizedPL')
            )

        if data.get('resettablePL') is not None:
            data['resettablePL'] = ctx.convert_decimal_number(
                data.get('resettablePL')
            )

        if data.get('financing') is not None:
            data['financing'] = ctx.convert_decimal_number(
                data.get('financing')
            )

        if data.get('guaranteedExecutionFees') is not None:
            data['guaranteedExecutionFees'] = ctx.convert_decimal_number(
                data.get('guaranteedExecutionFees')
            )

        return PositionSide(**data)


class CalculatedPositionState(BaseEntity):
    """
    The dynamic (calculated) state of a Position
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
    _properties = spec_properties.position_CalculatedPositionState

    def __init__(self, **kwargs):
        """
        Create a new CalculatedPositionState instance
        """
        super(CalculatedPositionState, self).__init__()
 
        #
        # The Position's Instrument.
        #
        self.instrument = kwargs.get("instrument")
 
        #
        # The Position's net unrealized profit/loss
        #
        self.netUnrealizedPL = kwargs.get("netUnrealizedPL")
 
        #
        # The unrealized profit/loss of the Position's long open Trades
        #
        self.longUnrealizedPL = kwargs.get("longUnrealizedPL")
 
        #
        # The unrealized profit/loss of the Position's short open Trades
        #
        self.shortUnrealizedPL = kwargs.get("shortUnrealizedPL")
 
        #
        # Margin currently used by the Position.
        #
        self.marginUsed = kwargs.get("marginUsed")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new CalculatedPositionState from a dict (generally from
        loading a JSON response). The data used to instantiate the
        CalculatedPositionState is a shallow copy of the dict passed in, with
        any complex child types instantiated appropriately.
        """

        data = data.copy()

        if data.get('netUnrealizedPL') is not None:
            data['netUnrealizedPL'] = ctx.convert_decimal_number(
                data.get('netUnrealizedPL')
            )

        if data.get('longUnrealizedPL') is not None:
            data['longUnrealizedPL'] = ctx.convert_decimal_number(
                data.get('longUnrealizedPL')
            )

        if data.get('shortUnrealizedPL') is not None:
            data['shortUnrealizedPL'] = ctx.convert_decimal_number(
                data.get('shortUnrealizedPL')
            )

        if data.get('marginUsed') is not None:
            data['marginUsed'] = ctx.convert_decimal_number(
                data.get('marginUsed')
            )

        return CalculatedPositionState(**data)


class EntitySpec(object):
    """
    The position.EntitySpec wraps the position module's type definitions
    and API methods so they can be easily accessed through an instance of a v20
    Context.
    """

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
        """
        List all Positions for an Account. The Positions returned are for every
        instrument that has had a position during the lifetime of an the
        Account.

        Args:
            accountID:
                Account Identifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('positions') is not None:
                parsed_body['positions'] = [
                    self.ctx.position.Position.from_dict(d, self.ctx)
                    for d in jbody.get('positions')
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


    def list_open(
        self,
        accountID,
        **kwargs
    ):
        """
        List all open Positions for an Account. An open Position is a Position
        in an Account that currently has a Trade opened for it.

        Args:
            accountID:
                Account Identifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('positions') is not None:
                parsed_body['positions'] = [
                    self.ctx.position.Position.from_dict(d, self.ctx)
                    for d in jbody.get('positions')
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
        instrument,
        **kwargs
    ):
        """
        Get the details of a single Instrument's Position in an Account. The
        Position may by open or not.

        Args:
            accountID:
                Account Identifier
            instrument:
                Name of the Instrument

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('position') is not None:
                parsed_body['position'] = \
                    self.ctx.position.Position.from_dict(
                        jbody['position'],
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


    def close(
        self,
        accountID,
        instrument,
        **kwargs
    ):
        """
        Closeout the open Position for a specific instrument in an Account.

        Args:
            accountID:
                Account Identifier
            instrument:
                Name of the Instrument
            longUnits:
                Indication of how much of the long Position to closeout. Either
                the string "ALL", the string "NONE", or a DecimalNumber
                representing how many units of the long position to close using
                a PositionCloseout MarketOrder. The units specified must always
                be positive.
            longClientExtensions:
                The client extensions to add to the MarketOrder used to close
                the long position.
            shortUnits:
                Indication of how much of the short Position to closeout.
                Either the string "ALL", the string "NONE", or a DecimalNumber
                representing how many units of the short position to close
                using a PositionCloseout MarketOrder. The units specified must
                always be positive.
            shortClientExtensions:
                The client extensions to add to the MarketOrder used to close
                the short position.

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        if 'longUnits' in kwargs:
            body.set('longUnits', kwargs['longUnits'])

        if 'longClientExtensions' in kwargs:
            body.set('longClientExtensions', kwargs['longClientExtensions'])

        if 'shortUnits' in kwargs:
            body.set('shortUnits', kwargs['shortUnits'])

        if 'shortClientExtensions' in kwargs:
            body.set('shortClientExtensions', kwargs['shortClientExtensions'])

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
            if jbody.get('longOrderCreateTransaction') is not None:
                parsed_body['longOrderCreateTransaction'] = \
                    self.ctx.transaction.MarketOrderTransaction.from_dict(
                        jbody['longOrderCreateTransaction'],
                        self.ctx
                    )

            if jbody.get('longOrderFillTransaction') is not None:
                parsed_body['longOrderFillTransaction'] = \
                    self.ctx.transaction.OrderFillTransaction.from_dict(
                        jbody['longOrderFillTransaction'],
                        self.ctx
                    )

            if jbody.get('longOrderCancelTransaction') is not None:
                parsed_body['longOrderCancelTransaction'] = \
                    self.ctx.transaction.OrderCancelTransaction.from_dict(
                        jbody['longOrderCancelTransaction'],
                        self.ctx
                    )

            if jbody.get('shortOrderCreateTransaction') is not None:
                parsed_body['shortOrderCreateTransaction'] = \
                    self.ctx.transaction.MarketOrderTransaction.from_dict(
                        jbody['shortOrderCreateTransaction'],
                        self.ctx
                    )

            if jbody.get('shortOrderFillTransaction') is not None:
                parsed_body['shortOrderFillTransaction'] = \
                    self.ctx.transaction.OrderFillTransaction.from_dict(
                        jbody['shortOrderFillTransaction'],
                        self.ctx
                    )

            if jbody.get('shortOrderCancelTransaction') is not None:
                parsed_body['shortOrderCancelTransaction'] = \
                    self.ctx.transaction.OrderCancelTransaction.from_dict(
                        jbody['shortOrderCancelTransaction'],
                        self.ctx
                    )

            if jbody.get('relatedTransactionIDs') is not None:
                parsed_body['relatedTransactionIDs'] = \
                    jbody.get('relatedTransactionIDs')

            if jbody.get('lastTransactionID') is not None:
                parsed_body['lastTransactionID'] = \
                    jbody.get('lastTransactionID')

        elif str(response.status) == "400":
            if jbody.get('longOrderRejectTransaction') is not None:
                parsed_body['longOrderRejectTransaction'] = \
                    self.ctx.transaction.MarketOrderRejectTransaction.from_dict(
                        jbody['longOrderRejectTransaction'],
                        self.ctx
                    )

            if jbody.get('shortOrderRejectTransaction') is not None:
                parsed_body['shortOrderRejectTransaction'] = \
                    self.ctx.transaction.MarketOrderRejectTransaction.from_dict(
                        jbody['shortOrderRejectTransaction'],
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
            if jbody.get('longOrderRejectTransaction') is not None:
                parsed_body['longOrderRejectTransaction'] = \
                    self.ctx.transaction.MarketOrderRejectTransaction.from_dict(
                        jbody['longOrderRejectTransaction'],
                        self.ctx
                    )

            if jbody.get('shortOrderRejectTransaction') is not None:
                parsed_body['shortOrderRejectTransaction'] = \
                    self.ctx.transaction.MarketOrderRejectTransaction.from_dict(
                        jbody['shortOrderRejectTransaction'],
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

