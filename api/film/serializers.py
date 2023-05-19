from rest_framework import serializers

from film.models import (
    FilmModel, FilmTypeModel, CategoryModel, StaffModel, RoleModel
)


# FilmModel
class FilmGetSerializer(serializers.ModelSerializer):

    film_type = serializers.PrimaryKeyRelatedField(
        source='film_type.name',
        queryset=FilmTypeModel.objects.all()
    )
    id_category = serializers.SlugRelatedField(
        many=True,
        queryset=CategoryModel.objects.all(),
        slug_field='name'
    )
    id_staff = serializers.SlugRelatedField(
        many=True,
        queryset=StaffModel.objects.all(),
        slug_field='get_full_name'
    )

    class Meta:
        model = FilmModel
        fields = (
            'id', 'title', 'description', 'stock',
            'price', 'availability', 'release_date',
            'film_type', 'id_category', 'id_staff'
        )


class FilmSerializer(serializers.ModelSerializer):

    stock = serializers.IntegerField()
    availability = serializers.IntegerField()

    class Meta:
        model = FilmModel
        fields = (
            'id', 'title', 'description', 'stock',
            'price', 'availability', 'release_date',
            'film_type', 'id_category', 'id_staff'
        )

    def validate(self, data):
        stock = data['stock']
        availability = data['availability']
        if availability > stock:
            raise serializers.ValidationError(
                "The availability can't be higher than stock"
            )
        return data


# CategoryModel
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = (
            'id', 'name'
        )


# RoleModel
class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoleModel
        fields = (
            'id', 'name'
        )


# StaffModel
class StaffGetSerializer(serializers.ModelSerializer):

    id_role = serializers.PrimaryKeyRelatedField(
        source='id_role.name',
        queryset=StaffModel.objects.all()
    )

    class Meta:
        model = StaffModel
        fields = (
            'id', 'get_full_name', 'id_role'
        )


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaffModel
        fields = (
            'id', 'name', 'lastname', 'id_role'
        )


# FilmTypeModel
class FilmTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmTypeModel
        fields = (
            'id', 'name'
        )
