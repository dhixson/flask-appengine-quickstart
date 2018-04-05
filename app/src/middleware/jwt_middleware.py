"""Middleware to log before and after response."""
import re
import jwt
from werkzeug.exceptions import Unauthorized
from werkzeug.wrappers import Request

class JWTMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print "MIDDLEWARE"
        request = Request(environ, shallow=True)
        header = request.headers.get('Authorization')
        if header is None:
            return Unauthorized()(environ, start_response)
        regex = r"(?:Bearer\s*)(\S+)\b"
        match = re.match(regex, header)
        if not match:
            return Unauthorized()(environ, start_response)
        data = jwt.decode(match.group(1), 'GgfkXtJ2ofNhwBv85WfbiEdFTFn5704A', algorithms=['HS256'])
        response = self.app(environ, start_response)
        return response

    def abort(code, environ, start_response):
        try:
            abort(code)
        except HTTPException as e:
            return e(environ, start_response)
