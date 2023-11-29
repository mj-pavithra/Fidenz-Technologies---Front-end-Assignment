from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_city_codes_and_weather, name='load_city_codes'),
]