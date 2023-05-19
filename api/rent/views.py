from rest_framework import generics, mixins

from rent.models import RentModel
from .serializers import RentGetSerializer, RentSerializer
from .services import RentServices


# Create your views here.
# RentModel
class RentAPIView(generics.ListAPIView):

    queryset = RentModel.objects.all()
    serializer_class = RentGetSerializer
    search_fields = ('id_user__username', 'id_film__title')
    ordering_fields = (
        'id', 'id_user__id', 'id_film__id',
        'rent_date', 'expected_return_day', 'tax'
    )


class RentCreateAPIView(generics.ListAPIView):

    queryset = RentModel.objects.all()
    serializer_class = RentSerializer

    @staticmethod
    def post(request, *args, **kwargs):
        return RentServices.create(
            request, RentSerializer, *args, **kwargs
        )


class RentRetrieveAPIView(
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):

    queryset = RentModel.objects.all()
    serializer_class = RentSerializer
    lookup_field = 'id'

    @staticmethod
    def put(request, id, *args, **kwargs):
        return RentServices.update(
            request, id, RentModel, RentSerializer, *args, **kwargs
        )

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
