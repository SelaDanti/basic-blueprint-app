from flask import request
from flask_restplus import Namespace, Resource,fields

ns_1 = Namespace('v1',description='challenge 2')

mod = ns_1.model('my model',{
	'name': fields.String(description='name')
	})

@ns_1.route('/home')
class Sales(Resource):
	@ns_1.expect(mod,validate=True)
	def post(self):
		data = request.get_json()
		return data,404


@ns_1.route('/home/s')
class Sale(Resource):
	@ns_1.expect(mod,validate=True)
	def put(self):
		data = request.get_json()
		return data,404


@ns_1.route('/home/sa')
class Sal(Resource):
	def get(self):
		data = {'':''}
		return data,200