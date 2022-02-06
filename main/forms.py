from dataclasses import field, fields
from selectors import SelectSelector
from this import d
from .models import Sportsman, Coach, School, Belt, Group
from django import forms
from django.forms import (CheckboxInput, ModelForm, TextInput, Textarea, EmailInput,
                          PasswordInput, DateInput, NumberInput, URLInput,
                          Select)

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


class BeltAddForm(ModelForm):
    class Meta:
        model = Belt
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть назву'}),
            'kyu': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введіть'}),
            'img': URLInput(attrs={'type': 'file', 'class': 'form-control', }),
        }


class CoachAddForm(ModelForm):
    class Meta:
        model = Coach
        # fields = '__all__'
        exclude = ['is_active']
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
