from django.urls import path
from . import views

urlpatterns = [
    # URLs para Veículo
    path('veiculo/list', views.ListVeiculo.as_view(), name="listveiculo"),
    path('veiculo/add', views.VeiculoAdd.as_view(), name="addveiculo"),
    path('veiculo/edit/<int:id>', views.VeiculoEdit.as_view(), name="editveiculo"),
    path('veiculo/delete/<int:id>', views.VeiculoDelete.as_view(), name="deleteveiculo"),
    
    # URLs para Tipo de Veículo
    path('tipo/list', views.ListTipoVeiculo.as_view(), name="list_tipo_veiculo"),
    path('tipo/add', views.TipoVeiculoAdd.as_view(), name="add_tipo_veiculo"),
    path('tipo/edit/<int:id>', views.TipoVeiculoEdit.as_view(), name="edit_tipo_veiculo"),
    path('tipo/delete/<int:id>', views.TipoVeiculoDelete.as_view(), name="delete_tipo_veiculo"),
]