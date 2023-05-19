from rest_framework import serializers

from rent.models import RentModel
from film.models import FilmModel
from account.models import CustomUser


class RentGetSerializer(serializers.ModelSerializer):

    id_user = serializers.PrimaryKeyRelatedField(
        source='id_user.username',
        queryset=CustomUser.objects.all()
    )
    id_film = serializers.PrimaryKeyRelatedField(
        source='id_film.title',
        queryset=FilmModel.objects.all()
    )

    class Meta:
        model = RentModel
        fields = (
            'id', 'id_user', 'id_film', 'rent_date', 'expected_return_day',
            'return_day', 'tax', 'debt'
        )


class RentSerializer(serializers.ModelSerializer):

    tax = serializers.IntegerField(read_only=True)
    debt = serializers.IntegerField(read_only=True)

    class Meta:
        model = RentModel
        fields = (
            'id', 'id_user', 'id_film', 'rent_date', 'expected_return_day',
            'return_day', 'tax', 'debt'
        )
