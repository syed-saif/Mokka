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
	def render_template_inside_class(template ,sub_dir = None, **namespace):
		'''
		A static method that provides the users the option to render user-created templates.
		So far, only this method and 'render_from_string' method, in this module, is meant to 
		be directly used by the user. Go to the end of this module to know why the function is named this way.
		params: 
		'template': The template to be rendered. This must be present inside the app's 'templates'
					folder(either the default or user created one). 
		'sub_dir': Additionally, the users may want to group certain templates together in a sub-directory
				   within the templates folder. In that case, this parameter can be used to specify the 
				   respective sub-directory. Defaults to 'None'.
		'namespace': To define variables within templates, a namespace(which is a dict of 'varaible':'value' pairs)
					 must be provided to TRender. This method accepts a bunch of keyword args(which becomes a dict)
					 and then it is provided to TRender.
		'''
		cls = Templates

		#a very simple render_template func:
		compiled = TRender(template, path = cls.app.templates_path)
		output = compiled.render(namespace)
		return output

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


#In this module, only 'render_template' and 'render_from_string' are meant to be used by user.
#But it's not possible to import only a selected method from a class, only the class itself can be imported
#To tackle this, we simply create a variable that points to the static method of the class
#Then this variable is imported, rather than directly attempting to import the class's methods.
#Here, the 'import' is all about importing stuff within __init__.py file of this package.  
render_template = Templates.render_template_inside_class

