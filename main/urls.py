from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('main.apps.home.urls')),
    path('core/', include('main.apps.core.urls'))
]
