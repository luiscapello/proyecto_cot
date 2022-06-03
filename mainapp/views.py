import email
from unicodedata import name
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import redirect, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
#from django.shortcuts import render
from mainapp.forms import RegisterForm
from mainapp.models import Cotizacion
from django.db import models


# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })


def cotizacion(request):

    cotizacion1 = Cotizacion(

            #date = '25/05/2022',
            typeCo = 'nueva',
            folio = '2515',
            customerCode = '5416',
            customers = 'capello',
            press = '1',
            request = '1',
            quotation = '1',
            codeUyeda = '1',
            description	= 'wsd',
            variant	= '4',
            development	= '145',
            axis = '1',
            output = '14',
            suaje = 'refe',
            substrate = 'erfe',
            adhesive = 'jjo',
            backup = 'backup',
            inkFront = '1',
            inkAdhesive	= '1',
            inkBackup = '2',
            typeInk	= 'typeInk',
            finished = 'finished',
            specialty = 'specialty',
            delivery = 'delivery',
            place = 'place',
            letterColor	= 'letterColor',
            typeDelivery = 'typeDelivery',
            speed = '15',
            test = 'test',
            packaging = 'packaging',
            prodpackaging = 'prodpackaging',
            annual = '2055',
            price = '215',
            ink1 = '1',
            ink2 = '2',
            ink3 = '3',
            ink4 = '4',
            ink5 = '5',
            ink6 = '6',
            ink7 = '7',
            ink8 = '8',
            ink9 = '9',
            ink10 = '10',
            note = 'note',
    )
    cotizacion1.save()

    return HttpResponse(f"Cotizacion creada: <strong>{cotizacion1.folio}</strong> - {cotizacion1.customers}")



def save_cotizacion(request):

    if request.method == 'GET':

        typeCo = request.GET['typeCo']
        folio = request.GET['folio']
        customerCode = request.GET['customerCode']
        customers = request.GET['customers']
        press =	request.GET['press']
        request	= request.GET['request']
        quotation =	request.GET['quotation']
        codeUyeda = request.GET['codeUyeda']
        description	= request.GET['description']
        variant	= request.GET['variant']
        development	= request.GET['development']
        axis = request.GET['axis']
        output = request.GET['output']
        suaje =	request.GET['suaje']
        substrate = request.GET['substrate']
        adhesive = request.GET['adhesive']
        backup = request.GET['backup']
        inkFront = request.GET['inkFront']
        inkAdhesive	= request.GET['inkAdhesive']
        inkBackup = request.GET['inkBackup']
        typeInk	= request.GET['typeInk']
        finished = request.GET['finished']
        specialty =	request.GET['specialty']
        delivery = request.GET['delivery']
        place =	request.GET['place']
        letterColor	= request.GET['letterColor']
        typeDelivery = request.GET['typeDelivery']
        speed =	request.GET['speed']
        test = request.GET['test']
        packaging =	request.GET['packaging']
        prodpackaging =	request.GET['prodpackaging']
        annual = request.GET['annual']
        price =	request.GET['price']
        ink1 = request.GET['ink1']
        ink2 = request.GET['ink2']
        ink3 = request.GET['ink3']
        ink4 = request.GET['ink4']
        ink5 = request.GET['ink5']
        ink6 = request.GET['ink6']
        ink7 = request.GET['ink7']
        ink8 = request.GET['ink8']
        ink9 = request.GET['ink9']
        ink10 = request.GET['ink10']
        note = request.GET['note']

        cotizacion1 = Cotizacion(
            typeCo = typeCo,
            folio = folio,
            customerCode = customerCode,
            customers = customers,
            press = press,
            request = request,
            quotation = quotation,
            codeUyeda = codeUyeda,
            description	= description,
            variant	= variant,
            development	= development,
            axis = axis,
            output = output,
            suaje = suaje,
            substrate = substrate,
            adhesive = adhesive,
            backup = backup,
            inkFront = inkFront,
            inkAdhesive	= inkAdhesive,
            inkBackup = inkBackup,
            typeInk	= typeInk,
            finished = finished,
            specialty = specialty,
            delivery = delivery,
            place = place,
            letterColor	= letterColor,
            typeDelivery = typeDelivery,
            speed = speed,
            test = test,
            packaging = packaging,
            prodpackaging = prodpackaging,
            annual = annual,
            price = price,
            ink1 = ink1,
            ink2 = ink2,
            ink3 = ink3,
            ink4 = ink4,
            ink5 = ink5,
            ink6 = ink6,
            ink7 = ink7,
            ink8 = ink8,
            ink9 = ink9,
            ink10 = ink10,
            note = note,
        )
        cotizacion1.save()

        return HttpResponse(f"Cotizacion creada: <strong>{cotizacion1.folio}</strong> - {cotizacion1.customers}")
    
    else:
        return HttpResponse("<h2> Nose ha podido guardar la cotización </h2>")

    


def Formulario(request):

    return render(request, 'mainapp/form.html', {
        'title': 'Solicitud de Cotización'
    })



def cotizaciones(request):

    cotizacion = Cotizacion.objects.raw("SELECT * FROM mainapp_cotizacion ")

    return render(request, 'mainapp/cotizaciones.html', {
        'cotizaciónes': cotizaciones
        
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