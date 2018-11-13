parcels = []

class Parcel(object):
	def __init__(self):
		self.db = parcels

	def create_order(self, parcel_to_order, location_to_pickup, location_to_deliver, status):
    	

		payload = {
    		'delivery_number': str(len(parcels) + 1),
    		'parcel_to_order': parcel_to_order,
    		'location_to_pickup': location_to_pickup,
    		'location_to_deliver': location_to_deliver,
    		'status': status
         }

		self.db.append(payload)
		return payload

	def get_all(self):
 		return self.db


 	def get_delivery(self, delivery_number):
 		res = self.db
 		results = [result for result in res if result['delivery_number'] == str(delivery_number)]
 		return results
 		

	