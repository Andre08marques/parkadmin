from django.urls import path
from . import views

urlpatterns = [
    path('veiculo/list', views.ListVeiculo.as_view(), name="listveiculo"),
    path('veiculo/add', views.VeiculoAdd.as_view(), name="addveiculo"),
    path('veiculo/edit/<int:id>', views.VeiculoEdit.as_view(), name="editveiculo"),
    
]