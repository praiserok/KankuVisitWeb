from django.shortcuts import render, redirect
from school.models import School
from .forms import SchoolAddForm


def school(request):
    error = ''
    if request.method == 'POST':
        form = SchoolAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school')
        else:
            error = 'Введено не коректні дані!'

    school = School.objects.all()
    form = SchoolAddForm()

    context = {
        'forms': form,
        'title': School._meta.verbose_name,
        'titles': School._meta.verbose_name_plural,
        'data': school,
        'error': error,
        'activeSchool': 'active'
    }

    return render(request, 'main/visit/pages/school.html', context)


def schoolEdit(request, school_id):
    return 10


def schoolDelete(request, school_id):

    school = School.objects.get(pk=school_id)
    school.delete()

    return redirect(request.META['HTTP_REFERER'])
