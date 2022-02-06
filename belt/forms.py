from belt.models import Belt
from django import forms
from django.forms import (ModelForm, TextInput, NumberInput, URLInput)


class BeltAddForm(ModelForm):
    class Meta:
        model = Belt
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть назву'}),
            'kyu': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введіть'}),
            'img': URLInput(attrs={'type': 'file', 'class': 'form-control', }),
        }
