from flask import Blueprint
from flask_restplus import Api

from .views.sales import ns_1


app_v1 = Blueprint('app_v1',__name__)

api_v1 = Api(app_v1,title='BluePrint App',description='A basic blue print app',version='2.0')

api_v1.add_namespace(ns_1)