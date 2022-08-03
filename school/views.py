from math import fabs
from pyexpat import model
from django.shortcuts import render, redirect
from school.models import School
from .forms import SchoolAddForm
from django.views.generic import DetailView, ListView, UpdateView, FormView
from django.urls import reverse_lazy


class SchoolEditView(UpdateView):
    model = School
    template_name = 'school/visit/schooledit.html'
    form_class = SchoolAddForm
    extra_context = {
        'activeSchool': 'active'
    }


class SchoolView(ListView, FormView):
    model = School
    form_class = SchoolAddForm
    template_name = 'school/visit/school.html'
    success_url = reverse_lazy('school')
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
        form.save()
        return super().form_valid(form)


def schoolDelete(request, slug):

    item = School.objects.get(slug=slug)
    item.delete()

    return redirect(request.META['HTTP_REFERER'])
