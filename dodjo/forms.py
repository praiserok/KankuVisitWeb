from django import forms
from dodjo.models import *
from django.forms import (ModelForm, NumberInput, TextInput, Select,
                          CheckboxSelectMultiple, TimeInput)

####### ШКОЛА #######


class SchoolAddForm(ModelForm):

    class Meta:
        model = School
        # fields = '__all__'
        exclude = ['slug']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть назва'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть місто'}),
            'adress': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть адресу'}),
            'coach': Select(attrs={'class': 'form-select '}),
        }

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super().__init__(*args, **kwargs)
        self.fields['coach'].empty_label = None
        self.fields['coach'].queryset = Coach.objects.filter(
            id=user_id)


class GroupAddForm(ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'school', 'costMoon', 'costTraining']
        exclude = ['slug', 'coach']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть назву'}),
            # 'coach': Select(attrs={'class': 'form-select '}),
            'school': Select(attrs={'class': 'form-select '}),
            'costMoon': NumberInput(attrs={'class': 'form-control'}),
            'costTraining': NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super(GroupAddForm, self).__init__(*args, **kwargs)
        self.fields['school'].empty_label = None
        self.fields['school'].queryset = School.objects.filter(
            coach=user_id)


class TimetableAddForm(ModelForm):
    class Meta:
        model = Timetable
        # labels = {
        #     'timeStart': ('То що таке?'),
        # }
        help_texts = {
            'group': ('Для якої групи цей графік?'),
        }
        # fields = '__all__'
        exclude = ['slug']
        widgets = {
            'days': CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'timeStart': TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'timeFinish': TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'group': Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super().__init__(*args, **kwargs)
        self.fields['group'].empty_label = None
        self.fields['group'].queryset = Group.objects.filter(
            school__coach=user_id)
