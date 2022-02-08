from belt.models import Belt
from django import forms
from django.forms import (ModelForm, TextInput, NumberInput, URLInput)


class BeltAddForm(ModelForm):
    class Meta:
        model = Belt
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть назву'}),
            'fullname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть повну назву'}),
            'number': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введіть номер поясу'}),
            'img': URLInput(attrs={'type': 'file', 'class': 'form-control', }),
        }
