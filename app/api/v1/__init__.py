from flask import Blueprint
from flask_restful import Api
from app.api.v1.views.parcelviews import DataDelivery, SingleDelivery



version1 = Blueprint("v1", __name__, url_prefix = "/api/v1")

api = Api(version1)
api.add_resource(DataDelivery, "/datadelivery")
api.add_resource(SingleDelivery, "/single/<int:delivery_number>")
