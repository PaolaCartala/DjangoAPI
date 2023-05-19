from django.test import TestCase
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import FilmModel, CategoryModel, RoleModel, FilmTypeModel
from rent.resources import RentTestResources


# Create your tests here.
class FilmModelTestCase(TestCase):

    def setUp(self) -> None:
        user = RentTestResources().set_user()
        user.save()
        data = RentTestResources.get_dataname()
        filmtype = FilmTypeModel.objects.create(name=data['name'])
        filmtype.save()
        category = CategoryModel.objects.create(name=data['name'])
        category.save()
        role = RoleModel.objects.create(name=data['name'])
        role.save()
        staff = RentTestResources().set_staff(role)
        staff.save()
        film = RentTestResources().set_film(filmtype, category, staff)
        film.save()

    def test_release_date_today(self):
        obj = FilmModel.objects.get(id=2)
        obj.release_date = timezone.now().date() + timedelta(days=1)
        self.assertRaises(ValidationError, obj.full_clean)
