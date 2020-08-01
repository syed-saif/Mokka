# Mokka 

Mokka is a delicate, experimental [WSGI](https://wsgi.readthedocs.io/en/latest/what.html) micro web framework, for 
building minimalistic python web applications. It is still under development and is open to contributions. It is built on 
top of a WSGI helper library, called [Werkzeug](https://www.palletsprojects.com/p/werkzeug/) and uses [
TRender](https://github.com/transceptor-technology/trender) templating engine, to render user created templates.

## Installation

This project will soon be published on [PyPI](https://pypi.org/), to make installations easy with 'pip'. Until then 
installations have to be done manually: 
* Clone/Download this repository.
* Optional but recommended: Create a new python [virtual environment](https://virtualenv.pypa.io/en/stable/).
* Activate the virtualenv (if created), `cd` into the root of this repo and install the dependencies using the bash
command:
```bash
pip install -r requirements.txt
```
* Now you have installed the package but, if you try to import it from elsewhere, you'll get 'ModuleNotFoundError'. This
is because python expects this package in the directory relative to the module making the import, since we 
technically didn't install anything.
* So your modules, that contain the app, have to be in the root dir of this repo. Note that this is a temporary problem 
and once the package is published in PyPI it'll be a lot easier to use.
* One dirty trick is to include these python lines in your scripts and then you can import this package from anywhere:
```python
import sys
sys.path.append('path/to/this/repo/on/your/machine')
```

## Quickstart 

Assuming you have installed the package:
```python
from mokka import Mokka, Router

app = Mokka()

with Router('/') as vb:
	def hello(req):
		return "Hello world!!"

	vb.bind(fun)

if __name__ == '__main__':

	from werkzeug.serving import run_simple
	run_simple('localhost', 4000, app)
```
Let's see step by step of what's happening here:
* We simply import the classes 'Mokka' and 'Router', and create a 'Mokka' instance and call it 'app'.
* The 'Router' object is intended to work as a [context manager](https://docs.python.org/3/reference/datamodel.html#context-managers), which will take care of the URL routing.
* 'Router' constructor takes in a URL as a paramater. The context manager returns a 'View_binder' object and we call it as 'vb'.
* A simple view fuction is defined inside this context manager block, and the function is then *binded* to the 'Router', with the 'View_binder.bind()' method.
* Then under `if __name__ == '__main__':`  we import a simple development server from [werkzeug](https://www.palletsprojects.com/p/werkzeug/) and we pass in the app instance.
* Note that, the docs for this project are still under development and will be available soon, showcasing all the features of mokka. 

## Why mokka?

Now I'll talk in direct speech. I'm a student who's still learning whatever he can and doing his best to showcase his 
skills. I had a great amount of curiosity over these web applications and how they work, how they interact with web
servers etc. And after spending my time pondering, I decided to take up this project and build my own framework, **not** 
to come up with something better than what is already there, but to learn what actually happens under the hood.
That gives me knowledge and *knowlegde is power*. This simple quote made me do it:
*'I see, and I forget. I hear, and I remember. I do, and I understand'*

I'll be sure to include my journey in the docs too. Stay tuned!  
