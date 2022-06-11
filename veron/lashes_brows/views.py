from django.http import HttpResponse
from . import models
from django.shortcuts import render

def all_info(request):
    return render(request, 'all_info.html')

def master_detail(request):
    return render(request, 'master.html')

def address_detail(request):
    return render(request, 'address.html')

def info_service_detail(request):
    services = models.Service.objects.all()
    reviews = models.Review.objects.all()
    context = {
        'services': services,
        'reviews': reviews,
    }
    return render(request, 'info_service.html', {'context': context})


def review_detail(request, review_id):
    reviews = get_object_or_404(models.Review, id=review_id)
    context = {
        'review': reviews,
    }
    return render(request, 'review.html', {'context': context})

def gift_certificate_detail(request):
    return render(request, 'gift_certificate.html')
