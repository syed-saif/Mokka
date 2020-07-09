#import werkzeug
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.utils import redirect

from .router import Router

#Werkzeug's Response class, by default, uses 'text/plain' as the mimetype.
#In Dummy, I prefer the default mimetype to be 'text/html' and hence the class variable is overridden as:
Response.default_mimetype = "text/html"

class Dummy():
	"""docstring for Dummy"""
	
	def __init__(self):
		self.url_map = Map()
		self.views = {}
		Router.bind_app(self)


		
	def get_response(self, endpoint, request, values = None):
		rv = self.views[endpoint](request, **values)
		return rv

	def __call__(self, environ, start_response ):
		'''
		When a request comes in, the server will call our application instance.
		When called, this method will execute. 
		'''
		
		request = Request(environ)
		adapter = self.url_map.bind_to_environ(environ)
		try:
			endpoint, values = adapter.match()
		
			response = self.get_response(endpoint, request, values)
			if isinstance(response, Response):
				return response(environ, start_response)
			res = Response(response)
		
			return res(environ, start_response)
		
		except HTTPException as e:
			return e(environ, start_response)




