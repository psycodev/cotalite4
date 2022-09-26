from ast import Return
from pyexpat.errors import messages
from urllib.request import Request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.views.generic import ListView
from django.contrib import messages

def register(request):
    if request.method =='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado con exito')
            return redirect ('http://127.0.0.1:8000/')
    else:
        form=RegistrationForm()
    context={ 'form':form}
    return render(request, 'registrar.html', context)

def listarUsu(request):
    users=User.objects.all()
    data={
            'users': users
        }
    print(users)
    return render(request, "listar.html", data)

def listusubyid(request, id):
    users = User.objects.filter(id=id)
    contexto = {'users': users}
    return render(request, "listar.html",contexto)

def updateusu(request, id):
    users = User.objects.get(id=id)
    if request.method == 'GET':
        form=RegistrationForm(instance=users)
    else:
        form=RegistrationForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/usuarios/succes")
    return render(request, 'registrar.html', {'form':form}) 

def deleteUser(request, id):
    users = User.objects.get(id=id)
    if request.method == 'POST':
        users.delete()
        return redirect('users:empleados')
    return render(request, 'delete.html', {'users': users}) 


    
    
    