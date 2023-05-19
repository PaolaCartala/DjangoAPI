from rest_framework import generics, mixins

from account.models import CustomUser
from .serializers import CustomUserSerializer


# Create your views here.
# CustomUser
class CustomUserAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    search_fields = ('username', 'first_name', 'last_name')
    ordering_fields = ('id', 'username', 'email')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomUserRetrieveAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
