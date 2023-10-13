from django.contrib import admin

# Register your models here.
from .models import KruegerJobDetail, PaperStock, MiscCost

class KruegerJobDetailInline(admin.StackedInline):
    model = KruegerJobDetail
    extra = 0
    readonly_fields = ['dateentered']

admin.site.register(KruegerJobDetail)

class MiscCostInline(admin.StackedInline):
    model = MiscCost
    extra = 0

admin.site.register(MiscCost)

class PaperStockInline(admin.StackedInline):
    model = PaperStock
    extra = 0
    
admin.site.register(PaperStock)
