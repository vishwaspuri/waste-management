from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('bin-list/',views.worker_bin_list,name='worker_bin_list'),
    path('bin/<int:pk>/',views.worker_bin_detail,name = 'worker_bin_detail'),

]
