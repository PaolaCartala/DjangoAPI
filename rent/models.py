from django.utils import timezone
from django.db import models

from film.models import FilmModel
from account.models import CustomUser
from .validators import RentValidators
from film.validators import FilmValidators


class RentModel(models.Model):

    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_film = models.ForeignKey(
        FilmModel, on_delete=models.DO_NOTHING
    )
    rent_date = models.DateField(default=timezone.now)
    expected_return_day = models.DateField(
        validators=[
            RentValidators.validate_date,
            RentValidators.validator_max_days
        ]
    )
    return_day = models.DateField(
        validators=[
            RentValidators.validate_date, FilmValidators.validator_today
        ],
        blank=True, null=True
    )
    tax = models.PositiveIntegerField(default=0, blank=True, null=True)
    debt = models.PositiveIntegerField(default=0, blank=True, null=True)

    @property
    def get_film_title(self):
        return self.id_film.title

    class Meta:
        verbose_name = 'Rent'
        verbose_name_plural = 'Rents'
        ordering = ['-id']

    def __str__(self):
        return f'{self.id_user.username} - {self.id_film.title}'
