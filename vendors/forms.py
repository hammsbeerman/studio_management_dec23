from django import forms
from .models import Vendor

class VendorForm(forms.ModelForm):
    required_css_class = 'required-field'
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Vendor name"}))
    #active = forms.BooleanField(widget=forms.CheckboxInput(attrs={"default": "True"}))
    class Meta:
        model = Vendor
        fields = ['name',  'address1',  'address2', 'city', 'state', 'zipcode', 'phone1', 'phone2', 'email', 'website', 'active']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            print(field)
            new_data = {
                "placeholder": f'Vendor {str(field)}',
                "class": 'form-control',
                #"hx-post": "",
                #"hx-trigger": "keyup changed delay:500ms",
                #"hx-target": "#recipe-container",
                #"hx-swap": "outerHTML"
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
        #self.fields['description'].widget.attrs.update({'rows': '2'})
        #self.fields['directions'].widget.attrs.update({'rows': '4'})