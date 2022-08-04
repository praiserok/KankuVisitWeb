from .models import Belt
from django.forms import (ModelForm, TextInput, NumberInput, URLInput)


class BeltAddForm(ModelForm):

    class Meta:
        model = Belt
        # fields = '__all__'
        exclude = ['slug', 'img']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть назву'}),
            'fullname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть повну назву'}),
            'number': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введіть номер поясу'}),
            # 'img': URLInput(attrs={'type': 'file', 'class': 'form-control', }),
        }
