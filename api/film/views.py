from rest_framework import generics, mixins

from film.models import (
    FilmModel, CategoryModel, RoleModel, StaffModel, FilmTypeModel
)
from .serializers import (
    FilmSerializer, FilmGetSerializer, CategorySerializer, RoleSerializer,
    StaffGetSerializer, StaffSerializer, FilmTypeSerializer
)


# Create your views here.
# FilmModel
class FilmAPIView(generics.ListAPIView):

    queryset = FilmModel.objects.all()
    serializer_class = FilmGetSerializer
    search_fields = (
        'title', 'film_type__name', 'id_category__name',
        'id_staff__name', 'id_staff__lastname'
    )
    ordering_fields = (
        'id', 'title', 'stock', 'price', 'availability', 'release_date'
    )


class FilmCreateAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    queryset = FilmModel.objects.all()
    serializer_class = FilmSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FilmRetrieveAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):

    queryset = FilmModel.objects.all()
    serializer_class = FilmSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# CategoryModel
class CategoryAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryRetrieveAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):

    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# RoleModel
class RoleAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RoleRetrieveAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):

    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# StaffModel
class StaffAPIView(generics.ListAPIView):

    queryset = StaffModel.objects.all()
    serializer_class = StaffGetSerializer
    search_fields = ('name', 'lastname', 'id_role__name')
    ordering_fields = ('id', 'name', 'lastname', 'id_role__name')


class StaffCreateAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    queryset = StaffModel.objects.all()
    serializer_class = StaffSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StaffRetrieveAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):

    queryset = StaffModel.objects.all()
    serializer_class = StaffSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# FilmTypeModel
class FilmTypeAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    queryset = FilmTypeModel.objects.all()
    serializer_class = FilmTypeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FilmTypeRetrieveAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):

    queryset = FilmTypeModel.objects.all()
    serializer_class = FilmTypeSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
