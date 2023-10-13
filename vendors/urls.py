from django.urls import path

from .views import (
    vendor_create_view,
    vendor_detail_view,
    vendor_detail_hx_view,
    vendor_update_view,
)

app_name='vendors'
urlpatterns = [
    #path("", vendor_list_view, name='list'),
    path("create/", vendor_create_view, name='create'),
    path("<int:id>/", vendor_detail_view, name='detail'),
    path("hx/<int:id>/", vendor_detail_hx_view, name='hx-detail'),
    path("<int:id>/edit", vendor_update_view, name='update'),
]