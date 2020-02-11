from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.html import strip_tags
from django.views import View

from django.views.generic import ListView, CreateView, DetailView, DeleteView, FormView
from django_tables2 import SingleTableView

from partners.forms import CreatePartner
from partners.tables import EventPartnerTable

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
                context={"partner": partner, "event": event, "event_id": event.pk})
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

# class TicketSendEmail(View):
#     def post(self, request, **kwargs):
#         event = get_object_or_404(Event, **kwargs)
#         partners = Partners.objects.all()
#
#         for partner in partners:
#             html_data = render_to_string(
#                 'event/emails/event_ticket.html',
#                 context={"partner": partner, "event": event})
#             plain_message = strip_tags(html_data)
#             send_mail(
#                 event.event_name,
#                 plain_message,
#                 settings.EMAIL_HOST_USER,
#                 [partner.email],
#                 html_message=html_data,
#                 fail_silently=False,
#             )
#         return HttpResponse()


class EventPartnersList(SingleTableView):

    model = Partners
    table_class = EventPartnerTable
    template_name = 'partners/event_partners.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['event'] = Event.objects.all()
        return context


class RegisterOnEvent(FormView):

    form_class = CreatePartner
    template_name = 'partners/create_partner.html'

    def get_success_url(self):
        return reverse('event-detail', kwargs=self.kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        partner = self.request.GET.get('partner')
        if partner:
            partner = Partners.objects.get(id=partner)
            kwargs["instance"] = partner
        return kwargs

    def form_valid(self, form):
        partner = form.save()
        event_id = self.kwargs.get('pk')
        event_qs = Event.objects.filter(id=event_id)
        if event_qs.exists():
            event_qs.first().visitors.add(partner)

        response = super().form_valid(form)
        return response


class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('event-list')
