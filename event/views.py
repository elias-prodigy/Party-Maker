from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView

from .forms import EventForm
from .models import Event


class EventList(ListView):

    model = Event
    paginate_by = 100


class CreateEvent(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event/create_event.html'
    success_url = "/event"


class EventDetailView(DetailView):
    model = Event
    template_name = 'event/detail.html'