from app.api.v1.models.parcelmodels import Parcel
from flask_restful import Resource
from flask import make_response, jsonify, request


def validate_number(integer):
    """This function is used to validate that a user enters an integer"""
    try:
        int(integer)
    except ValueError:
        return False
    else:
        return True


def validate_string(string):
    """This function is used to validate if a user enters a string or blank data"""
    if type(string) is not str:
        return False
    elif bool(string.strip()) is False:
        return False
    elif validate_number(string) is True:
        return False

    else:
        return True


class DataDelivery(Resource, Parcel):

    def post(self):
        """This is where the user posts their data"""
        data = request.get_json(force=True)
        try:
            user_id = data["user_id"]
            parcel_type = data["parcel_type"]
            location_to_pickup = data["location_to_pickup"]
            location_to_deliever = data["location_to_deliever"]
            
        except KeyError:
            return{"message": "Complete the Parcel order"}, 400
        if not validate_number(user_id):
            return{"message": "enter your user id"}, 400
        if not validate_string(parcel_type):
            return{"message": "enter the parcel type"}, 400
        if not validate_string(location_to_pickup):
            return{"message": "enter the location to pickup"}, 400
        if not validate_string(location_to_deliever):
            return{"message": "enter the location_to_deliever"}, 400


        new_data = Parcel.create_order(
            self, user_id, parcel_type, location_to_pickup, location_to_deliever)
        return{"message": "you have succesfully created an order"}, 201

    def get(self):
        parcels = Parcel.get_all(self)
        return{"message": "Parcel orders succesfully fetched.", "parcels": parcels}, 200


class SingleDelivery(Resource, Parcel):

    def get(self, delivery_id):

        single = Parcel.get_delivery(self, delivery_id)
        if not single:
            return{"message": "There is no Parcel order with that id"}, 400
        return{"message": "Here is the Parcel order", "parcels": single}, 200


class SingleUser(Resource, Parcel):

    def get(self, user_id):
        user = Parcel.get_user(self, user_id)
        if not user:
            return{"message": "There is no Parcel order for a user with that user id"}, 400
        return{"message": "This is the users Parcel orders", "user": user}, 200


class CancelDelivery(Resource, Parcel):

    def put(self, delivery_id):
        cancel = Parcel.put_delivery(self, delivery_id)
        return{"message": "Updated the delivery status to cancel", }, 200 


