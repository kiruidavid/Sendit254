from flask import Blueprint
from flask_restful import Api
from app.api.v1.views.parcelviews import DataDelivery



version1 = Blueprint("v1", __name__, url_prefix = "/api/v1")

api = Api(version1)
api.add_resource(DataDelivery, "/datadelivery")
