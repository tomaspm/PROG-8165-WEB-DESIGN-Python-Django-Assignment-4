from django import forms
from django.contrib.auth.models import User
from AppTrans.models import Categories
from AppTrans.models import Transactions

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password','first_name','last_name')

class CategoriesForm(forms.ModelForm):
    class Meta():
        model=Categories
        fields=('category',)

class TransactionsForm(forms.ModelForm):
    class Meta:
        model=Transactions
        fields=('dateoftrans','description','transcategory','amount')
