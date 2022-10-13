import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from todolist.models import Task
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description'
        ]


@login_required(login_url='/todolist/login/')
def show_json(request):
    tasks = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", tasks), content_type="application/json")


# @login_required(login_url='login/')
# def ajax_show_todolist(request):
#     context = {
#         'user': request.user
#     }
#     return render(request, 'todolist_ajax.html', context)


@login_required(login_url='/todolist/login')
@csrf_exempt
def delete_task_ajax(request, id):
    if request.method == "DELETE":
        task = get_object_or_404(Task, id = id)
        task.delete()
    return HttpResponse(status=202)

@login_required(login_url='/todolist/login/')
def create_task_json(request):
    if request.method == "POST":
        task = Task(
            title = request.POST["title"],
            desc = request.POST["desc"],
            user = request.user,
        )
        task.save()
        return HttpResponse(
            serializers.serialize("json", [task]),
            content_type="application/json",
        )
    return HttpResponse("Invalid method", status_code=405)



@login_required(login_url='/todolist/login/')
@csrf_exempt
def create_task_ajax(request):
    task = TaskForm()

    if request.method == "POST":
        task = TaskForm(request.POST)
        if task.is_valid():
            title = task.cleaned_data['title']
            description = task.cleaned_data['description']

            new_task = Task.objects.create(title=title, description=description, user=request.user, date=datetime.date.today())
            new_task.save()

            result = {
                'fields':{
                    'title':new_task.title,
                    'description':new_task.description,
                    'is_finished':new_task.is_finished,
                    'date':new_task.release_date,
                },
                'pk':new_task.pk
            }

            return JsonResponse(result)

@login_required(login_url='/todolist/login')
@csrf_exempt
def update_task_ajax(request, id):
    if request.method == "PATCH":
        task = get_object_or_404(Task, id = id)
        task.is_finished = not task.is_finished
        task.save()
    
    result = {
        'fields':{
            'title': task.title,
            'description': task.description,
            'is_finished': task.is_finished,
            'date': task.release_date,
            },
            'pk': task.pk
        }
        
    return JsonResponse(result)

@login_required(login_url='/todolist/login/')
def update_task(request, id):
    task_list = Task.objects.filter(id=id)
    task = task_list[0]
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    task_list = Task.objects.filter(id=id)
    task = task_list[0]
    task.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    my_tasks = Task.objects.filter(user=request.user)
    context = {
        'my_tasks': my_tasks,
        'username': request.user.username,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task (request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            return redirect('todolist:show_todolist')
        else:
            form = user()
    
    context = {'form':form}
    return render(request, 'create-task.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("todolist:login_user"))
    response.delete_cookie('last_login')
    return response