from django.shortcuts import render

# Create your views here.


def partners_list(request):
    return render(request, 'partners/partners.html', {})


def create_partner(request):
    return render(request, 'partners/create_partner.html', {})