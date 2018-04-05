"""Middleware to log before and after response."""

class LoggerMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print ' - - - - - - - - -'
        print 'Before Response'
        print ' - - - - - - - - -'
        response = self.app(environ, start_response)
        print ' - - - - - - - - -'
        print 'After Response'
        print ' - - - - - - - - -'
        return response
