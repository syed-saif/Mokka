import sys
sys.path.append('/media/moinudeen/OS/SP/Mokka')
from mokka import Mokka, Router, render_from_string


app = Mokka()

with Router('/home/') as vb:
	def fun(req):
		return render_from_string("<h1>Hello world and @name</h1>", name = "saif")

	vb.bind(fun)




if __name__ == '__main__':
    from werkzeug.serving import run_simple

    run_simple('localhost', 4000, app, use_debugger=True, use_reloader = True)
