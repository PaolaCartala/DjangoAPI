from django.contrib import admin

from .models import RentModel


class RentAdmin(admin.ModelAdmin):
    list_display = (
        'id_film', 'id_user', 'rent_date',
        'expected_return_day', 'return_day'
    )
    search_fields = ('id_user__username', 'id_film__title')


# Register your models here.
admin.site.register(RentModel, RentAdmin)
