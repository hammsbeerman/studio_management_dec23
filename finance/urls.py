from django.urls import path
from . import views

urlpatterns = [
    path('', views.finance_main, name='finance'),
    path('ap/', views.add_bill_payable, name='add_bill_payable'),
    path('daily_sale/', views.add_daily_sale, name='add_daily_sale'),
    #path('', views.customer_list, name='customer_list'),
    #path('record/<int:pk>', views.customer_record, name='customer_record'),
    #path('delete_customer/<int:pk>', views.delete_customer, name='delete_customer'),
    #path('update_customer/<int:pk>', views.update_customer, name='update_customer'),
    #path('add_ap/', views.add_customer, name='add_customer'),
]