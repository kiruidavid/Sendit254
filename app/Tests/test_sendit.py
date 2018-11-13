import unittest
import tempfile 
import json 
from app import create_app
from app.api.v1.views import parcelviews,userviews
from app.api.v1.models import parcelmodels,usermodels

class TestDataParcel(unittest.TestCase):
	def setUp(self):
		self.app = create_app()
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()


		self.new_data = { 
		"delivery_number": "1",
		"location_to_deliever": "buru",
		"location_to_pickup": "tao",
		"parcel_to_order": "money",
		"status": "pending"

		}	

	def test_post(self):
		response = self.client.post('/api/v1/datadelivery', data=json.dumps(self.new_data), content_type='application/json')
		result = json.loads(response.data)
		self.assertEqual(result['message'],'order is a success', msg="Assertion error not Equal" )


	def test_get(self):
		response = self.client.get('/api/v1/datadelivery', data=json.dumps(self.new_data), content_type='application/json')
		result = json.loads(response.data) 



	def test_getdelivery(self):
		response = self.client.get('/api/v1/single/1', data=json.dumps(self.new_data), content_type='application/json')
		result = json.loads(response.data) 


	def test_put(self):
		response = self.client.get('/api/v1/cancel/1', data=json.dumps({"status":"canceled"}), content_type='application/json')
		result = json.loads(response.data)


class TestUserDeliver(unittest.TestCase):
	def setUp(self):
		self.app = create_app()
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()

		self.new_data = {
		"user_id":"3",	
		"parcel_to_order":"books",
		"location_to_pickup":"texas",
		"location_to_deliever":"ruai"
		} 

	def test_post(self):
		response = self.client.post('/api/v1/user', data=json.dumps(self.new_data), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],'order is a success', msg="Assertion error not Equal" ) 

	def test_getuser(self):
		response = self.client.post('/api/v1/user/3', data=json.dumps(self.new_data), content_type='application/json')
		result = json.loads(response.data)



class TestCreateUser(unittest.TestCase):
	def setUp(self):
		self.app = create_app()
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()
		self.app_context.push()  


		self.new_user = {

		"user_id": "1",
		"email": "kim.we@grail.com",
		"phone_number": "07342323",
		"user_name": "kim1",
		"password": "password12"
		}


	def test_post(self):
		response = self.client.post('/api/v1/create', data=json.dumps(self.new_user), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'you created an account', msg="Assertion error not Equal")
		
	def test_get(self):
		response = self.client.post('/api/v1/create', data=json.dumps(self.new_user), content_type='application/json')
		result = json.loads(response.data)


		
	