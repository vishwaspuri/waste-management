from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('bin-list/',views.worker_bin_list,name='worker_bin_list'),
    path('bin/<int:pk>/',views.worker_bin_detail,name = 'worker_bin_detail'),
    path('list/',views.citizen_bin_list, name='citizen_bin_list'),
    path('citizen-bin/<int:pk>/',views.bin_detail, name='bin_detail'),
    path('bin/new/', views.new_bin, name='new_bin'),
]
