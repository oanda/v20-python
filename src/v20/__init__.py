import requests
from v20 import account
from v20 import transaction
from v20 import trade
from v20 import pricing
from v20 import position
from v20 import order
from v20.response import Response


class AuthenticationError(Exception):
    def __init__(self, username, status, reason):
        self.username = username
        self.status = status
        self.reason = reason

    def __str__(self):
        return "Authenticating {} resulted in a {} ({}) response".format(
            self.username,
            self.status,
            self.reason
        )


class Context(object):
    def __init__(self, hostname, port, ssl=False):
        """Create an API context for a specific host/port"""

        # Current username for the context
        self.username = None

        # Context headers to add to every request sent to the server
        self._headers = {
            "Content-Type": "application/json",
            "User-Agent": "OANDA/3.0.2 (client; python)"
        }

        # Current authentication token
        self.token = None

        # The list of accounts accessible for the current token
        self.token_account_ids = []

        # The base URL for every request made using the context
        self._base_url = "http{}://{}:{}".format(
            "s" if ssl else "",
            hostname,
            port
        )

        # The session used for communicating with the REST server
        self._session = requests.Session()

        self.account = account.EntitySpec(self)
        self.transaction = transaction.EntitySpec(self)
        self.trade = trade.EntitySpec(self)
        self.pricing = pricing.EntitySpec(self)
        self.position = position.EntitySpec(self)
        self.order = order.EntitySpec(self)

    def authenticate(self, username, password):
        """Log in using a username and password. Store the authorization token
        and fetch the list of Accounts accessible for that token"""
        # TODO write authorization module
        response = self.authorization.login(
            username=username,
            password=password
        )

        if response.status != 200:
            raise AuthenticationError(
                username,
                response.status,
                response.reason
            )

        self.set_token(response.body.get("token"))

        self.username = username

        response = self.account.list()

        self.token_account_ids = response.body.get("accounts")

    def set_token(self, token):
        self.token = token

        self.set_header(
            'Authorization',
            "Bearer {}".format(token)
        )

    def set_header(self, key, value):
        self._headers[key] = value

    def delete_header(self, key):
        if key in self._headers:
            del self._headers[key]

    def request(self, request):

        url = "{}{}".format(self._base_url, request.path)

        http_response = self._session.request(
            request.method,
            url,
            headers=self._headers,
            params=request.params,
            data=request.body,
            stream=request.stream
        )

        request.headers = http_response.request.headers

        response = Response(
            request,
            request.method,
            http_response.url,
            http_response.status_code,
            http_response.reason,
            http_response.headers
        )

        if request.stream:
            response.set_line_parser(
                request.line_parser
            )

            response.set_lines(
                http_response.iter_lines(1)
            )
        else:
            response.set_raw_body(http_response.text)

        return response
