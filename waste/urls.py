from django.urls import path, include
from . import views

urlpatterns = [
    path('',include(views.index),name='index'),
]
