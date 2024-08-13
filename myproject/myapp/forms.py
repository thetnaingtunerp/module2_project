from django import forms
from .models import *
class itemcreateform(forms.ModelForm):
    class Meta:
        model = item
        fields = '__all__'
        widgets = {
            'itemname': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class categoryform(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'
        widgets = {
            'categoryname': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
