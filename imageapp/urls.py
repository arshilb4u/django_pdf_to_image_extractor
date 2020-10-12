from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('convert_data', views.convert_data, name='convert'),
     
]
