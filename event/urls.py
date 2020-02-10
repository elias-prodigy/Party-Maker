from django.urls import path

from . import views
from .views import EventList, CreateEvent, EventDetailView, EventSendEmail, EventDelete

urlpatterns = [
    path('', EventList.as_view(), name='event-list'),
    path('create/', CreateEvent.as_view(), name='create-event'),
    path('detail/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('send_email/<int:pk>/', EventSendEmail.as_view(), name='send-email'),
    path('event/<int:pk>/delete/', EventDelete.as_view(), name='event-delete')
]