from django.urls import path
from . import views

urlpatterns = [

    path('', views.device_list_view, name='device_list_view'),
    path('<str:hostname>/details', views.device_detail_view, name='device_detail'),
    path('<str:hostname>/interfaces', views.device_get_interfaces, name='device_get_interfaces'),
    path('<str:host>/port_security/', views.port_security, name='port_security'),
    path('dhcpSnooping/', views.dhcpSnooping, name='dhcpSnooping'),
    path('arppoising/', views.arppoising, name='arppoising'),
    path('stp/', views.stp, name='stp'),

]
