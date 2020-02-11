from django.urls import path
from . import views

urlpatterns = [
    path('', views.PartnersList.as_view(), name='partners'),
    path('create/', views.PartnerCreation.as_view(), name='partner_new'),
    path('create/created_new_partner/', views.SuccessRegistration.as_view(), name='created_new_partner'),
    path('<pk>/delete/', views.DeletePartners.as_view(), name='delete_partners'),
    path('<pk>/update/', views.UpdatePartners.as_view(), name='update_partners'),
]
