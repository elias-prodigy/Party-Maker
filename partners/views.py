from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django_tables2 import SingleTableView
from .models import Partners
from event.models import Event
from .forms import CreatePartner
from .tables import PartnerTable


class PartnersList(SingleTableView):

    model = Partners
    table_class = PartnerTable
    template_name = 'partners/partners.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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


class DeletePartners(DeleteView):

    model = Partners

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse()


class UpdatePartners(UpdateView):

    model = Partners
    fields = ['name', 'surname', 'sponsor', 'manager_name']
    success_url = '/partners/'
