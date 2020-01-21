from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CreatePartner
from django.utils import timezone
# Create your views here.


def partners_list(request):
    return render(request, 'partners/partners.html', {})


def create_partner(request):
    if request.method == "POST":
        form = CreatePartner(request.POST)
        if form.is_valid():
            partner = form.save()
            partner.published_date = timezone.now()
            partner.save()
            return redirect('created_new_partner')
            """, pk=partner.pk - добавить в скобки, в предыдущую строку, чтобы задать каждому 
            Партнеру уникальный порядковый номер"""
    else:
        form = CreatePartner()
    return render(request, 'partners/create_partner.html', {'form': form})


def created_new_partner(request):
    return render(request, 'partners/partner_is_created.html', {})
