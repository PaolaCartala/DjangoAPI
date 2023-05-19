from django.test import TestCase
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError

from film.models import CategoryModel, RoleModel, FilmTypeModel
from .models import RentModel
from .resources import RentTestResources
from .validators import RentValidators


# Create your tests here.
class RentModelTestCase(TestCase):

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
        datarent = RentTestResources.get_datarent()
        rental = RentModel.objects.create(
            id_user=user,
            id_film=film,
            rent_date=datarent['rent_date'],
            expected_return_day=datarent['expected_return_day'],
            return_day=datarent['return_day'],
            tax=datarent['tax'],
        )
        rental.save()
        return super().setUp()

    def test_expected_return_day_today(self):
        obj = RentModel.objects.get(id=2)
        obj.expected_return_day = timezone.now().date() - timedelta(days=1)
        self.assertRaises(ValidationError, obj.full_clean)

    def test_expected_return_day_today_max(self):
        obj = RentModel.objects.get(id=3)
        obj.expected_return_day = timezone.now().date() + timedelta(days=16)
        self.assertRaises(ValidationError, obj.full_clean)

    def test_return_day_today(self):
        obj = RentModel.objects.get(id=4)
        obj.return_day = timezone.now().date() - timedelta(days=1)
        self.assertRaises(ValidationError, obj.full_clean)

        obj.return_day = timezone.now().date() + timedelta(days=1)
        self.assertRaises(ValidationError, obj.full_clean)


class RentValidatorsTestCase(TestCase):

    def test_validate_date(self):
        value = timezone.now().date() - timedelta(days=1)
        self.assertRaises(
                ValidationError, RentValidators.validate_date,
                value
            )

    def test_max_days(self):
        value = timezone.now().date() + timedelta(days=20)
        self.assertRaises(
                ValidationError, RentValidators.validator_max_days,
                value
            )
