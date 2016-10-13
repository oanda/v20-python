import json
from v20.base_entity import BaseEntity
from v20.base_entity import Property
from v20.base_entity import EntityDict
from v20.request import Request



class UserInfo(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "username",
            "username",
            "The user-provided username.",
            "primitive",
            "string",
            False,
            None
        ),
        Property(
            "userID",
            "userID",
            "The user's OANDA-assigned user ID.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "country",
            "country",
            "The country that the user is based in.",
            "primitive",
            "string",
            False,
            None
        ),
        Property(
            "emailAddress",
            "emailAddress",
            "The user's email address.",
            "primitive",
            "string",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(UserInfo, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('username') is not None:
            body['username'] = \
                data.get('username')

        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('country') is not None:
            body['country'] = \
                data.get('country')

        if data.get('emailAddress') is not None:
            body['emailAddress'] = \
                data.get('emailAddress')

        self = UserInfo(**body)

        return self


class UserInfoExternal(BaseEntity):
    _summary_format = ""
    _name_format = ""

    _properties = [
        Property(
            "userID",
            "userID",
            "The user's OANDA-assigned user ID.",
            "primitive",
            "integer",
            False,
            None
        ),
        Property(
            "country",
            "country",
            "The country that the user is based in.",
            "primitive",
            "string",
            False,
            None
        ),
        Property(
            "FIFO",
            "FIFO",
            "Flag indicating if the the user's Accounts adhere to FIFO execution rules.",
            "primitive",
            "boolean",
            False,
            None
        ),
    ]

    def __init__(self, **kwargs):
        super(UserInfoExternal, self).__init__()
        for prop in self._properties:
            setattr(self, prop.name, kwargs.get(prop.name, prop.default))

    @staticmethod
    def from_dict(data):

        body = {}
        if data.get('userID') is not None:
            body['userID'] = \
                data.get('userID')

        if data.get('country') is not None:
            body['country'] = \
                data.get('country')

        if data.get('FIFO') is not None:
            body['FIFO'] = \
                data.get('FIFO')

        self = UserInfoExternal(**body)

        return self

class EntitySpec(object):
    UserInfo = UserInfo
    UserInfoExternal = UserInfoExternal

    def __init__(self, ctx):
        self.ctx = ctx


    def get(
        self,
        userSpecifier,
        **kwargs
    ):
        """User Info

        Fetch the user information for the specified user. This endpoint is
        intended to be used by the user themself to obtain their own
        information.

        Parameters
        ----------
        userSpecifier : 
            The specifier for the User to fetch user information for.
        """


        request = Request(
            'GET',
            '/v3/users/{userSpecifier}'
        )

        request.set_path_param(
            'userSpecifier',
            userSpecifier
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('userInfo') is not None:
                parsed_body['userInfo'] = \
                    UserInfo.from_dict(
                        jbody['userInfo']
                    )


        if str(response.status) == "401":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')


        if str(response.status) == "403":
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


    def get_external(
        self,
        userSpecifier,
        **kwargs
    ):
        """External User Info

        Fetch the externally-available user information for the specified user.
        This endpoint is intended to be used by 3rd parties that have been
        authorized by a user to view their personal information.

        Parameters
        ----------
        userSpecifier : 
            The specifier for the User to fetch user information for.
        """


        request = Request(
            'GET',
            '/v3/users/{userSpecifier}/externalInfo'
        )

        request.set_path_param(
            'userSpecifier',
            userSpecifier
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if str(response.status) == "200":
            if jbody.get('userInfo') is not None:
                parsed_body['userInfo'] = \
                    UserInfoExternal.from_dict(
                        jbody['userInfo']
                    )


        if str(response.status) == "401":
            if jbody.get('errorCode') is not None:
                parsed_body['errorCode'] = \
                    jbody.get('errorCode')

            if jbody.get('errorMessage') is not None:
                parsed_body['errorMessage'] = \
                    jbody.get('errorMessage')


        if str(response.status) == "403":
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

