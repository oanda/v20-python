import json
from base_entity import BaseEntity
from base_entity import Property
from base_entity import EntityDict
from request import Request


class EntitySpec(object):

    def __init__(self, ctx):
        self.ctx = ctx


    def login(
        self,
        **kwargs
    ):
        """Login

        Obtain an authorization token for a client using their username and
        password.

        Parameters
        ----------
        username : string, optional
            The client's username.
        password : string, optional
            The client's password.
        """


        request = Request(
            'POST',
            '/v3/login'
        )

        body = EntityDict()

        body.set('username', kwargs.get('username'))

        body.set('password', kwargs.get('password'))

        request.set_body_dict(body.dict)

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if response.status is 200:
            if jbody.get('token') is not None:
                parsed_body['token'] = \
                    jbody.get('token')


        if response.status is 400:
            parsed_body = jbody

        if response.status is 401:
            parsed_body = jbody

        if response.status is 405:
            parsed_body = jbody

        response.body = parsed_body

        return response


    def logout(
        self,
        **kwargs
    ):
        """Logout

        Invalidate a client's authorization token.

        Parameters
        ----------
        """


        request = Request(
            'POST',
            '/v3/logout'
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        if response.status is 200:
            parsed_body = jbody

        if response.status is 400:
            parsed_body = jbody

        if response.status is 405:
            parsed_body = jbody

        response.body = parsed_body

        return response

