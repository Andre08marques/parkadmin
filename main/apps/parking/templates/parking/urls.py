from django.urls import path
from . import views

app_name = 'parking'

urlpatterns = [
    # TabelaPreco URLs
    path('tabelas/', views.TabelaPrecoListView.as_view(), name='tabelapreco_list'),
    path('tabelas/criar/', views.TabelaPrecoCreateView.as_view(), name='tabelapreco_create'),
    path('tabelas/<int:pk>/editar/', views.TabelaPrecoUpdateView.as_view(), name='tabelapreco_update'),
    path('tabelas/<int:pk>/deletar/', views.TabelaPrecoDeleteView.as_view(), name='tabelapreco_delete'),
    
    # TipoVeiculo URLs
    path('tipos-veiculo/', views.TipoVeiculoListView.as_view(), name='tipoveiculo_list'),
    path('tipos-veiculo/novo/', views.TipoVeiculoCreateView.as_view(), name='tipoveiculo_create'),
    path('tipos-veiculo/<int:pk>/editar/', views.TipoVeiculoUpdateView.as_view(), name='tipoveiculo_update'),
    path('tipos-veiculo/<int:pk>/deletar/', views.TipoVeiculoDeleteView.as_view(), name='tipoveiculo_delete'),
    
    # TipoCobranca URLs
    path('tipos-cobranca/', views.TipoCobrancaListView.as_view(), name='tipocobranca_list'),
    # ... Add other TipoCobranca URLs
    
    # Preco URLs
    path('precos/', views.PrecoListView.as_view(), name='preco_list'),
    # ... Add other Preco URLs
]