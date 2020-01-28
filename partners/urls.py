from django.urls import path
from . import views

urlpatterns = [
    path('', views.PartnersList.as_view(), name='partners'),
    path('create/', views.PartnerCreation.as_view(), name='partner_new'),
    path('create/created_new_partner/', views.SuccessRegistration.as_view(), name='created_new_partner'),
]
