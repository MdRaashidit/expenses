from expensesapp.models import investment
from django.shortcuts import redirect, render
from .models import investment
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

@login_required
def home(request):
    all_data=investment.objects.filter(user=request.user).order_by('dbdate').reverse()
    total = investment.objects.filter(user=request.user).aggregate(Sum('dbamount'))
    context = {'keypassword' : all_data, 'alltotal': total['dbamount__sum']}
    return render(request,'index.html',context)
    

@login_required
def add_expenses(request):
    if  request.method =="POST":
        addexpenses = request.POST.get('forminvest')
        addamount = request.POST.get('formamount')
        addplace = request.POST.get('formplace')
        addshop=request.POST.get('formshop')
        adddate=request.POST.get('formdate')
        new_password = investment(user=request.user, dbinvest=addexpenses, dbamount=addamount,dbplace=addplace,dbshopname=addshop,dbdate=adddate)
        new_password.save()
        return redirect('home')
    return render(request,'add.html')




def signup(request):
    if request.method=="POST":
        susername=request.POST.get('username')
        password=request.POST.get('password')
        encrypted_password = make_password(password)
        user = User(username=susername, password=encrypted_password)
        user.save() 
        return redirect('home')
    return render(request, "signup.html")
 