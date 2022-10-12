from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task

# Menampilkan halaman utama dengan wajib login
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    cuuser = request.user
    dataTask = Task.objects.all().filter(user = cuuser)
    context = {
        'user': cuuser,
        'task': dataTask,
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_json(request):
    cuuser = request.user
    dataTask = Task.objects.all().filter(user = cuuser)
    return HttpResponse(serializers.serialize("json", dataTask), content_type="application/json")

# Halaman register akun
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# Halaman login akun
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# Keluar dari akun
def logout_user(request):
    logout(request)
    return redirect('todolist:login')

# Mmebuat task baru
@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        task = Task()
        task.user = request.user
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('todolist:show_todolist')

    return render(request, 'createtask.html')

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == 'POST':
        task = Task()
        task.user = request.user
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('todolist:show_todolist')

# Hapus task
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('todolist:show_todolist')

# Update task menjadi sudah selesai atau belum
def update_task(request, id):
    task = Task.objects.get(id=id)
    if (task.is_finished == True):
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return redirect('todolist:show_todolist')