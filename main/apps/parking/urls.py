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
    path('tipos-cobranca/novo/', views.TipoCobrancaCreateView .as_view(), name='tipocobranca_create'),
    path('tipos-cobranca/<int:pk>/editar/', views.TipoCobrancaUpdateView.as_view(), name='tipocobranca_update'),
    path('tipos-cobranca/<int:pk>/deletar/', views.TipoCobrancaDeleteView.as_view(), name='tipocobranca_delete'),
    
    # Preco URLs
    path('precos/', views.PrecoListView.as_view(), name='preco_list'),
    path('precos/novo/', views.PrecoCreateView.as_view(), name='preco_create'),
    path('precos/<int:pk>/editar/', views.PrecoUpdateView.as_view(), name='preco_update'),
    path('precos/<int:pk>/deletar/', views.PrecoDeleteView.as_view(), name='preco_delete'),
]