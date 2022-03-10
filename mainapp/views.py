import email
from django.shortcuts import redirect, render, redirect
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
#from django.shortcuts import render_to_response



# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

def formulario(request):

    return render(request, 'mainapp/form.html', {
        'title': 'Solicitud de Cotización'
    })

def cotizaciones(request):

    return render(request, 'mainapp/cotizaciones.html', {
        'title': 'Solicitud de Cotización'
    })

def register_page(request):

    if request.user.is_autenticated:
        return redirect('inicio')
    else:
        register_form = RegisterForm()

        if request.method == "POST":
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()

                return redirect('inicio')

        return render(request, 'users/register.html',{
            'title': 'Registro',
            'register_form': register_form
        })

def login_page(request):
    

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicio')

        else:
            messages.warning(request, 'El usuario o la Contraseña no son correctos!!')


    return render(request, 'users/login.html', {
        'title': 'Identificate'
    })

def logout_user(request):
    logout(request)
    return redirect('login')