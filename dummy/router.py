from werkzeug.routing import Rule, Map


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
		self.endpoint = None

	def __enter__(self):
		
		return View_binder(self)

	def __exit__(self, *args):
		if self.methods is None:
			self.methods = ['GET']
		rule_obj = Rule(self.rule, endpoint = self.endpoint.__name__, methods = self.methods)
		Router.app.url_map.add(rule_obj)
		Router.app.views[self.endpoint.__name__] = self.endpoint