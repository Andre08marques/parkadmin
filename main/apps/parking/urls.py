from django.urls import path
from . import views


urlpatterns = [
    path('table/price/list', views.ListTablePrice.as_view(), name='listtableprice'),
    path('table/price/add', views.TablePriceAdd.as_view(), name='addtableprice'),
    path('table/price/edit/<int:id>', views.TablePriceEdit.as_view(), name='edittableprice'),
    path('table/price/delete/<int:id>', views.TablePriceDelete.as_view(), name='deletetableprice')
]