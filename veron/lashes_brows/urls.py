from django.urls import path
from . import views

urlpatterns = [
    path('all_info/', views.all_info, name='all_info'),
    path('all_info/master/', views.master_detail, name='master_info'),
    path('all_info/address/', views.address_detail, name='address_info'),
    path('all_info/info_service/', views.info_service_detail, name='info_service'),
    path('review_info/<int:review_id>/', views.review_detail, name='review_info'),
    path('all_info/gift_certificate/', views.gift_certificate_detail, name='gift_certificate_info'),
]
