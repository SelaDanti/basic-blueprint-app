from flask import Resource

from setup import nsm_1


@nsm_1.route('/')
class Hello(Resource):
	def get(self):
		return {'':''}