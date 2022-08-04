from django.urls import path
from . import views

urlpatterns = [
    path('', views.snb_form, name='snb_form'),
]