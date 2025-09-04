from django.urls import path
from . import views


urlpatterns = [
    path('unidade/list', views.ListUnidade.as_view(), name='listunidade'),
    path('unidade/add', views.UnidadeAdd.as_view(), name='addunidade'),
    path('unidade/edit/<int:id>', views.UnidadeEdit.as_view(), name='editunidade')
    
]