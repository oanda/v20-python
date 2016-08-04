import json

class Request(object):
    def __init__(self, method, path):
        self.method = method
        self.base_path = path
        self.path = path
        self.params = {}
        self.stream = False
        self.body = ""
        self.line_parser = None
        self.headers = {}

    def set_path_param(self, key, value):
        if value is None:
            return
        key = "{" + key + "}"
        self.path = self.path.replace(key, str(value))

    def set_param(self, key, value):
        if value is None:
            return

        self.params[key] = str(value)

    def set_body_string(self, body_str):
        self.body = body_str

    def set_body_dict(self, params):
        if len(params) is 0:
            return

        self.body = json.dumps(params)

    def set_stream(self, stream):
        self.stream = stream

    def set_line_parser(self, parser):
        self.line_parser = parser
