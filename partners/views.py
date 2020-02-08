from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Partners
from event.models import Event
from .forms import CreatePartner
from django.utils import timezone


class PartnersList(ListView):

    model = Partners
    template_name = 'partners/partners.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['event'] = Event.objects.all()
        return context


class PartnerCreation(CreateView):

    model = Partners
    form_class = CreatePartner
    template_name = 'partners/create_partner.html'
    success_url = 'created_new_partner/'


class SuccessRegistration(View):

    def get(self, request):
        return render(request, 'partners/partner_is_created.html', {})


#def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['event'] = Event.objects.all()
    #     return context