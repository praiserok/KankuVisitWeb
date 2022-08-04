from .models import Sportsman
from django.forms import (ModelForm, TextInput, EmailInput,
                          DateInput, NumberInput, Select)


class SportsmanAddForm(ModelForm):

    class Meta:
        model = Sportsman
        # fields = ['first_name', 'last_name', 'surname', 'dateBirth',
        #           'belts', 'group', 'is_active']

        exclude = ['slug', 'coach']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть ім\'я'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть прізвище'}),
            'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть побатькові', }),
            'dateBirth': DateInput(attrs={'type': 'date', 'class': 'form-control', }),
            'belts': Select(attrs={'class': 'form-select '}),
            'group': Select(attrs={'class': 'form-select '}),
            # 'coach': Select(attrs={'class': 'form-select '})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['belts'].empty_label = 'Пояс не обарано'
        self.fields['group'].empty_label = 'Групу не обарано'
        # self.fields['coach'].empty_label = 'Тренер не обарано'
