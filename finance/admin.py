from django.contrib import admin

# Register your models here.

from .models import AccountsPayable, DailySales

class AccountsPayableInline(admin.StackedInline):
    model = AccountsPayable
    extra = 0
    #readonly_fields = ['dateentered']

admin.site.register(AccountsPayable)

class DailySalesInline(admin.StackedInline):
    model = DailySales
    extra = 0

admin.site.register(DailySales)
