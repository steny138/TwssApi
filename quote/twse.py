#-*- coding: utf-8 -*-

from flask.ext import restful

class TWSE_Quote(restful.Resource):
	def get(self):
		return {'no': 2330, 'open': 30, 'close': 40}