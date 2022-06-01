from django.http import HttpResponse
from . import models
from django.shortcuts import render
from django.shortcuts import get_object_or_404

def main_page(request):
    return HttpResponse("VERON LASHES & BROWS")

def all_info(request):
    info = models.Master.objects.all()
    return HttpResponse(info)

def all_info(request):
    info = models.Master.objects.all()
    context = {
        'info': info,
    }
    return render(request, 'all_info.html', {'context': context})

def master_detail(request, master_id):
    master = get_object_or_404(models.Master, id=master_id)
    context = {
        'master': master,
    }
    return render(request, 'master_info.html', {'context': context})

def certificate_detail(request, certificate_id):
    certificate = get_object_or_404(models.Certificate, id=certificate_id)
    context = {
        'certificate': certificate,
    }
    return render(request, 'certificate_info.html', {'context': context})

def address_detail(request, address_id):
    address = get_object_or_404(models.Address, id=address_id)
    context = {
        'address': address,
    }
    return render(request, 'address_info.html', {'context': context})

def service_detail(request, service_id):
    service = get_object_or_404(models.Service, id=service_id)
    context = {
        'service': service,
    }
    return render(request, 'service_info.html', {'context': context})

def review_detail(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    context = {
        'review': review,
    }
    return render(request, 'review_info.html', {'context': context})

def price_detail(request, price_id):
    price = get_object_or_404(models.Price, id=price_id)
    context = {
        'price': price,
    }
    return render(request, 'price_info.html', {'context': context})

def gift_certificate_detail(request, gift_certificate_detail_id):
    gift_certificate_detail = get_object_or_404(models.Gift_certificate, id=gift_certificate_detail_id)
    context = {
        'gift_certificate_detail': gift_certificate_detail,
    }
    return render(request, 'gift_certificate_detail_info.html', {'context': context})