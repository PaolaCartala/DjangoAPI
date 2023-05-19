from django.db import models
from django.core.validators import MinValueValidator

from .validators import FilmValidators


class CategoryModel(models.Model):

    name = models.CharField(
        max_length=50, null=False, blank=False, unique=True
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
        ordering = ['id']

    def __str__(self):
        return self.name


class RoleModel(models.Model):

    name = models.CharField(
        max_length=50, null=False, blank=False, unique=True
    )

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
        ordering = ['id']

    def __str__(self):
        return self.name


class StaffModel(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    id_role = models.ForeignKey(
        RoleModel, on_delete=models.DO_NOTHING
    )

    @property
    def get_full_name(self):
        return f'{self.name} {self.lastname}'

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'
        ordering = ['id']

    def __str__(self):
        return f"{self.lastname}, {self.name} - {self.id_role}"


class FilmTypeModel(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Film Type'
        verbose_name_plural = 'Films Type'
        ordering = ['-id']

    def __str__(self):
        return self.name


class FilmModel(models.Model):

    title = models.CharField(
        max_length=50, null=False, blank=False, unique=True
    )
    description = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    availability = models.PositiveIntegerField()
    release_date = models.DateField(
        validators=[FilmValidators.validator_today]
    )
    film_type = models.ForeignKey(
        FilmTypeModel, on_delete=models.DO_NOTHING
    )
    id_category = models.ManyToManyField(CategoryModel)
    id_staff = models.ManyToManyField(StaffModel)

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'
        ordering = ['-id']

    def __str__(self):
        return f"{self.film_type} - ({self.release_date.year}) {self.title}"
