from app.api.v1.models.usermodels import Users 
from flask_restful import Resource
from flask import make_response,jsonify,request


class UserDelivery(Resource, Users):

	def post(self):
		data = request.get_json(force=True)
		user_id = data["user_id"]
		parcel_to_order = data["parcel_to_order"]
		location_to_pickup = data["location_to_pickup"]
		location_to_deliever = data["location_to_deliever"]
		

		new_data = Users.create_order(self, user_id,parcel_to_order,location_to_pickup,location_to_deliever)
		return {'message':'order is a success'}


	def get(self):
		 res = Users.get_all(self)
		 return res 


class GetUsers(Resource, Users):
	def get(self, user_id):
		res = Users.get_user(self, user_id)
		return res  


class CreateUser(Resource, Users):
	def post(self):
		data = request.get_json(force=True)
		email = data["email"]
		phone_number = data["phone_number"]
		user_name = data["user_name"]
		password = data["password"]
		


		new_user = Users.create_account(self, email, phone_number, user_name, password)
		return {'message': 'you created an account'}


	def get(self):
		res = Users.get_users(self)
		return res
		 

class Login(Resource, Users):
	def post(self):
		data = request.get_json(force=True)
		user_name = data["user_name"]
		password = data["password"]
		role = data["role"]

		log_in = Users.log_in(self, user_name, password, role)
		return{'message':'you are logged in'}



