from django.urls import path

from .views import (
    RentAPIView, RentCreateAPIView, RentRetrieveAPIView,
)


urlpatterns = [
    path('', RentAPIView.as_view(), name='rent'),
    path('create/', RentCreateAPIView.as_view(), name='rent-create'),
    path(
        '<int:id>/', RentRetrieveAPIView.as_view(),
        name='rent-up-del'
    ),
]
