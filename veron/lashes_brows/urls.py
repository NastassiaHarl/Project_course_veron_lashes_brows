from django.urls import path
from . import views

urlpatterns = [
    path('main_page/', views.main_page, name='veron'),
    path('all_info/', views.all_info, name='all_info'),
    path('master_info/<int:master_id>/', views.master_detail, name='master_info'),
    path('certificate_info/<int:certificate_id>/', views.certificate_detail, name='certificate_info'),
    path('address_info/<int:address_id>/', views.address_detail, name='address_info'),
    path('service_info/<int:service_id>/', views.service_detail, name='service_info'),
    path('review_info/<int:review_id>/', views.review_detail, name='review_info'),
    path('price_info/<int:price_id>/', views.price_detail, name='price_info'),
    path('gift_certificate_info/<int:gift_certificate_id>/', views.gift_certificate_detail, name='gift_certificate_info'),
]
