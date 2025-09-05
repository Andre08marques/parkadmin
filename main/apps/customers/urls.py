from django.urls import path
from . import views

urlpatterns = [

    path('contrato/list', views.ListContrato.as_view(), name='listcontrato'),
    path('contrato/add', views.ContratoAdd.as_view(), name='addcontrato'),
    path('contrato/edit/<int:id>', views.ContratoEdit.as_view(), name='editcontrato'),
    

]