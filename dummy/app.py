
import sys
import os

#import werkzeug
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.utils import redirect

from .router import Router
from .templating import Templates

#Werkzeug's Response class, by default, uses 'text/plain' as the mimetype.
#In Dummy, I prefer the default mimetype to be 'text/html' and hence the class variable is overridden as:
Response.default_mimetype = "text/html"

class Dummy():
	"""docstring for Dummy"""
	
	def __init__(self, templates_path = None):
		self.url_map = Map()
		self.views = {}

		self.templates_path = templates_path
		self.verify_templates_path()

		Router.bind_app(self)
		Templates.bind_app(self)

	def get_root_path(self):
		'''
		Returns the root path of the module that contains the 'Dummy' instance
		Note that this fails when, instance is created and ran with an IDE
		'''
		filename = getattr(sys.modules.get('__main__'), '__file__')
		path = os.path.dirname(filename)
		root_path = os.path.abspath(path)
		return root_path

	def verify_templates_path(self):
		'''
		Checks if the provided path is relative, then if it exists, else
		throws appropriate errors 
		'''
		path = self.templates_path
		
		if path is not None and not isinstance(path, str):
			raise ValueError("'templates_path' provided to 'Dummy' constructor must be of type 'str'")
		
		if path is not None:
			if os.path.isabs(path):
				raise ValueError("If 'templates_path' is provided to 'Dummy' constructor"
				 ", it must be relative. An absolute path was given instead")

			if not os.path.exists(path):
				raise ValueError("'templates_path' provided to 'Dummy' constructor does not exist."
					" Provide a valid, relative path")


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




