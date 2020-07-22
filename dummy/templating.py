#Dummy will use 'TRender' templating engine, to render user-created templates.
from trender import TRender

class Templates:

	@staticmethod
	def check_for_templates_folder():
		'''
		This method checks if a folder named 'templates' exists within the root directory
		of the application. If yes, then we use that folder, else we create that folder.
		'''	
		pass	


	@classmethod
	def bind_app(cls, app):
		cls.app = app
		cls.root_path = app.get_root_path()
