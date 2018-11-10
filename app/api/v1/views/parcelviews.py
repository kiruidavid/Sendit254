from app.api.v1.models.parcelmodels import Parcel
from flask_restful import Resource 
from flask import make_response, jsonify, request



class DataDelivery(Resource,Parcel):

	def post(self):
		data = request.get_json(force=True)
		parcel_to_order = data["parcel_to_order"]
		location_to_pickup = data["location_to_pickup"]
		location_to_deliever = data["location_to_deliever"]
		status = data["status"]

		new_data = Parcel.create_order(self,parcel_to_order,location_to_pickup,location_to_deliever, status)
		return {'message':new_data}


	def get(self):
		 res = Parcel.get_all(self)
		 return res 


class SingleDelivery(Resource, Parcel):
	def get(self, delivery_number):
		res = Parcel.get_delivery(self, delivery_number)
		return res 


class CancelDelivery(Resource, Parcel):
	def put(self, delivery_number):
		res = Parcel.put_delivery(self, delivery_number)
		return res
	


		

	

		

	
	 








		

