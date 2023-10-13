from django import forms
from .models import Customer

class AddCustomerForm(forms.ModelForm):
    company_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Company Name", "class":"form-control"}), label="")
    first_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    address1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Address 1", "class":"form-control"}), label="")
    address2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Address 2", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
    zipcode = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")
    phone1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone 1", "class":"form-control"}), label="")
    phone2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone 2", "class":"form-control"}), label="")
    email = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    website = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Website", "class":"form-control"}), label="")

    class Meta:
        model = Customer
        exclude = ("user",)