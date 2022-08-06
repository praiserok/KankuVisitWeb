from sportsman.forms import SportsmanAddForm
from sportsman.models import Sportsman
from django.http import HttpResponseRedirect
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from additional.add import CustomSuccessMessageMixin
from django.contrib import messages
from django.db.models import Q


class SportsmanEditView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Sportsman
    template_name = 'sportsman/visit/sportsmanedit.html'
    form_class = SportsmanAddForm
    success_msg = 'Дані ' + Sportsman._meta.verbose_name + 'а обновлено успішно!'
    success_url = reverse_lazy('sportsman')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activeSportsman'] = 'active'
        return context

#  Функція що заюороняє редагувати якщо ти не створював

    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()
        kwargs.update({'user_id': self.request.user.id})
        if kwargs['instance'].coach == None:
            return kwargs
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

        search = self.request.GET.get('search')
        query = self.request.GET.get('query')
        if search == 'name' and query:
            sportsman = Sportsman.objects.filter(
                Q(first_name__startswith=query, coach_id=self.request.user.id) | Q(last_name__startswith=query, coach_id=self.request.user.id))
            context['data'] = sportsman
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.coach = self.request.user
        self.object.save()
        return super().form_valid(form)

    # фільтр що відображати

    def get_queryset(self):
        return Sportsman.objects.filter(Q(coach=self.request.user) | Q(coach_id=None))

    # Передаємо user_id з request в форму

    def get_form_kwargs(self):
        kwargs = super(SportsmanView, self).get_form_kwargs()
        kwargs.update({'user_id': self.request.user.id})
        return kwargs


class sportsmanDeleteView(LoginRequiredMixin, CustomSuccessMessageMixin, DeleteView):
    model = Sportsman
    template_name = 'sportsman/visit/sportsman.html'
    success_url = reverse_lazy('sportsman')
    success_msg = Sportsman._meta.verbose_name + 'а - видалено!'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

#  Функція що забороняє видалити якщо ти не створював

    def form_valid(self, form):
        self.object = self.get_object()

        if self.request.user != self.object.coach:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
