from werkzeug.routing import Rule, Map
from types import FunctionType
#from typing import Callable

class View_binder:
	'''
	The instance of this class is responsible to bind the users' view functions
	to the Router object, which will in turn bind the functions to url_map of the app. 
	''' 
	def __init__(self, router):
		self.router = router

	def bind(self, view):
		self.router.endpoint = view


class Router:
	'''
	The class for creating the context manager to route URLs to user
	defined functions
	'''
	

	@classmethod
	def bind_app(cls, app_instance):
		cls.app = app_instance
	
	
	def __init__(self, url_rule, methods = None):

		self.rule = url_rule
		self.methods = methods


	def __enter__(self):
		
		self.endpoint = None
		return View_binder(self)

	def __exit__(self, exc_type, exc_val, exc_tb):
		
		if self.endpoint is None:
			raise RuntimeError(f"Router for '{self.rule}' expected"
				" the user to bind a 'function' to it"
				" but got 'None'.")

		if not isinstance(self.endpoint, FunctionType):
			raise TypeError("View_binder.bind() argument must be"
				f" a 'function', not '{type(self.endpoint).__name__}'") 

		if self.methods is None:
			self.methods = ['GET']

		rule_obj = Rule(self.rule, endpoint = self.endpoint.__name__, methods = self.methods)
		Router.app.url_map.add(rule_obj)
		Router.app.views[self.endpoint.__name__] = self.endpoint