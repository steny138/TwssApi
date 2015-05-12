#-*- coding: utf-8 -*-

from flask.ext import restful

class History(restful.Resource):
    def get(self):
        return {'open': 30, 'close': 40}
