from flask import Blueprint
from flask_restplus import Api


app_v1 = Blueprint('app_v1',__name__)
api_v1 = Api(app_v1)


nsm_1 = api_v1.namespace('v1',description='something')