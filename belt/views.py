from django.shortcuts import render, redirect
from belt.models import Belt
from .forms import BeltAddForm


def belt(request):

    error = ''
    if request.method == 'POST':
        form = BeltAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school')
        else:
            error = 'Введено не коректні дані!'
    belt = Belt.objects.all()
    form = BeltAddForm()

    context = {
        'forms': form,
        'title': Belt._meta.verbose_name,
        'titles': Belt._meta.verbose_name_plural,
        'data': belt,
        'error': error,
        'activeBelt': 'active'
    }

    return render(request, 'main/visit/pages/belt.html', context)
