from django.shortcuts import render
from . import forms

    # Create your views here.
def index(request):
        return render(request,'AppTrans/index.html')
def form_name_view(request):
        form=forms.FormName()
        if request.method=='POST':
            form=forms.FormName(request.POST)
            if form.is_valid():
                print("Validation Success!")
                print("User Name: "+ form.cleaned_data['name'])
                print("Password "+ form.cleaned_data['password'])
        return render(request,'AppTrans/index.html',{'form':form})




# Create your views here.

















# Create your views here.
