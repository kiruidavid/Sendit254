from flask import Blueprint
from flask_restful import Api
from app.api.v1.views.parcelviews import DataDelivery, SingleDelivery,SingleUser, CancelDelivery
from app.api.v1.views.userviews import CreateUser


version1 = Blueprint("v1", __name__, url_prefix="/api/v1")

api = Api(version1, catch_all_404s=True)
api.add_resource(DataDelivery, "/parcels")
api.add_resource(SingleDelivery, "/parcels/<int:delivery_id>")
api.add_resource(SingleUser, "/users/<int:user_id>/parcels")
api.add_resource(CancelDelivery, "/parcels/<int:delivery_id>/cancel")
api.add_resource(CreateUser, "/create")


