from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import AddCustomerForm
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customers.html', {'customers':customers})

def customer_record(request, pk):
    if request.user.is_authenticated:
        #Look up records
        customer_record = Customer.objects.get(id=pk)
        return render(request, 'customers/record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')
    
def delete_customer(request, pk):
    if request.user.is_authenticated:
        delete_customer = Customer.objects.get(id=pk)
        delete_customer.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('customer_list')
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')
    
def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('customer_list')
        return render(request, 'customers/add_customer.html', {'form':form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')
    
def update_customer(request, pk):
    if request.user.is_authenticated:
        current_record = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=current_record)
        #instance=current_record fills out the form with current data from db
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been saved")
            return redirect('customer_list')
        return render(request, 'customers/update_customer.html', {'form':form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')