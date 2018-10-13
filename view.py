from flask import Resource

v1 = Namespace('v1',description='something')

@v1.route('/')
class Hello(Resource):
	def get(self):
		return {'':''}