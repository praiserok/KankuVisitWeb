from django import forms
from .models import Coach
from django.forms import (CheckboxInput, ModelForm, TextInput, Textarea, EmailInput,
                          PasswordInput, DateInput, NumberInput, URLInput,
                          Select)


class CoachAddForm(ModelForm):
    class Meta:
        model = Coach
        fields = '__all__'
        # exclude = ['is_active']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть ім\'я'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть прізвище'}),
            'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть побатькові', }),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введіть email'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введіть пароль'}),
            'dateBirth': DateInput(attrs={'type': 'date', 'class': 'form-control', }),
            'telephone': NumberInput(attrs={'class': 'form-control ', 'placeholder': 'Введіть номер телефону'}),
            'telephone2': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введіть 2 номер телефону'}),
            'information': Textarea(attrs={'class': 'form-control', 'placeholder': 'Інформація про вас', 'rows': '1'}),
            'photo': URLInput(attrs={'type': 'file', 'class': 'form-control'}),
            'belts': Select(attrs={'class': 'form-select '}),
        }


class CoachEditForm(ModelForm):
    class Meta:
        model = Coach
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть ім\'я'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть прізвище'}),
            'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть побатькові', }),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введіть email'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введіть пароль'}),
            'dateBirth': DateInput(attrs={'type': 'date', 'class': 'form-control', }),
            'telephone': NumberInput(attrs={'class': 'form-control ', 'placeholder': 'Введіть номер телефону'}),
            'telephone2': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введіть 2 номер телефону'}),
            'information': Textarea(attrs={'class': 'form-control', 'placeholder': 'Інформація про вас', 'rows': '1'}),
            'photo': URLInput(attrs={'type': 'file', 'class': 'form-control'}),
            'belts': Select(attrs={'class': 'form-select '}),
            'is_active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'flexSwitchCheckChecked'})}
