from django.urls import path

from .views import (
    FilmAPIView, FilmCreateAPIView, FilmRetrieveAPIView,
    CategoryAPIView, CategoryRetrieveAPIView,
    RoleAPIView, RoleRetrieveAPIView,
    StaffAPIView, StaffCreateAPIView, StaffRetrieveAPIView,
    FilmTypeAPIView, FilmTypeRetrieveAPIView
)


urlpatterns = [
    path('', FilmAPIView.as_view(), name='film'),
    path('create/', FilmCreateAPIView.as_view(), name='film-create'),
    path(
        '<int:id>/', FilmRetrieveAPIView.as_view(),
        name='film-up-del'
    ),
    path('category/', CategoryAPIView.as_view(), name='category'),
    path(
        'category/<int:id>/', CategoryRetrieveAPIView.as_view(),
        name='category-up-del'
    ),
    path('role/', RoleAPIView.as_view(), name='role'),
    path(
        'role/<int:id>/', RoleRetrieveAPIView.as_view(),
        name='role-up-del'
    ),
    path('staff/', StaffAPIView.as_view(), name='staff'),
    path('staff/create/', StaffCreateAPIView.as_view(), name='staff-create'),
    path(
        'staff/<int:id>/', StaffRetrieveAPIView.as_view(),
        name='staff-up-del'
    ),
    path('filmtype/', FilmTypeAPIView.as_view(), name='filmtype'),
    path(
        'filmtype/<int:id>/', FilmTypeRetrieveAPIView.as_view(),
        name='filmtype-up-del'
    ),
]
