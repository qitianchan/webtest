__author__ = 'qitian'
import os
import sys
import web
import app
from core.urldeal import config_urls

urls =	config_urls()
app = web.application(urls, globals())

render = web.template.render('templates', globals())

class Angular:
	def GET(self):
		return render.angularjs()

if __name__ == '__main__':
	app.run()
