from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Event


class EventList(ListView):

    model = Event
    paginate_by = 100

    # def event_list(self, request):
    #     events = get_object_or_404(Event, pk=pk)
    #     return render(request, 'event/event_list.html', {})
