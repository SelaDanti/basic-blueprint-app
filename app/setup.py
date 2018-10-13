from flask import Blueprint
from flask_restplus import Api

from .view import nsm_1


app_v1 = Blueprint('app_v1',__name__)
api_v1 = Api(app_v1)


api_v1.add_namespace(nsm_1)