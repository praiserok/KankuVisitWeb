from django.http import HttpResponseRedirect
from django.shortcuts import render
from flask import request
from dodjo.models import School, Group, Timetable
from dodjo.forms import SchoolAddForm, GroupAddForm, TimetableAddForm
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from additional.add import CustomSuccessMessageMixin
from django.contrib import messages
from django.db.models import Q


####### ШКОЛА #######


class SchoolView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView, ListView):
    model = School
    form_class = SchoolAddForm
    template_name = 'school/visit/school.html'
    success_url = reverse_lazy('school')
    success_msg = School._meta.verbose_name + ' добавлена успішно!'
    context_object_name = 'data'
    paginate_by = 25  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = School._meta.fields
        context['table'] = School._meta.app_label
        context['activeSchool'] = 'active'
        context['title'] = School._meta.verbose_name
        context['titles'] = School._meta.verbose_name_plural
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.coach = self.request.user
        self.object.save()
        return super().form_valid(form)

    # фільтр що відображати

    def get_queryset(self):
        return School.objects.filter(Q(coach=self.request.user) | Q(coach_id=None))

# Передаємо user_id з request в форму

    def get_form_kwargs(self):
        kwargs = super(SchoolView, self).get_form_kwargs()
        kwargs.update({'user_id': self.request.user.id})
        return kwargs


class SchoolEditView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = School
    template_name = 'school/visit/schooledit.html'
    form_class = SchoolAddForm
    success_msg = 'Дані ' + School._meta.verbose_name + ' обновлена успішно!'
    success_url = reverse_lazy('school')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activeSchool'] = 'active'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user_id': self.request.user.id})
        if kwargs['instance'].coach == None:
            return kwargs
        if self.request.user != kwargs['instance'].coach:
            return self.handle_no_permission()
        return kwargs


class SchoolDeleteView(LoginRequiredMixin, CustomSuccessMessageMixin, DeleteView):
    model = School
    template_name = 'school/visit/school.html'
    success_url = reverse_lazy('school')
    success_msg = School._meta.verbose_name + ' видалена!'

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

####### ШКОЛА #######
####### ГРУПИ #######


class GroupView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView, ListView):
    model = Group
    form_class = GroupAddForm
    template_name = 'group/visit/group.html'
    success_url = reverse_lazy('group')
    success_msg = Group._meta.verbose_name + ' добавлена успішно!'
    context_object_name = 'data'
    paginate_by = 25  # if pagination is desired
#   form = GroupAddForm(user_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = Group._meta.fields
        context['table'] = Group._meta.app_label
        context['activeGroup'] = 'active'
        context['title'] = Group._meta.verbose_name
        context['titles'] = Group._meta.verbose_name_plural
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.coach = self.request.user
        self.object.save()
        return super().form_valid(form)

    # фільтр що відображати

    def get_queryset(self):
        return Group.objects.filter(coach=self.request.user)

# Передаємо user_id з request в форму
    def get_form_kwargs(self):
        kwargs = super(GroupView, self).get_form_kwargs()
        kwargs.update({'user_id': self.request.user.id})
        return kwargs


class GroupEditView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Group
    template_name = 'group/visit/groupedit.html'
    form_class = GroupAddForm
    success_url = reverse_lazy('group')
    success_msg = Group._meta.verbose_name + ' обновлена успішно!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activeGroup'] = 'active'
        return context

    def get_form_kwargs(self):
        kwargs = super(GroupEditView, self).get_form_kwargs()
        if self.request.user != kwargs['instance'].coach:
            return self.handle_no_permission()
        kwargs.update({'user_id': self.request.user.id})
        return kwargs


class GroupDeleteView(LoginRequiredMixin, CustomSuccessMessageMixin, DeleteView):
    model = Group
    template_name = 'group/visit/group.html'
    success_url = reverse_lazy('group')
    success_msg = Group._meta.verbose_name + ' видалена!'

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

####### ГРУПИ #######
####### ГРАФІК #######


class TimetableView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView, ListView):
    model = Timetable
    form_class = TimetableAddForm
    template_name = 'timetable/visit/timetable.html'
    success_url = reverse_lazy('timetable')
    success_msg = Timetable._meta.verbose_name + ' добавлено успішно!'
    context_object_name = 'data'
    paginate_by = 25  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = Timetable._meta.fields
        context['table'] = Timetable._meta.app_label
        context['activeTimetable'] = 'active'
        context['title'] = Timetable._meta.verbose_name
        context['titles'] = Timetable._meta.verbose_name_plural
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # фільтр що відображати

    def get_queryset(self):
        return Timetable.objects.filter(group__school__coach=self.request.user)

    # Передаємо user_id з request в форму
    def get_form_kwargs(self):
        kwargs = super(TimetableView, self).get_form_kwargs()
        kwargs.update({'user_id': self.request.user.id})
        return kwargs


class TimetableEditView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Timetable
    template_name = 'timetable/visit/timetableedit.html'
    form_class = TimetableAddForm
    success_url = reverse_lazy('timetable')
    success_msg = Timetable._meta.verbose_name + ' обновлена успішно!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activeTimetable'] = 'active'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user_id': self.request.user.id})
        # if self.request.user != kwargs['instance'].group:
        #     return self.handle_no_permission()
        return kwargs


class TimetableDeleteView(LoginRequiredMixin, CustomSuccessMessageMixin, DeleteView):
    model = Timetable
    template_name = 'timetable/visit/timetable.html'
    success_url = reverse_lazy('timetable')
    success_msg = Timetable._meta.verbose_name + ' видалена!'

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
