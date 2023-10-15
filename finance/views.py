from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import AccountsPayableForm, DailySalesForm
from .models import AccountsPayable

# Create your views here.

def finance_main(request):
    return render(request, 'finance/main.html')

def add_bill_payable(request):
    form = AccountsPayableForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('add_bill_payable')
        return render(request, 'finance/add_ap.html', {'form':form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')
    
def add_daily_sale(request):
    form = DailySalesForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('add_daily_sale')
        return render(request, 'finance/add_daily_sale.html', {'form':form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')
