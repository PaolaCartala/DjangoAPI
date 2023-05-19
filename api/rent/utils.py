from django.utils import timezone
from rest_framework import serializers

from film.models import FilmModel


class RentUtils:

    @staticmethod
    def verify_availability(id):
        instance = FilmModel.objects.get(id=id)
        if instance.availability < 1:
            raise serializers.ValidationError(
                "There is no availability for this film"
            )
        if instance.availability > instance.stock:
            raise serializers.ValidationError(
                "Availability can't be higher than stock"
            )
        return True

    @staticmethod
    def update_availability(id, update):
        instance = FilmModel.objects.get(id=id)
        if update == 'subst':
            instance.availability -= 1
        elif update == 'add':
            instance.availability += 1
        instance.save()

    def update_tax(self, instance):
        expected_return_day = instance.expected_return_day
        if expected_return_day < timezone.now().date():
            days = timezone.now().date() - expected_return_day
            tax = days.days * 2
            instance.tax = tax
        instance.return_day = timezone.now().date()
        return instance.tax

    def update_debt(self, instance):
        tax = self.update_tax(instance)
        rent_date = instance.rent_date
        id_film = instance.id_film
        film = FilmModel.objects.get(id=id_film.id)
        price = film.price
        rent_days = timezone.now().date() - rent_date
        original_debt = rent_days.days * price
        debt = original_debt + tax
        instance.debt = debt
        instance.save()
