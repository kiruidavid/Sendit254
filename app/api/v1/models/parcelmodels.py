parcels = [{"delivery_id": "1",
            "user_id": "5",
            "parcel_type": "books",
            "location_to_pickup": "kile",
            "location_to_deliver": "buru",
            "status": "pending"
            }
           ]


class Parcel(object): 
    """The class name"""

    def __init__(self):
        self.db = parcels

    def create_order(self, user_id, parcel_type, location_to_pickup, location_to_deliver): 
        """Function for creating an order"""

        payload = {
            "delivery_id": str(len(parcels) + 1),
            "user_id": user_id,
            "parcel_type": parcel_type,
            "location_to_pickup": location_to_pickup,
            "location_to_deliver": location_to_deliver,
            "status": str("pending")
        }

        self.db.append(payload)
        return payload

    def get_all(self): 
        """Function to get all deliveries made"""
        res = self.db
        return res

    def get_delivery(self, delivery_id): 
        """Function for getting a single delivery"""
        res = self.db
        results = [result for result in res if result[
            "delivery_id"] == str(delivery_id)]
        return results

    def get_user(self, user_id): 
        """Function for getting a specific user with their user_id"""
        res = self.db
        results = [result for result in res if result[
            "user_id"] == str(user_id)]
        return results

    def put_delivery(self, delivery_id): 
        """Function for updated the delivery status to canceled using the delivery_id"""
        res = self.db
        results = [result for result in res if result[
            "delivery_id"] == str(delivery_id)]
        result = results[0]
        result["status"] = "canceled"
     


    
