import requests
from v20 import instrument
from v20 import position
from v20 import trade
from v20 import site
from v20 import primitives
from v20 import account
from v20 import transaction
from v20 import user
from v20 import pricing
from v20 import order
from v20 import pricing_common
from v20.response import Response
from v20.errors import V20ConnectionError, V20Timeout

class Context(object):
    """
    A v20.Context encapuslates a connection to OANDA's v20 REST API
    """
    def __init__(
        self,
        hostname,
        port=443,
        ssl=True,
        application="",
        token=None,
        decimal_number_as_float=True,
        stream_chunk_size=512,
        stream_timeout=10,
        datetime_format="RFC3339",
        poll_timeout=2
    ):
        """
        Create an API context for v20 access

        Args:
            hostname: The hostname of the v20 REST server
            port: The port of the v20 REST server
            ssl: Flag to enable/disable SSL
            application: Optional name of the application using the v20 bindings
            token: The authorization token to use when making requests to the
                v20 server
            decimal_number_as_float: Flag that controls whether the string
                representation of floats received from the server should be
                converted into floats or not
            stream_chunk_size: The size of each chunk to read when processing a
                stream response
            stream_timeout: The timeout to use when making a stream request
                with the v20 REST server
            datetime_format: The format to request when dealing with times
            poll_timeout: The timeout to use when making a polling request with
                the v20 REST server
        """

        #
        # V20 REST server hostname
        #
        self.hostname = hostname

        #
        # V20 REST server port
        #
        self.port = port

        #
        # The format to use when dealing with times
        #
        self.datetime_format = datetime_format

        #
        # Form the value for the OANDA-Agent header
        #
        extensions = ""

        if application != "":
            extensions = " ({})".format(application)

        oanda_agent = "v20-python/3.0.25{}".format(extensions)

        #
        # Context headers to add to every request sent to the server
        #
        self._headers = {
            "Content-Type": "application/json",
            "OANDA-Agent": oanda_agent,
            "Accept-Datetime-Format": self.datetime_format
        }

        #
        # Current authentication token
        #
        self.token = None

        if token is not None:
            self.set_token(token)

        #
        # The base URL for every request made using the context
        #
        self._base_url = "http{}://{}:{}".format(
            "s" if ssl else "",
            hostname,
            port
        )

        #
        # The session used for communicating with the REST server
        #
        self._session = requests.Session()

        #
        # Flag that controls whether the string representation of floats
        # received from the server should be converted into floats or not
        #
        self.decimal_number_as_float = decimal_number_as_float

        #
        # The size of each chunk to read when processing a stream
        # response
        #
        self.stream_chunk_size = stream_chunk_size

        #
        # The timeout to use when making a stream request with the
        # v20 REST server
        #
        self.stream_timeout = stream_timeout

        #
        # The timeout to use when making a polling request with the
        # v20 REST server
        #
        self.poll_timeout = poll_timeout

        self.instrument = instrument.EntitySpec(self)
        self.position = position.EntitySpec(self)
        self.trade = trade.EntitySpec(self)
        self.site = site.EntitySpec(self)
        self.primitives = primitives.EntitySpec(self)
        self.account = account.EntitySpec(self)
        self.transaction = transaction.EntitySpec(self)
        self.user = user.EntitySpec(self)
        self.pricing = pricing.EntitySpec(self)
        self.order = order.EntitySpec(self)
        self.pricing_common = pricing_common.EntitySpec(self)


    def set_header(self, key, value):
        """
        Set an HTTP header for all requests to the v20 API using
        this context

        Args:
            key: header key to set
            value: header value
        """

        self._headers[key] = value


    def delete_header(self, key):
        """
        Remove an HTTP header from the context

        Args:
            key: header key to remove
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

        Args:
            format: UNIX or RFC3339
        """
        if not format in ["UNIX", "RFC3339"]:
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

        Args:
            dt: A datetime object to convert to a string
        """

        if self.datetime_format == "UNIX":
            return dt.strftime("%s.000000000")

        return dt.strftime("%Y-%m-%dT%H:%M:%S.000000000Z")


    def set_convert_decimal_number_to_native(self, value):
        """
        Enable or disable the conversion of string-represented decimal
        numbers to native format (floats).

        Args:
            value: True of False to enable/disable this feature
        """
        self.decimal_number_as_float = value


    def convert_decimal_number(self, value):
        """
        Parse a wire-format DecimalNumber, AccountValue or PriceValue (i.e. a
        string-formatted float) either to a float or leave as a string
        depending on how the context is configured

        Args:
            value: A string representation of a float to parse
        """
        if self.decimal_number_as_float:
            return float(value)

        return value


    def set_stream_chunk_size(self, size):
        """
        Set the chunk size when iterating over the lines of a stream response
        """
        self.stream_chunk_size = size


    def set_stream_timeout(self, timeout):
        """
        Set the timeout for stream requests
        """
        self.stream_timeout = timeout


    def set_poll_timeout(self, timeout):
        """
        Set the timeout for poll requests
        """
        self.poll_timeout = timeout


    def request(self, request):
        """
        Perform an HTTP request through the context

        Args:
            request: A v20.request.Request object

        Returns:
            A v20.response.Response object
        """

        url = "{}{}".format(self._base_url, request.path)

        timeout = self.poll_timeout

        if request.stream is True:
            timeout = self.stream_timeout

        try:
            http_response = self._session.request(
                request.method,
                url,
                headers=self._headers,
                params=request.params,
                data=request.body,
                stream=request.stream,
                timeout=timeout
            )
        except requests.exceptions.ConnectionError:
            raise V20ConnectionError(url)
        except requests.exceptions.ConnectTimeout:
            raise V20Timeout(url, "connect")
        except requests.exceptions.ReadTimeout:
            raise V20Timeout(url, "read")

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
