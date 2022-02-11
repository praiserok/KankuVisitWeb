from django import forms
from django.forms import (ModelForm, Select, TextInput)
from group.models import Group


class GroupAddForm(ModelForm):
    class Meta:
        model = Group
        # fields = '__all__'
        exclude = ['slug']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть назву'}),
            'coach': Select(attrs={'class': 'form-select '}),
            'school': Select(attrs={'class': 'form-select '})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['school'].empty_label = 'Школи не обарано'
        self.fields['coach'].empty_label = 'Тренера не обарано'
