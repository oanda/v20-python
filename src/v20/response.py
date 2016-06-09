class UnexpectedStatusError(Exception):
    def __init__(self, method, path, status, expectedStatus):
        self.method = method
        self.path = path
        self.status = status
        self.expectedStatus = expectedStatus

    def __str__(self):
        return "{} {} returned unexpected status {} (expected {})".format(
            self.method,
            self.path,
            self.status,
            self.expectedStatus
        )


class NoSuchValueError(Exception):
    def __init__(self, method, path, status, key, availableKeys):
        self.method = method
        self.path = path
        self.status = status
        self.key = key
        self.availableKeys = availableKeys

    def __str__(self):
        return "{} {} result {} does not have field '{}' (available keys are {})".format(
            self.method,
            self.path,
            self.status,
            self.key,
            self.availableKeys
        )


class Response(object):
    def __init__(self, method, path, status, reason, content_type):
        self.method = method
        self.path = path
        self.status = status
        self.reason = reason
        self.content_type = content_type
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

    def parts(self):
        def line_parser(line):
            return "line", line

        parser = line_parser

        if self.line_parser is not None:
            parser = self.line_parser

        if self.lines is None:
            return

        for line in self.lines:
            yield parser(line)

    def __str__(self):
        s  = "Method = {}\n".format(self.method)
        s += "Path = {}\n".format(self.path)
        s += "Status = {}\n".format(self.status)
        s += "Reason = {}\n".format(self.reason)
        s += "Content-Type = {}\n".format(self.content_type)
        return s
