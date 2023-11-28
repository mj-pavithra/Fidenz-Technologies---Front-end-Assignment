from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_city_codes, name='load_city_codes'),
]