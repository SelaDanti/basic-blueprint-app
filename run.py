from flask import Flask, Blueprint
from flask_restplus import Api, Resource, fields

api_v1 = Blueprint('api', __name__,)
api_v2 = Blueprint('api v2', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }}
api = Api(api_v1, version='1.0', title='Blueprint V1',
    description='A simple blueprint app',authorizations=authorizations
)
api2 = Api(api_v2, version='2.0', title='Blueprint V2',
    description='A simple blueprint app',authorizations=authorizations
)

v1 = api.namespace('v1', description='Challenge 2')
v2 = api2.namespace('v2', description='Challenge 2')

@v1.route('/')
class Hello(Resource):
	@v1.doc(security='apikey')
	def get(self):
		return {'hello':'Am from version 1 of the api'}


@v2.route('/')
class Hello2(Resource):
	@v1.doc(security='apikey')
	def get(self):
		return {'hello':'am from version 2 of the api'}



if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1)
    app.register_blueprint(api_v2,url_prefix='/v')
    app.run(debug=True)