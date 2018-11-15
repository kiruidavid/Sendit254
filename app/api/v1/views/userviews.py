from app.api.v1.models.usermodels import Users
from flask_restful import Resource
from flask import make_response, jsonify, request 
import re


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


class CreateUser(Resource, Users):

    def post(self):
        data = request.get_json(force=True)
        try:
            email = data["email"]
            phone_number = data["phone_number"]
            user_name = data["user_name"]
            password = data["password"]
        except KeyError:
            return {"message": "Incomplete request"}, 400
        if not validate_string(email):
            return{"message": "enter the email"}, 400
        if not validate_number(phone_number):
            return{"message": "enter the phone number"}, 400
        if not validate_string(user_name):
            return{"message": "enter the user name"}, 400
        if not validate_string(password):
            return{"message": "enter the password"}, 400

        
        new_user = Users.create_account(
            self, email, phone_number, user_name, password)
        return {"message": "you created an account"}, 200

    def get(self):
        res = Users.get_users(self)
        return res

"""This is where a user or admin logs in"""
"""If the login is successful it should return a message {"you are logged in"}"""




            


           
        

   
