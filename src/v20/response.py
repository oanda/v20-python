import requests
from v20.errors import ResponseUnexpectedStatus, ResponseNoField, V20Timeout, V20ConnectionError

class Response(object):
    def __init__(self, request, method, path, status, reason, headers):
        self.request = request
        self.method = method
        self.path = path
        self.status = status
        self.reason = reason
        self.headers = headers
        self.content_type = headers.get("content-type", None)
        self.raw_body = None
        self.body = None
        self.lines = None
        self.line_parser = None

    def set_raw_body(self, raw_body):
        self.raw_body = raw_body

    def set_lines(self, lines):
        self.lines = lines

    def set_line_parser(self, parser):
        self.line_parser = parser

    def get(self, field, status=None):
        if status is not None:
            if str(self.status) != str(status):
                raise ResponseUnexpectedStatus(self, status)

        value = self.body.get(field)

        if value is None:
            raise ResponseNoField(self, field)

        return value

    def parts(self):
        def line_parser(line):
            return "line", line

        parser = line_parser

        if self.line_parser is not None:
            parser = self.line_parser

        if self.lines is None:
            return

        try:
            for line in self.lines:
                yield parser(line)
        except requests.exceptions.ConnectionError:
            raise V20Timeout(self.path, "stream")
        except requests.exceptions.ChunkedEncodingError:
            raise V20ConnectionError(self.path)

    def __str__(self):
        s  = "Method = {}\n".format(self.method)
        s += "Path = {}\n".format(self.path)
        s += "Status = {}\n".format(self.status)
        s += "Reason = {}\n".format(self.reason)
        s += "Content-Type = {}\n".format(self.content_type)
        return s
