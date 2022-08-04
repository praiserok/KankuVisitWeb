from belt.models import Belt
from .forms import BeltAddForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from additional.add import CustomSuccessMessageMixin
from django.contrib import messages


class BeltEditView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Belt
    template_name = 'belt/visit/beltedit.html'
    form_class = BeltAddForm
    success_url = reverse_lazy('belt')
    success_msg = 'Дані ' + Belt._meta.verbose_name + 'у обновлено успішно!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activeBelt'] = 'active'
        return context

#  Функція що заюороняє редагувати якщо ти не створював

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     if self.request.user != kwargs['instance'].coach:
    #         return self.handle_no_permission()
    #     return kwargs


class BeltView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView, ListView):
    model = Belt
    form_class = BeltAddForm
    template_name = 'belt/visit/belt.html'
    success_msg = Belt._meta.verbose_name + ' добавлено успішно!'
    success_url = reverse_lazy('belt')
    context_object_name = 'data'
    paginate_by = 25  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = Belt._meta.fields
        context['table'] = Belt._meta.app_label
        context['activeBelt'] = 'active'
        context['title'] = Belt._meta.verbose_name
        context['titles'] = Belt._meta.verbose_name_plural
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # фільтр що відображати

    # def get_queryset(self):
    #     return Sportsman.objects.filter(coach=self.request.user)


class beltDeleteView(LoginRequiredMixin, CustomSuccessMessageMixin, DeleteView):
    model = Belt
    template_name = 'belt/visit/belt.html'
    success_url = reverse_lazy('belt')
    success_msg = Belt._meta.verbose_name + ' видалено!'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

#  Функція що забороняє видалити якщо ти не створював

    # def form_valid(self, form):
    #     self.object = self.get_object()

    #     if self.request.user != self.object.coach:
    #         return self.handle_no_permission()
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #     return HttpResponseRedirect(success_url)
