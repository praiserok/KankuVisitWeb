from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {
        'title': 'Головна сторінка сайта',
        'tasks': tasks
    })


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма була не вірною!'

    form = TaskForm()
    context = {'form': form, 'title': 'Створити Task', 'error': error}
    return render(request, 'main/create.html', context)