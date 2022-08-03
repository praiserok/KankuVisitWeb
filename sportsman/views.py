import re
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import coach
from sportsman.forms import SportsmanAddForm
from sportsman.models import Sportsman, Coach
from django.views.generic import DetailView, ListView, UpdateView, FormView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?slug=%s' % (self.success_url, self.object.slug)


class SportsmanEditView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Sportsman
    template_name = 'sportsman/visit/sportsmanedit.html'
    form_class = SportsmanAddForm
    success_msg = 'Дані ' + Sportsman._meta.verbose_name + 'а обновлено успішно!'
    success_url = reverse_lazy('sportsman')
    extra_context = {
        'activeSportsman': 'active'
    }
#  Функція що заюороняє редагувати якщо ти не створював

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].coach:
            return self.handle_no_permission()
        return kwargs


class SportsmanView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView, ListView):
    model = Sportsman
    form_class = SportsmanAddForm
    template_name = 'sportsman/visit/sportsman.html'
    success_msg = Sportsman._meta.verbose_name + 'а - добавлено успішно!'
    success_url = reverse_lazy('sportsman')
    context_object_name = 'data'
    paginate_by = 25  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = Sportsman._meta.fields
        context['table'] = Sportsman._meta.app_label
        context['activeSportsman'] = 'active'
        context['title'] = Sportsman._meta.verbose_name
        context['titles'] = Sportsman._meta.verbose_name_plural
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.coach = self.request.user
        self.object.save()
        return super().form_valid(form)

    # фільтр що відображати

    # def get_queryset(self):
    #     return Sportsman.objects.filter(coach=self.request.user)


class sportsmanDeleteView(LoginRequiredMixin, DeleteView):
    model = Sportsman
    template_name = 'sportsman/visit/sportsman.html'
    success_url = reverse_lazy('sportsman')
    success_msg = Sportsman._meta.verbose_name + 'а - видалено!'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

#  Функція що заюороняє видалити якщо ти не створював

    def form_valid(self, form):
        self.object = self.get_object()

        if self.request.user != self.object.coach:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
