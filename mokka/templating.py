import os

#Mokka will use 'TRender' templating engine, to render user-created templates.
from trender import TRender

class Templates:
	'''
	A class to encapsulate all templating features of 'Mokka' into one.
	Note that this class is never instantiated, anywhere in this code.
	This is only to keep certain things together. 
	'''

	@staticmethod
	def render_template_inside_class(template ,sub_dir = None, **namespace):
		'''
		A static method that provides the users the option to render user-created templates.
		So far, only this method and 'render_from_string_inside_class' method, in this module, is meant to 
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

		#default template path:
		path = cls.app.templates_path
		
		#In case 'sub_dir' arg was passed:
		if sub_dir is not None:

			cls.verify_sub_dir(path)
			path = os.path.join(path, sub_dir)	
		
		compiled = TRender(template, path = path)
		output = compiled.render(namespace)
		
		return output

	@staticmethod
	def render_from_string_inside_class(source_string, **namespace):
		'''
		A static method that lets the user render strings, provided the namespace/context is given.
		In this module, only this method and 'render_template_inside_class' is meant to be used by the user.
		Again, the last few lines in this module will explain why this method is named this way.
		params:
		'source_string': The string to be rendered. Only 'str' objects must be passed.
		'namespace': These are the values of the variables, defined inside the string to be rendered. Here, a bunch 
		of keyword args are accepted(which becomes a dict) and are passed to TRender engine.  
		'''
		cls = Templates

		if not isinstance(source_string, str):
			raise ValueError("'source_string' arg passed to 'render_from_string' must"
				" be of type 'str'.")

		compiled = TRender(source_string)
		output = compiled.render(namespace)

		return output


	@classmethod
	def verify_sub_dir(cls, path):
		'''
		Checks if the provided path is relative, then if it exists, else
		throws appropriate errors 
		'''

		if not isinstance(path, str):
			raise ValueError("'sub_dir' argument provided to 'render_template' must be of type 'str'")

		if os.path.isabs(path):
			raise ValueError("'sub_dir' argument provided to 'render_template' must be a" 
			 " relative path. An absolute path was given instead.")

		if not os.path.isdir(path):
			raise ValueError("'sub_dir' argument provided to 'render_template' does not exist."
				" Provide a valid, relative path.")

		
	@classmethod
	def check_and_create_templates_folder(cls):
		'''
		This method creates a templates folder in the root directory
		of app, if no path was provided to 'Mokka' constructor. 
		Note: To keep things simple, only the default 'templates' folder,
		in the root path of app, will be created by Mokka, and no directories
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
			except Exception as e:
				#if any other exception is catched, it is raised here
				#hopefully there won't be any :P 
				
				raise e


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

#same for this method as well:
render_from_string = Templates.render_from_string_inside_class