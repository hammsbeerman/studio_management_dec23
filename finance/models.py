from django.db import models
from vendors.models import Vendor


class AccountsPayable(models.Model):
    date_recieved = models.DateField(auto_now=False, auto_now_add=False)
    vendor = models.ForeignKey(Vendor, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.CharField('Description', max_length=100, blank=True, null=True)
    invoice_number = models.CharField('Invoice Number', max_length=100, blank=True, null=True)
    amount = models.DecimalField('Amount', max_digits=10, decimal_places=2)
    discount = models.DecimalField('Discount', blank=True, null=True, max_digits=10, decimal_places=2)
    discount_date_due = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    paid = models.BooleanField('Paid', null=True)
    date_paid = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    amount_paid = models.DecimalField('Amount Paid', blank=True, null=True, max_digits=10, decimal_places=2)


    def __str__(self):
        #Pulling from Foreign Key
        return self.vendor.name
    
class DailySales(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False)
    cash = models.DecimalField('Cash', max_digits=10, decimal_places=2, blank=True, null=True)
    checks = models.DecimalField('Checks', max_digits=10, decimal_places=2, blank=True, null=True)
    creditcard = models.DecimalField('Credit Card', max_digits=10, decimal_places=2, blank=True, null=True)
    creditcard_fee = models.DecimalField('Credit Card Fee', max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        #Formatted this way to convert datetime to string
        return str(self.date)