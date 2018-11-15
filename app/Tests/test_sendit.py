import unittest
import json
from app import create_app
from app.api.v1.views import parcelviews, userviews
from app.api.v1.models import parcelmodels, usermodels


class TestDataParcel(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        self.data = {
            "user_id": "5",
            "parcel_type": "books",
            "location_to_pickup": "kile",
            "location_to_deliever": "buru"
        }

        self.wrong_data = {
            "user_id": "",
            "parcel_type": "books",
            "location_to_pickup": "kile",
            "location_to_deliever": "buru"


        }

    def test_post(self):
        response = self.client.post(
            "/api/v1/parcels", data=json.dumps(self.data), content_type="application/json")
        assert response.status_code == 201

    def test_blank_user_id(self):
        response = self.client.post(
            "/api/v1/parcels", data=json.dumps(self.wrong_data), content_type="application/json")
        result = json.loads(response.data)
        assert response.status_code == 400

    new_data = {
        "delivery_id": "1",
        "user_id": "5",
        "parcel_type": "books",
        "location_to_pickup": "kile",
        "location_to_deliver": "buru",
        "status": "pending" 
    }
    
    def test_get(self):
        response = self.client.get("/api/v1/parcels")
        assert response.status_code == 200   

    def test_getparcel(self):
       response = self.client.get("/api/v1/parcels/1")
       assert response.status_code == 200 

    def test_wrong_url(self):
        response = self.client.get("/api/v1/parcels/z")
        assert response.status_code == 404 
    def test_get_excess(self):
        response = self.client.get("/api/v1/parcels/3")
        assert response.status_code == 400 
    def test_get_user(self):
        response = self.client.get("/api/v1/users/5/parcels")
        assert response.status_code == 200 
    def test_url_entry(self):
        response = self.client.get("/api/v1/users/e/parcels")
        assert response.status_code == 404 
    def test_wrong_user(self):
        response = self.client.get("/api/v1/users/3/parcels")
        assert response.status_code == 400 
    def test_cancel(self):
        response = self.client.put("/api/v1/parcels/1/cancel/")
        assert response.status_code == 200 



   
       
       
        


       


      
        


