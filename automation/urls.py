from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('network_admin.urls')),
    path('layer2/', include('layer2.urls')),
    path('layer3/', include('layer3.urls')),
    path('mytopology/', include('topology.urls')),

  ]
