from rest_framework import status
from rest_framework.response import Response

from .utils import RentUtils


class RentServices:

    @staticmethod
    def create(request, serializer, *args, **kwarg):
        serializer = serializer(data=request.data)
        if serializer.is_valid():
            available = RentUtils.verify_availability(
                serializer.validated_data['id_film'].id
            )
            if available:
                serializer.save()
                RentUtils.update_availability(
                    serializer.data['id_film'], 'subst'
                )
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update(request, id, model, serializer, *args, **kwargs):
        instance = model.objects.get(id=id)
        if not instance:
            return Response(
                {"res": "Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        RentUtils().update_debt(instance)
        serializer = serializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            RentUtils.update_availability(serializer.data['id_film'], 'add')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
