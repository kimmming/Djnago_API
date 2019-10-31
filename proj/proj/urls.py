
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include
from mys import urls
from rest_framework import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mys.urls')),
    path('api-auth/',include('rest_framework.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
