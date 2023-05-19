from django.urls import path, include


app_name = 'api'
urlpatterns = [
    path('film/', include('api.film.urls')),
    path('rent/', include('api.rent.urls')),
    path('account/', include('api.account.urls')),
]
