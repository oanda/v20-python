import requests
from v20 import account
from v20 import transaction
from v20 import trade
from v20 import instrument
from v20 import pricing
from v20 import position
from v20 import order
from v20 import user
from v20.response import Response


class Context(object):
    """
    A v20.Context encapuslates a connection to OANDA's v20 REST API
    """
    def __init__(self, hostname, port, ssl=False, application=""):
        """
        Create an API context for v20 access

        Args:
            hostname: The hostname of the v20 REST server
            port: The port of the v20 REST server
            ssl: Flag to enable/disable SSL
            application: Optional name of the application using the v20 bindings
        """

        # Current username for the context
        self.username = None

        extensions = ""

        if application != "":
            extensions = " ({})".format(application)

        # The format to use when dealing with times
        self.datetime_format = "RFC3339"

        oanda_agent = "v20-python/3.0.7{}".format(extensions)

        # Context headers to add to every request sent to the server
        self._headers = {
            "Content-Type": "application/json",
            "OANDA-Agent": oanda_agent,
            "Accept-Datetime-Format": self.datetime_format
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

        # The size of each chunk to read when processing a stream
        # respons
        self.stream_chunk_size = 512

        self.account = account.EntitySpec(self)
        self.transaction = transaction.EntitySpec(self)
        self.trade = trade.EntitySpec(self)
        self.instrument = instrument.EntitySpec(self)
        self.pricing = pricing.EntitySpec(self)
        self.position = position.EntitySpec(self)
        self.order = order.EntitySpec(self)
        self.user = user.EntitySpec(self)


    def set_header(self, key, value):
        """
        Set an HTTP header for all requests to the v20 API using 
        this context
        """

        self._headers[key] = value


    def delete_header(self, key):
        """
        Remove an HTTP header from the context
        """
        if key in self._headers:
            del self._headers[key]


    def set_token(self, token):
        """
        Set the token for the v20 context

        Args:
            token: The token used to access the v20 REST api
        """

        self.token = token

        self.set_header(
            'Authorization',
            "Bearer {}".format(token)
        )


    def set_datetime_format(self, format):
        """
        Set the Accept-Datetime-Format header to an acceptable
        value
        """
        if not format in ["UNIX", "RFC3330"]:
            return

        self.datetime_format = format

        self.set_header("Accept-Datetime-Format", self.datetime_format)


    def set_datetime_format_unix(self):
        """
        Set the datetime format for the context to UNIX
        """
        self.set_datetime_format("UNIX")


    def set_datetime_format_rfc3339(self):
        """
        Set the datetime format for the context to RFC3339
        """
        self.set_datetime_format("RFC3339")


    def datetime_to_str(self, dt):
        """
        Format a datetime object as a string depending on how the
        context has been configured.
        """

        if self.datetime_format == "UNIX":
            return dt.strftime("%s.000000000")

        return dt.strftime("%Y-%m-%dT%H:%M:%S.000000000Z")


    def set_stream_chunk_size(self, size):
        self.stream_chunk_size = size


    def request(self, request):
        """
        Perform an HTTP request through the context

        Args:
            request: A v20.request.Request object

        Returns:
            A v20.response.Response object
        """
        
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
                http_response.iter_lines(
                    self.stream_chunk_size
                )
            )
        else:
            response.set_raw_body(http_response.text)

        return response
