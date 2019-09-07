from django.urls import path
from . import views


urlpatterns = [

    path('', views.dash, name='mytopology'),
    path('data/', views.topo, name='topo'),

    ]
