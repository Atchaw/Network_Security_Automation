from django.urls import path

from . import views

urlpatterns = [

    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', views.rule_list, name='rule_list'),
    path('rules/create/', views.rule_create, name='rule_create'),
    path('rules/<int:pk>/update/', views.rule_update, name='rule_update'),
    path('rules/<int:pk>/delete/', views.rule_delete, name='rule_delete'),
]
