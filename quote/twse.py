#-*- coding: utf-8 -*-

import json
import flask
from flask.ext import restful
from twss import fetch_from_twse as twse
from datetime import datetime , timedelta
class TWSE_Quote(restful.Resource):
	def get(self, no,date):
		data = twse.QuoteStock(no, datetime.strptime(date, '%Y-%M-%d')).data
		result = []
		for x in data:
			result.append(x.__dict__)

		return  result