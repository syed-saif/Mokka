import os

#Dummy will use 'TRender' templating engine, to render user-created templates.
from trender import TRender

class Templates:
	'''
	A class to encapsulate all templating features of 'Dummy' into one.
	Note that this class is never instantiated, anywhere in this code.
	This is only to keep certain things together. 
	'''

	@staticmethod
	def render_template():
		'''
		A static method that provides the users the option to either render templates 
		or strings. So far, only this method, in this module, is meant to be directly used 
		by the user.
		'''
		pass

	@classmethod
	def check_and_create_templates_folder(cls):
		'''
		This method creates a templates folder in the root directory
		of app, if no path was provided to 'Dummy' constructor. 
		Note: To keep things simple, only the default 'templates' folder,
		in the root path of app, will be created by Dummy, and no directories
		for user-provided paths will be created.
		'''	
		if cls.app.templates_path is None:
			
			try:
				path = os.path.join(cls.root_path, 'templates/')
				cls.app.templates_path = path
				os.mkdir(path)
				
			except FileExistsError:
				#Since mkdir can sometimes produce a race condition, and say that
				#the file/dir already exists even when it's not, we do nothing when
				#this exception is raised 
				
				pass
			else:
				#if any other exception is catched, it is raised here
				#hopefully there won't be any :P 
				
				raise 


	@classmethod
	def bind_app(cls, app):
		'''
		Binds this class with the app instance. This method also acts as a 
		'setup method' to set all the required things up and running. 
		'''
		cls.app = app
		cls.root_path = app.get_root_path()
		cls.check_and_create_templates_folder()
