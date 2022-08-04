from datetime import date
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from flask import request
from .forms import *
from coach.forms import CoachAddForm
from .models import *
from slugify import slugify
from django.views.generic import CreateView
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'titles': 'Головна сторінка'
    }
    return render(request, 'main/index.html', context)


@login_required
def indexVisit(request):
    context = {
        'titles': 'Тренерська'
    }
    return render(request, 'main/visit/index.html', context)


def about(request):
    return render(request, 'main/about.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'title': 'Реєстрація'
    }

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('visit')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    # success_url = reverse_lazy('login')
    extra_context = {
        'title': 'Вхід для тренера'
    }

    def get_success_url(self):
        return reverse_lazy('visit')


def logout_user(request):
    logout(request)
    return redirect('login')
