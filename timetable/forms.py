from django import forms
from django.forms import (CheckboxInput, CheckboxSelectMultiple,
                          ModelForm, Select, TextInput, TimeInput)
from .models import Timetable


class TimetableAddForm(ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'
        widgets = {
            'days': Select(attrs={'class': 'form-select'}),
            'timeStart': TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'timeFinish': TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'group': Select(attrs={'class': 'form-select'})
        }
