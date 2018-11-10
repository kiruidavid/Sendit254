users = []

class Users(object):
	def __init__(self):
		self.db = users 

	def create_order(self, user_id,parcel_to_order,location_to_pickup,location_to_deliever):
		delivery = {
		'user_id': user_id,
		'parcel_to_order':parcel_to_order,
		'location_to_pickup':location_to_pickup,
		'location_to_deliever':location_to_deliever 
		}

		self.db.append(delivery)
		return delivery


	def get_all(self):
		return self.db


	def get_user(self, user_id):
		res = self.db
		results = [result for result in res if result["user_id"] == str(user_id)]
		return results

		
		
		