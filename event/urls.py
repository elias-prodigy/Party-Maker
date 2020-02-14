from django.urls import path

from .views import EventList, CreateEvent, EventDetailView, EventSendEmail, EventDelete, EventPartnersList, \
    RegisterOnEvent, UpdatePartnersOnEvent, TicketSendEmail

urlpatterns = [
    path('', EventList.as_view(), name='event-list'),
    path('create/', CreateEvent.as_view(), name='create-event'),
    path('detail/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('send_email/<int:pk>/', EventSendEmail.as_view(), name='send-email'),
    path('send_ticket/<int:pk>/', TicketSendEmail.as_view(), name='ticket-email'),
    path('<int:pk>/delete/', EventDelete.as_view(), name='event-delete'),
    path('<int:pk>/table', EventPartnersList.as_view(), name='event_partner_table'),
    path('<int:pk>/register/', RegisterOnEvent.as_view(), name='register-to-event'),
    path('update/<int:pk>/', UpdatePartnersOnEvent.as_view(), name='update_partners_event'),

]