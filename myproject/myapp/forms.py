from django import forms
from .models import *
class itemcreateform(forms.ModelForm):
    class Meta:
        model = item
        fields = '__all__'
        widgets = {
            'itemname': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }