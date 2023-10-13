from django.urls import path

#from .views import (
#    newjob,
#)

#app_name='krueger'
#urlpatterns = [
    #path("kruegerprint/", newjob, name='krueger-print'),
#    path('', newjob, name='krueger-print'),
#]

from . import views

urlpatterns = [
    path('', views.newjob, name='krueger-print'),
    #path('papers/', views.paper, name='paper'),
    path('paperprice/', views.paperprice, name='paperprice'),
    #path('delete_customer/<int:pk>', views.papersizes, name='delete_customer'),
]