from django.urls import path
from . import views

urlpatterns = [
    path('', views.partners_list, name='partners'),
    path('create/', views.create_partner, name='partner_new'),
]