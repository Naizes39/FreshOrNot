# classifier/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.classify, name='classify'),
]
