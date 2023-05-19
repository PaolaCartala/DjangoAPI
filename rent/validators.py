from datetime import timedelta
from django.utils import timezone

from django.core.exceptions import ValidationError


class RentValidators:

    @staticmethod
    def validate_date(value):
        if value < timezone.now().date():
            raise ValidationError(
                "Please enter a valid date!"
            )

    @staticmethod
    def validator_max_days(value):
        if value > timezone.now().date() + timedelta(days=15):
            raise ValidationError(
                "You can't rent the film for more than 15 days"
            )
