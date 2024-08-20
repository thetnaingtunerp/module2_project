from django import forms
from .models import *
class itemcreateform(forms.ModelForm):
    class Meta:
        model = item
        fields = '__all__'
        widgets = {
            'itemname': forms.TextInput(attrs={'class': 'form-control', 'required':'true'}),
            'category': forms.Select(attrs={'class': 'form-control', 'required':'true'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'required':'true'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'required':'true'}),
        }


class categoryform(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'
        widgets = {
            'categoryname': forms.TextInput(attrs={'class': 'form-control', 'required':'true'}),
           
        }


class ULoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())