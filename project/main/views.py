from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .models import Task, Objavlenie, Employ
from .form import TaskForm, ObjavForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html',{'title': 'Главная сайта',  'tasks': tasks})


def about(request):
    all_objav = Objavlenie.objects.all()
    return render(request, 'main/about.html',{'title': 'Обьявления',  'all_objav': all_objav})


def employ(request):
    employes = Employ.objects.all()
    return render(request, 'main/employ.html', {'title': 'Сотрудники',  'employes': employes})


def login(request):
    #потом поменять на другую бд
    tasks = Task.objects.all()
    return render(request, 'main/login.html', {'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не соответствует'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)



def create_objav(request):
    error = ''
    if request.method == 'POST':
        form = ObjavForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            error = 'Форма не соответствует'

    form = ObjavForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_objav.html', context)


