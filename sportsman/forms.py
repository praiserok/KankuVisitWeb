from dodjo.models import Group
from .models import Sportsman
from coach.models import Coach
from django.forms import (ModelForm, TextInput, EmailInput,
                          DateInput, NumberInput, Select)


class SportsmanAddForm(ModelForm):

    class Meta:
        model = Sportsman
        # fields = ['first_name', 'last_name', 'surname', 'dateBirth',
        #           'belts', 'group', 'is_active']

        exclude = ['slug']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть ім\'я'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть прізвище'}),
            'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть побатькові', }),
            'dateBirth': DateInput(attrs={'type': 'date', 'class': 'form-control', }),
            'belts': Select(attrs={'class': 'form-select '}),
            'group': Select(attrs={'class': 'form-select '}),
            'coach': Select(attrs={'class': 'form-select '})
        }

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super().__init__(*args, **kwargs)
        self.fields['belts'].empty_label = 'Пояс не обарано'
        self.fields['coach'].empty_label = None
        self.fields['coach'].queryset = Coach.objects.filter(id=user_id)
        if len(Group.objects.filter(coach_id=user_id)) < 1:
            self.fields['group'].empty_label = 'Не створено груп!'
        else:
            self.fields['group'].empty_label = 'Групу не обарано'
        self.fields['group'].queryset = Group.objects.filter(
            coach_id=user_id)
