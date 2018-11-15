users = []


class Users(object):

	def __init__(self):
		self.db = users

	def create_order(self, user_id, parcel_to_order, location_to_pickup, location_to_deliever):
		delivery = {
		'user_id': user_id,
		'parcel_to_order': parcel_to_order,
		'location_to_pickup': location_to_pickup,
		'location_to_deliever': location_to_deliever
		}

		self.db.append(delivery)
		return delivery

	def get_all(self):
		return self.db

	def get_user(self, user_id):
		res = self.db
		results = [result for result in res if result["user_id"] == str(user_id)]
		return results

	def create_account(self, email, phone_number, user_name, password):
		account = {
		'user_id': str(len(users) + 1), 
		'email':email,
		'phone_number':phone_number,
		'user_name':user_name,
		'password':password, 
		
		}

		self.db.append(account)
		return account


	def get_users(self):
		res = self.db 
		return res 


	def log_in(self, user_name, password, role):
		log_in={
		'user_name':user_name,
		'password':password,
		'role':role 
		} 

		if user_name == 'user_name' and password == 'password':
			return log_in



		
