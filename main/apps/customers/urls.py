from django.urls import path
from . import views

urlpatterns = [

    path('contrato/list', views.ListContrato.as_view(), name='listcontrato'),
    

]