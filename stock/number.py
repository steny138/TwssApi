#-*- coding: utf-8 -*-

from flask.ext import restful

class GetNumber(restful.Resource):
	def get(self):
		return {'no': '2330'}

class BaseInfo(restful.Resource):
	def get(self):
		return {'name': '台積電'}