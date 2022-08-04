from django.http import HttpResponseRedirect
from .forms import CoachAddForm
from .models import Coach
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from additional.add import CustomSuccessMessageMixin


class CoachEditView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Coach
    template_name = 'coach/visit/coachedit.html'
    form_class = CoachAddForm
    success_msg = 'Дані ' + Coach._meta.verbose_name + 'а обновлено успішно!'
    success_url = reverse_lazy('coach')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activeCoach'] = 'active'
        return context
    #  Функція що заюороняє редагувати якщо ти не створював

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.id != kwargs['instance'].id:
            return self.handle_no_permission()
        return kwargs


class CoachView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView, ListView):
    model = Coach
    form_class = CoachAddForm
    template_name = 'coach/visit/coach.html'
    success_url = reverse_lazy('coach')
    success_msg = Coach._meta.verbose_name + 'а - добавлено успішно!'
    context_object_name = 'data'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = Coach._meta.fields
        context['table'] = Coach._meta.app_label
        context['activeCoach'] = 'active'
        context['title'] = Coach._meta.verbose_name
        context['titles'] = Coach._meta.verbose_name_plural
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    # фільтр що відображати

    # def get_queryset(self):
    #     return Coach.objects.filter(id=self.request.user.id)


class coachDeleteView(LoginRequiredMixin, DeleteView):
    model = Coach
    template_name = 'coach/visit/Coach.html'
    success_url = reverse_lazy('coach')
    success_msg = Coach._meta.verbose_name + 'а - видалено!'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

#  Функція що забороняє видалити якщо ти не створював

    def form_valid(self, form):
        self.object = self.get_object()

        if self.request.user.id != self.object.id:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
