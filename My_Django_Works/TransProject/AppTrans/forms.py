from django import forms
class FormName(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
def clean(self):
    all_clean_data=super().clean()
