from django import forms
from django.forms import TextInput, EmailInput

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city']
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 20%; float:left; ',
                'placeholder': 'First Name'
            }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 20%;float:left;',
                'placeholder': 'Last Name'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
            'address': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Address'
            }),
            'city': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'City'
            }),
        }

