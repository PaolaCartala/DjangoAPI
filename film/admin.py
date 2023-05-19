from django.contrib import admin

from .models import (
    FilmModel, CategoryModel, RoleModel, FilmTypeModel, StaffModel
)


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'film_type', 'stock', 'availability')
    fields = (
        'title', 'film_type', 'description',
        'stock', 'availability', 'price', 'release_date',
        'id_staff', 'id_category'
    )
    search_fields = ('title', 'release_date')


class StaffAdmin(admin.ModelAdmin):
    search_fields = ('name', 'lastname', 'id_role')


admin.site.register(FilmModel, FilmAdmin)
admin.site.register(FilmTypeModel)
admin.site.register(CategoryModel)
admin.site.register(RoleModel)
admin.site.register(StaffModel, StaffAdmin)
