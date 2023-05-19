from django.urls import path

from .views import (
    CustomUserAPIView, CustomUserRetrieveAPIView
)


urlpatterns = [
    path('', CustomUserAPIView.as_view(), name='account'),
    path(
        '<int:id>/', CustomUserRetrieveAPIView.as_view(),
        name='account-up-del'
    ),
]
