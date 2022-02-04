from .models import Sportsman, Task
from .models import Coach

from django.forms import (ModelForm, TextInput, Textarea, EmailInput,
                          PasswordInput, DateInput, NumberInput, URLInput,
                          Select)


class CoachForm(ModelForm):

    class Meta:
        model = Coach
        fields = [
            'first_name', 'last_name', 'surname', 'email', 'password',
            'dateBirth', "telephone", "telephone2", "information", 'photo',
            'belt'
            # '__all__'
        ]
        widgets = {
            'first_name':
            TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ім\'я'
            }),
            'last_name':
            TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть прізвище'
            }),
            'surname':
            TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть побатькові',
            }),
            'email':
            EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть email'
            }),
            'password':
            PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть пароль'
            }),
            'dateBirth':
            DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'telephone':
            NumberInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Введіть номер телефону'
            }),
            'telephone2':
            NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть 2 номер телефону'
            }),
            'information':
            Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Інформація про вас',
                    'rows': '1'
                }),
            'photo':
            URLInput(attrs={
                'type': 'file',
                'class': 'form-control',
            }),
            'belt':
            Select(attrs={
                'class': 'form-select',
            }),
        }


class SportsmanForm(ModelForm):

    class Meta:
        model = Sportsman
        fields = [
            'first_name', 'last_name', 'surname', 'dateBirth', "telephone",
            'belt'
        ]
        widgets = {
            'first_name':
            TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ім\'я'
            }),
            'last_name':
            TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть прізвище'
            }),
            'surname':
            TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть побатькові',
            }),
            'dateBirth':
            DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'telephone':
            NumberInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Введіть номер телефону'
            }),
            'belt':
            Select(attrs={
                'class': 'form-select',
            }),
        }