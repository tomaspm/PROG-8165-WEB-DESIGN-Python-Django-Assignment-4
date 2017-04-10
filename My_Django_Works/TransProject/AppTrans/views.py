from django.shortcuts import render
from AppTrans.forms import UserForm,CategoriesForm,TransactionsForm
from AppTrans.models import Transactions

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'AppTrans/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def  dashboard(request):
    trans_list=Transactions.objects.order_by('dateoftrans')
    trans_dict={'trans':trans_list}
    return render(request,'AppTrans/dashboard.html', context=trans_dict)














@login_required
def category(request):
    if request.method=="POST":
        category_form=CategoriesForm(data=request.POST)

        if category_form.is_valid():
            categorydata=category_form.save(commit=False)
            categorydata.save()
        else:
            print(category_form.errors)
    else:
        category_form= CategoriesForm()
    return render(request,'AppTrans/addcategory.html')



@login_required
def transaction(request):
    if request.method=="POST":
        transaction_form=TransactionsForm(data=request.POST)
        if transaction_form.is_valid():
            transdata=transaction_form.save(commit=False)
            transdata.save()
        else:
            print(transaction_form.errors)
    else:
        transaction_form = TransactionsForm()
    return render(request, 'AppTrans/addtransaction.html')



def register(request):

    registered = False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)

        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm
    return render(request,'AppTrans/registration.html',{'user_form':user_form,'registered':registered})


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username:{} and password {}".format(username,password))
            return HttpResponse("invlaid login details supplied")
    else:
        return render(request,'AppTrans/login.html',{})
