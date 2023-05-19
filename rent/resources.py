from datetime import timedelta
from django.utils import timezone

from account.models import CustomUser
from film.models import FilmModel, StaffModel


class RentTestResources:

    def get_datauser(self):
        data = {
            "username": "example_customer",
            "first_name": "Example",
            "last_name": "Customer",
            "email": "example2@example.com",
            "address": "Fake Address 123",
            "phone": 123456
        }
        return data

    def set_user(self):
        datauser = self.get_datauser()
        user = CustomUser.objects.create(
            username=datauser['username'],
            email=datauser['username'],
        )
        user.set_password('tests123456')
        return user

    @staticmethod
    def get_dataname():
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

    def set_staff(self, role):
        data = self.get_datastaff()
        staff = StaffModel.objects.create(
            name=data['name'],
            lastname=data['lastname'],
            id_role=role
        )
        return staff

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
                1
            ],
            "id_staff": [
                1
            ]
        }
        return data

    def set_film(self, filmtype, category, staff):
        datafilm = self.get_datafilm()
        film = FilmModel.objects.create(
            title=datafilm['title'],
            stock=datafilm['stock'],
            price=datafilm['price'],
            availability=datafilm['availability'],
            release_date=datafilm['release_date'],
            film_type=filmtype
        )
        film.id_category.set([category, ])
        film.id_staff.set([staff, ])
        return film

    @staticmethod
    def get_datarent():
        rent_date = timezone.now().date()
        expected_return = timezone.now().date() + timedelta(days=3)
        data = {
            'id_user': 1,
            "id_film": 6,
            "rent_date": rent_date,
            "expected_return_day": expected_return,
            "return_day": None,
            "tax": 0
        }
        return data
