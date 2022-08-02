from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

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

    class Meta:
        model = User
        fields = ('username', 'email', 'password1',
                  'password2', 'first_name', 'last_name')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ваш логін'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
