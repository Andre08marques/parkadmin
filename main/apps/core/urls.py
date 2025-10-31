from django.urls import path
from . import views


urlpatterns = [
    # CRUD for Unidade
    path('unidade/list', views.ListUnidade.as_view(), name='listunidade'),
    path('unidade/add', views.UnidadeAdd.as_view(), name='addunidade'),
    path('unidade/edit/<int:id>', views.UnidadeEdit.as_view(), name='editunidade'),
    path('unidade/delete/<int:id>', views.UnidadeDelete.as_view(), name='deleteunidade'),

    # CRUD for Patio
    path('patios/', views.PatioListView.as_view(), name='patio_list'),
    path('patios/create/', views.PatioCreateView.as_view(), name='patio_create'),
    path('patios/<int:pk>/update/', views.PatioUpdateView.as_view(), name='patio_update'),
    path('patios/<int:pk>/delete/', views.PatioDeleteView.as_view(), name='patio_delete'),

    # CRUD for Vaga
    path('vagas/', views.VagaListView.as_view(), name='vaga_list'),
    path('vagas/create/', views.VagaCreateView.as_view(), name='vaga_create'),
    path('vagas/<int:pk>/update/', views.VagaUpdateView.as_view(), name='vaga_update'),
    path('vagas/<int:pk>/delete/', views.VagaDeleteView.as_view(), name='vaga_delete'),
]