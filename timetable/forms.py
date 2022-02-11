from django import forms
from django.forms import (CheckboxInput, CheckboxSelectMultiple,
                          ModelForm, Select, SelectMultiple, TextInput, TimeInput)
from .models import Timetable


class TimetableAddForm(ModelForm):
    class Meta:
        model = Timetable
        # fields = '__all__'
        exclude = ['slug']
        widgets = {
            'days': CheckboxSelectMultiple(attrs={'class': ''}),
            'timeStart': TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'timeFinish': TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'group': Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].empty_label = 'Групу не обарано'
