# Generated by Django 4.1.1 on 2022-09-23 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import film.validators
import rent.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("film", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RentModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rent_date", models.DateField(default=django.utils.timezone.now)),
                (
                    "expected_return_day",
                    models.DateField(
                        validators=[
                            rent.validators.RentValidators.validate_date,
                            rent.validators.RentValidators.validator_max_days,
                        ]
                    ),
                ),
                (
                    "return_day",
                    models.DateField(
                        blank=True,
                        null=True,
                        validators=[
                            rent.validators.RentValidators.validate_date,
                            film.validators.FilmValidators.validator_today,
                        ],
                    ),
                ),
                ("tax", models.PositiveIntegerField(blank=True, default=0, null=True)),
                ("debt", models.PositiveIntegerField(blank=True, default=0, null=True)),
                (
                    "id_film",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="film.filmmodel",
                    ),
                ),
                (
                    "id_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Rent",
                "verbose_name_plural": "Rents",
                "ordering": ["-id"],
            },
        ),
    ]
