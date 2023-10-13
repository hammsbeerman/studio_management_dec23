from django.db import models

class Customer(models.Model):
    company_name = models.CharField('Company Name', max_length=100, blank=True, null=True)
    first_name = models.CharField('First Name', max_length=100, blank=True, null=True)
    last_name = models.CharField('Last Name', max_length=100, blank=True, null=True)
    address1 = models.CharField('Address 1', max_length=100, blank=True, null=True)
    address2 = models.CharField('Adddress 2', max_length=100, blank=True, null=True)
    city = models.CharField('City', max_length=100, null=True)
    state = models.CharField('State', max_length=100, null=True)
    zipcode = models.CharField('Zipcode', max_length=100, blank=True, null=True)
    phone1 = models.CharField('Phone 1', max_length=100, blank=True, null=True)
    phone2 = models.CharField('Phone 2', max_length=100, blank=True, null=True)
    email = models.EmailField('Email', max_length=100, blank=True, null=True)
    website = models.URLField('Website', max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated = models.DateTimeField(auto_now = True, blank=False, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return (f"{self.company_name} {self.first_name} {self.last_name}") 
