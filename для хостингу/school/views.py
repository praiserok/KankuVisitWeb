# from django.http import HttpResponseRedirect
# from school.models import School
# from .forms import SchoolAddForm
# from django.views.generic import ListView, UpdateView, CreateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
# from additional.add import CustomSuccessMessageMixin
# from django.contrib import messages


# class SchoolEditView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
#     model = School
#     template_name = 'school/visit/schooledit.html'
#     form_class = SchoolAddForm
#     success_msg = 'Дані ' + School._meta.verbose_name + ' обновлена успішно!'
#     success_url = reverse_lazy('school')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['activeSchool'] = 'active'
#         return context

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         if self.request.user != kwargs['instance'].coach:
#             return self.handle_no_permission()
#         return kwargs


# class SchoolView(LoginRequiredMixin, CustomSuccessMessageMixin, CreateView, ListView):
#     model = School
#     form_class = SchoolAddForm
#     template_name = 'school/visit/school.html'
#     success_url = reverse_lazy('school')
#     success_msg = School._meta.verbose_name + ' добавлена успішно!'
#     context_object_name = 'data'
#     paginate_by = 25  # if pagination is desired

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['fields'] = School._meta.fields
#         context['table'] = School._meta.app_label
#         context['activeSchool'] = 'active'
#         context['title'] = School._meta.verbose_name
#         context['titles'] = School._meta.verbose_name_plural
#         return context

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.coach = self.request.user
#         self.object.save()
#         return super().form_valid(form)

#     # фільтр що відображати

#     # def get_queryset(self):
#     #     return Sportsman.objects.filter(coach=self.request.user)


# class schoolDeleteView(LoginRequiredMixin, CustomSuccessMessageMixin, DeleteView):
#     model = School
#     template_name = 'school/visit/school.html'
#     success_url = reverse_lazy('school')
#     success_msg = School._meta.verbose_name + ' видалена!'

#     def post(self, request, *args, **kwargs):
#         messages.success(self.request, self.success_msg)
#         return super().post(request)

# #  Функція що забороняє видалити якщо ти не створював

#     def form_valid(self, form):
#         self.object = self.get_object()
#         if self.request.user != self.object.coach:
#             return self.handle_no_permission()
#         success_url = self.get_success_url()
#         self.object.delete()
#         return HttpResponseRedirect(success_url)
