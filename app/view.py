from flask_restplus import Resource, Namespace


nsm_1 = Namespace('v1',description='something')

@nsm_1.route('/')
class Hello(Resource):
	def get(self):
		return {'':''}