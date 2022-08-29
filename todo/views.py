from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

def home(request):
    todos = Todo.objects.all()
    contex = {
        "todos" : todos
    }
    return render(request, "todo/home.html", contex)

def todo_create(request):
    form = TodoForm()
    if request.method = "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    contex = {
        "form" : form
    }

    return render(request, "todo/todo_add.html", contex)