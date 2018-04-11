class V20ConnectionError(Exception):
    """
    A V20ConnectionError is raised when a connection to the V20 REST
    server was not possible.
    """
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return "Connection to v20 REST server at {} failed".format(
            self.url
        )


class V20Timeout(Exception):
    """
    A V20Timeout is raised when attempting to interract with the V20 REST
    server has timed out.
    """
    def __init__(self, url, type):
        self.url = url
        self.type = type

    def __str__(self):
        return "v20 REST request to {} has timed out ({})".format(
            self.url,
            self.type
        )


class ResponseUnexpectedStatus(Exception):
    """
    A ResponseUnexpectedStatus exception is raised when a certain HTTP status
    code is expected in a response however a differend status code has
    been received.
    """
    def __init__(self, response, expected_status):
        self.response = response
        self.expected_status = expected_status

    def __str__(self):
        return "{} {} expected status {}, got {} ({})".format(
            self.response.method,
            self.response.path,
            self.expected_status,
            self.response.status,
            self.response.reason
        )


class ResponseUnexpectedStatus(Exception):
    """
    A ResponseUnexpectedStatus exception is raised when a certain HTTP status
    code is expected in a response however a differend status code has
    been received.
    """
    def __init__(self, response, expected_status):
        self.response = response
        self.expected_status = expected_status

    def __str__(self):
        return "{} {} expected status {}, got {} ({})".format(
            self.response.method,
            self.response.path,
            self.expected_status,
            self.response.status,
            self.response.reason
        )


class ResponseNoField(Exception):
    """
    A ResponseNoField exception is raised when a specific field is
    expected in the body of a HTTP response however it does not exist.
    """
    def __init__(self, response, field):
        self.response = response
        self.field = field

    def __str__(self):
        contains = ", ".join(
            ["'{}'".format(f) for f in self.response.body.keys()]
        )
        return "{} response for {} {} does not have field '{}' (contains {})".format(
            self.response.status,
            self.response.method,
            self.response.path,
            self.field,
            contains
        )
