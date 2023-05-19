from django.core.exceptions import ValidationError
from django.utils import timezone


class FilmValidators:

    @staticmethod
    def validator_today(value):
        if value > timezone.now().date():
            raise ValidationError(
                "The date can't be greater than today!"
            )
