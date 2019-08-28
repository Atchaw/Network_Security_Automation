from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [

    path('', views.dash, name='mytopology'),
    path('data/', views.topo, name='topo'),

    ]
