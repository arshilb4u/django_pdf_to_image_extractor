from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bantu', views.bantu, name='bantu'),
     
]