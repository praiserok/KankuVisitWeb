from dataclasses import field, fields
from django import forms
from .models import Coach
from django.forms import (CheckboxInput, ModelForm, TextInput, Textarea, EmailInput,
                          PasswordInput, DateInput, NumberInput, URLInput,
                          Select)


class CoachAddForm(ModelForm):
    class Meta:
        model = Coach
        fields = ['first_name', 'last_name', 'surname', 'dateBirth',
                  'telephone', 'email', 'information', 'belts', 'is_active']
        exclude = ['slug']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть ім\'я'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть прізвище'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введіть email'}),
            'is_active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'flexSwitchCheckChecked'}),
            'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть побатькові', }),
            'dateBirth': DateInput(attrs={'type': 'date', 'class': 'form-control', }),
            'telephone': NumberInput(attrs={'class': 'form-control ', 'placeholder': 'Введіть номер телефону'}),
            # 'telephone2': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введіть 2 номер телефону'}),
            'information': Textarea(attrs={'class': 'form-control', 'placeholder': 'Інформація про вас', 'rows': '1'}),
            'belts': Select(attrs={'class': 'form-select '}),
            # 'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введіть пароль'}),
            # 'photo': URLInput(attrs={'type': 'file', 'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['belts'].empty_label = 'Пояс не обарано'
