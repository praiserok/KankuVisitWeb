from belt.models import Belt
from coach.models import Coach
from group.models import Group
from .models import Sportsman
from django import forms
from django.forms import (ModelForm, TextInput, EmailInput,
                          DateInput, NumberInput, Select)

formattrsall = {'class': 'form-control', 'placeholder': "Example"}
formattrsselect = {'class': 'form-select', 'type': 'date'}


class SportsmanEditForm(forms.Form):
    first_name = forms.CharField(label='Імя', max_length=20)
    last_name = forms.CharField(label='Прізвище', max_length=25)
    surname = forms.CharField(label='По батькові', max_length=20)
    dateBirth = forms.DateField(label='Дата народження')
    telephone = forms.IntegerField(label='Номер телефону')
    belts = forms.ModelChoiceField(queryset=Belt.objects.all(),
                                   label='Рівень поясу', empty_label='Пояс не обрано')
    coach = forms.ModelChoiceField(queryset=Coach.objects.all(),
                                   label='Тренер', empty_label='Тренера не обрано')
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   label='Група в якій тренується', empty_label='Групу не обрано')
    is_active = forms.BooleanField(label='Тренується?', initial=True,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    qwe = [first_name, last_name, surname,
           dateBirth, telephone, belts, coach, group]

    i = 0
    while i < len(qwe):
        qwe[i].widget.attrs.update(formattrsall)
        i += 1


class SportsmanAddForm(ModelForm):

    class Meta:
        model = Sportsman
        # fields = ['first_name', 'last_name', 'surname', 'dateBirth', 'telephone', 'belts', 'group', 'coach'
        #           ]
        exclude = ['is_active']
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
