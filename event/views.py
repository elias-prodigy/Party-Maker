from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .forms import EventForm
from .models import Event, Partners


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


class EventSendEmail(View):
    def post(self, request, **kwargs):
        event = get_object_or_404(Event, **kwargs)
        partners = Partners.objects.all()

        for partner in partners:
            html_data = render_to_string(
                'event/emails/emails_invait.html',
                context={"partner": partner, "event": event})
            plain_message = strip_tags(html_data)
            send_mail(
                event.event_name,
                plain_message,
                settings.EMAIL_HOST_USER,
                [partner.email],
                html_message=html_data,
                fail_silently=False,
            )
        return HttpResponse()


class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('event-list')
