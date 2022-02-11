from math import fabs
from pyexpat import model
from django.shortcuts import render, redirect
from school.models import School
from .forms import SchoolAddForm
from django.views.generic import DetailView, ListView, UpdateView


class SchoolEditView(UpdateView):
    model = School
    template_name = 'school/visit/schooledit.html'
    form_class = SchoolAddForm
    extra_context = {
        'activeSchool': 'active'
    }


def school(request):
    error = ''
    model = School.objects.all().order_by('coach')
    fields = School._meta.fields
    table = School._meta.app_label

    if request.method == 'POST':
        form = SchoolAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('school')
        else:
            error = 'Введено не коректні дані!'
    else:
        form = SchoolAddForm()

    # fields = School._meta.get_field('name')
    # print(School._meta.app_label) Таблиця назва
    # print(School._meta.label) Таблиця назва
    # values = School.objects.values()

    context = {
        'forms': form,
        'title': School._meta.verbose_name,
        'titles': School._meta.verbose_name_plural,
        'data': model,
        'fields': fields,
        'table': table,
        'error': error,
        'activeSchool': 'active'
    }

    return render(request, 'school/visit/school.html', context)


def schoolDelete(request, slug):

    item = School.objects.get(slug=slug)
    item.delete()

    return redirect(request.META['HTTP_REFERER'])
