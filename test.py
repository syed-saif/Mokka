from dummy import Dummy, Router


app = Dummy()

with Router('/home/') as vb:
	def fun(req):
		return "<h1>Hello world</h1>"

	vb.bind(fun)




if __name__ == '__main__':
    from werkzeug.serving import run_simple

    run_simple('localhost', 4000, app, use_debugger=True, use_reloader = True)
