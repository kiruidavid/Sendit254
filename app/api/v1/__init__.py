from flask import Blueprint
from flask_restful import Api
from app.api.v1.views.parcelviews import DataDelivery, SingleDelivery,CancelDelivery
from app.api.v1.views.userviews import UserDelivery,GetUsers,CreateUser



version1 = Blueprint("v1", __name__, url_prefix = "/api/v1")

api = Api(version1)
api.add_resource(DataDelivery, "/datadelivery")
api.add_resource(SingleDelivery, "/single/<int:delivery_number>")
api.add_resource(CancelDelivery, "/cancel/<int:delivery_number>")
api.add_resource(UserDelivery,"/user")
api.add_resource(GetUsers, "/user/<int:user_id>")
api.add_resource(CreateUser, "/create")
