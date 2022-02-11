from belt.models import Belt
from coach.models import Coach
from group.models import Group
from .models import Sportsman
from django import forms
from django.forms import (ModelForm, TextInput, EmailInput,
                          DateInput, NumberInput, Select)


class SportsmanAddForm(ModelForm):

    class Meta:
        model = Sportsman
        # fields = '__all__'
        # ['first_name', 'last_name', 'surname', 'dateBirth',
        #           'telephone', 'belts', 'group', 'coach', 'is_active']
        # '__all__'

        exclude = ['slug']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть ім\'я'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть прізвище'}),
            'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть побатькові', }),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введіть email'}),
            'dateBirth': DateInput(attrs={'type': 'date', 'class': 'form-control', }),
            'telephone': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введіть номер телефону'}),
            'belts': Select(attrs={'class': 'form-select '}),
            'group': Select(attrs={'class': 'form-select '}),
            'coach': Select(attrs={'class': 'form-select '})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['belts'].empty_label = 'Пояс не обарано'
        self.fields['group'].empty_label = 'Групу не обарано'
        self.fields['coach'].empty_label = 'Тренер не обарано'
