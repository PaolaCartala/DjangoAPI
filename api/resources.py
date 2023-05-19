from datetime import timedelta
from django.utils import timezone


class APITestResources:

    @staticmethod
    def get_datauser():
        data = {
            "username": "example_customer",
            "first_name": "Example",
            "last_name": "Customer",
            "email": "example2@example.com",
            "address": "Fake Address 123",
            "phone": 123456
        }
        return data

    def get_dataname(self):
        data = {
            "name": "test"
        }
        return data

    def get_datastaff(self):
        data = {
            "name": "testname",
            "lastname": "testlastname",
            "id_role": 1
        }
        return data

    def get_datafilm(self):
        data = {
            "title": "film title",
            "description": "test description",
            "stock": 10,
            "price": 50.0,
            "availability": 10,
            "release_date": "2001-11-29",
            "film_type": 1,
            "id_category": [
                1,
            ],
            "id_staff": [
                1,
            ]
        }
        return data

    @staticmethod
    def get_datarent():
        rent_date = timezone.now().date()
        expected_return = timezone.now().date() + timedelta(days=3)
        data = {
            'id_user': 2,
            "id_film": 1,
            "rent_date": rent_date,
            "expected_return_day": expected_return,
            "return_day": None,
            "tax": 0,
            "debt": 0
        }
        return data

    @staticmethod
    def get_datarent_update():
        rent_date = timezone.now().date()
        expected_return = timezone.now().date() + timedelta(days=3)
        data = {
            'id_user': 2,
            "id_film": 1,
            "rent_date": rent_date,
            "expected_return_day": expected_return,
            "return_day": timezone.now().date(),
            "tax": 0,
            "debt": 0
        }
        return data

    @staticmethod
    def get_datarent_update_error():
        return_day = timezone.now().date() - timedelta(days=3)
        return return_day
