from django.urls import path
from . import views

urlpatterns = [
    path('', views.partners_list, name='partners'),
    path('create/', views.create_partner, name='partner_new'),
    path('created_new_partner/', views.created_new_partner, name='created_new_partner'),
]
