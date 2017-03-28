import ujson as json
from v20.base_entity import BaseEntity
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import spec_properties



class UserInfo(BaseEntity):
    """
    A representation of user information, as provided to the user themself.
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
    _properties = spec_properties.user_UserInfo

    def __init__(self, **kwargs):
        """
        Create a new UserInfo instance
        """
        super(UserInfo, self).__init__()
 
        #
        # The user-provided username.
        #
        self.username = kwargs.get("username")
 
        #
        # The user's OANDA-assigned user ID.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The country that the user is based in.
        #
        self.country = kwargs.get("country")
 
        #
        # The user's email address.
        #
        self.emailAddress = kwargs.get("emailAddress")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new UserInfo from a dict (generally from loading a JSON
        response). The data used to instantiate the UserInfo is a shallow copy
        of the dict passed in, with any complex child types instantiated
        appropriately.
        """

        data = data.copy()

        return UserInfo(**data)


class UserInfoExternal(BaseEntity):
    """
    A representation of user information, as available to external (3rd party)
    clients.
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
    _properties = spec_properties.user_UserInfoExternal

    def __init__(self, **kwargs):
        """
        Create a new UserInfoExternal instance
        """
        super(UserInfoExternal, self).__init__()
 
        #
        # The user's OANDA-assigned user ID.
        #
        self.userID = kwargs.get("userID")
 
        #
        # The country that the user is based in.
        #
        self.country = kwargs.get("country")
 
        #
        # Flag indicating if the the user's Accounts adhere to FIFO execution
        # rules.
        #
        self.FIFO = kwargs.get("FIFO")

    @staticmethod
    def from_dict(data, ctx):
        """
        Instantiate a new UserInfoExternal from a dict (generally from loading
        a JSON response). The data used to instantiate the UserInfoExternal is
        a shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        return UserInfoExternal(**data)


class EntitySpec(object):
    """
    The user.EntitySpec wraps the user module's type definitions
    and API methods so they can be easily accessed through an instance of a v20
    Context.
    """

    UserInfo = UserInfo
    UserInfoExternal = UserInfoExternal

    def __init__(self, ctx):
        self.ctx = ctx


    def get_info(
        self,
        userSpecifier,
        **kwargs
    ):
        """
        Fetch the user information for the specified user. This endpoint is
        intended to be used by the user themself to obtain their own
        information.

        Args:
            userSpecifier:
                The User Specifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('userInfo') is not None:
                parsed_body['userInfo'] = \
                    self.ctx.user.UserInfo.from_dict(
                        jbody['userInfo'],
                        self.ctx
                    )

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


    def get_external_info(
        self,
        userSpecifier,
        **kwargs
    ):
        """
        Fetch the externally-available user information for the specified user.
        This endpoint is intended to be used by 3rd parties that have been
        authorized by a user to view their personal information.

        Args:
            userSpecifier:
                The User Specifier

        Returns:
            v20.response.Response containing the results from submitting the
            request
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

        #
        # Parse responses as defined by the API specification
        #
        if str(response.status) == "200":
            if jbody.get('userInfo') is not None:
                parsed_body['userInfo'] = \
                    self.ctx.user.UserInfoExternal.from_dict(
                        jbody['userInfo'],
                        self.ctx
                    )

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

