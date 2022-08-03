from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from coach.models import Coach

# Форма для реєстрації користувачів


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Логін', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Придумайте собі логін'}))
    email = forms.EmailField(
        label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введіть свій Email', 'type': 'email'}))
    password1 = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    password2 = forms.CharField(
        label='Повторіть пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    first_name = forms.CharField(label="Ваше ім'я", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Ім'я"}))
    last_name = forms.CharField(label="Ваша фамілія", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Фамілія"}))
    surname = forms.CharField(label="Побатькові", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Побатькові"}))
    dataBirth = forms.DateField(label="Дата народження", widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}))
    telephone = forms.IntegerField(label="Номер телефону", widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Введіть номер телефону: 380681111111'}))
    # telephone2 = forms.IntegerField(label="Номер телефону 2", widget=forms.NumberInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Введіть номер телефону 2'}))

    class Meta:
        model = Coach
        fields = ('username', 'email', 'password1',
                  'password2', 'first_name', 'last_name', 'surname', 'dataBirth', 'telephone')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ваш логін'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
