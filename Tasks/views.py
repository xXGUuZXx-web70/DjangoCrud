from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task

# Create your views here.
def home(request):
    return render(request, 
                  "home.html",
                  {"form":TaskForm})

def tasks(request):
    tasks = Task.objects.filter(user=request.user,
                                 datecompleted__isnull=True)
    return render(request, "tasks.html",
                  {"tasks":tasks})

def seleccionar(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        return redirect('tasks')
    return render(request, 'seleccionar.html', {'task': task})

def create_task(request):
    if request.method == "GET":
        return render(request, 
                "create_task.html",
                   {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("tasks")
        except ValueError:
            return render(request, 
                    "create_task.html",
                   {"form": TaskForm(),
                    "error":"Por favor ingrese datos validos"})
        
def editar_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)

    if request.method == "GET":
        form = TaskForm(instance=task)
        return render(request, "editar.html", {"form": form})
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("tasks")
            else:
                return render(request, "editar.html", {"form": form, "error": "Datos inválidos"})
        except ValueError:
            return render(request, "editar.html", {"form": form, "error": "Error al editar la tarea"})

def eliminar(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        task.delete()
        return redirect("tasks")

    return render(request, "eliminar.html", {"task": task})



def signout(request):
    logout(request)
    return redirect("home")

def signin(request):
    if request.method == "GET":
        return render(request, 
                  "signin.html",
                  {"form":AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,
                          'signin.html',
                          {"form": AuthenticationForm(),
                           "error":"Usuario o contraseña incorrecta"})
        else:
            login(request, user)
            return redirect("tasks")

def signup(request):
    if request.method == "GET":
        return render(request, 
                  "signup.html",
                  {"form":UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("tasks")

            except IntegrityError:
                return render(request,
                              'signup.html',
                              {"form": UserCreationForm(),
                               "error":"Error al crear el usuario"})
                
        else:
                 return render(request,
                              'signup.html',
                              {"form": UserCreationForm(),
                               "error":"Error, Las contraseñas no coinciden"})