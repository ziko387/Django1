from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task,Taskers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from.forms import CustomUserCreationForm




# Create your views here
""""authentication views functionalities"""
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = CustomUserCreationForm()
    return render(request, 'cooler/register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('task_list')

    else:
        form = AuthenticationForm()
    return render(request,'cooler/login.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')



"""these functionalities take care of CRUD :-)"""
@login_required(login_url='login')
def task_list(request):
    """this functions collects task items """
    # [] empty list is a default if task are empty
    #tasks=request.session.get('tasks',[])
    #fenching task from db for logged in user
    #tasks = Task.objects.all()
    tasks=Task.objects.filter(user=request.user)
    taskers = Task.objects.all()
    ##the render function returning a .html template
    return render(request,'cooler/task_list.html',
                  {'tasks':tasks,"tasker":taskers})
@login_required(login_url='login')
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('task')
        tasker_id = request.POST.get('tasker')

        #save to db
        if title:
            # validating the id entered
           tasker = Taskers.objects.get(id=tasker_id) if tasker_id else None
           Task.objects.create(title=title,tasker=tasker,user=request.user)
        messages.success(request, 'Tasker and task added successfully')
    else:
        messages.error(request, 'please enter a valid tasker')
    return redirect('task_list')

@login_required(login_url='login')
def add_tasker(request):
    if request.method == "POST":
        username = request.POST.get('user_tasker')
        email = request.POST.get('user_email')

        if username:
            tasker = Taskers.objects.create(username=username,email=email)
            return redirect('task_list')

def delete_task(request,task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('task_list')


def mark_complete(request,task_id):
    tasks = Task.objects.get(id=task_id)
    Task.completed = True
    Task.save()
    return redirect('task_list')



