from school.models import School
from django import forms
from django.forms import (ModelForm, TextInput, Select)


class SchoolAddForm(ModelForm):

    class Meta:
        model = School
        # fields = '__all__'
        exclude = ['is_active']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть назва'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть місто'}),
            'adress': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть адресу'}),
            'coach': Select(attrs={'class': 'form-select '})
        }
