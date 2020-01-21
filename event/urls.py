from django.urls import path

from . import views
from .views import EventList

urlpatterns = [
    path('', EventList.as_view(), name='event-list')

]