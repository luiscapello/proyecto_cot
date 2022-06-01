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




# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

def Formulario(request):

    return render(request, 'mainapp/form.html', {
        'title': 'Solicitud de Cotización'
    })

def crear_cotizacion(request):

    cotizacion = Cotizacion(

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
    cotizacion.save()

    return HttpResponse(f"Cotizacion creada: <strong>{cotizacion.folio}</strong> - {cotizacion.customers}")


# def save_form(request):

#     if request.method == 'POST':

#         date = request.POST['date']
#         typeCo = request.POST['typeCo']
#         folio = request.POST['folio']
#         customerCode = request.POST['customerCode']
#         customers = request.POST['customers']
#         press =	request.POST['press']
#         request	= request.POST['request']
#         quotation =	request.POST['quotation']
#         codeUyeda = request.POST['codeUyeda']
#         description	= request.POST['description']
#         variant	= request.POST['variant']
#         development	= request.POST['development']
#         axis = request.POST['axis']
#         output = request.POST['output']
#         suaje =	request.POST['suaje']
#         substrate = request.POST['substrate']
#         adhesive = request.POST['adhesive']
#         backup = request.POST['backup']
#         inkFront = request.POST['inkFront']
#         inkAdhesive	= request.POST['inkAdhesive']
#         inkBackup = request.POST['inkBackup']
#         typeInk	= request.POST['typeInk']
#         finished = request.POST['finished']
#         specialty =	request.POST['specialty']
#         delivery = request.POST['delivery']
#         place =	request.POST['place']
#         letterColor	= request.POST['letterColor']
#         typeDelivery = request.POST['typeDelivery']
#         speed =	request.POST['speed']
#         test = request.POST['test']
#         packaging =	request.POST['packaging']
#         prodpackaging =	request.POST['prodpackaging']
#         annual = request.POST['annual']
#         price =	request.POST['price']
#         ink1 = request.POST['ink1']
#         ink2 = request.POST['ink2']
#         ink3 = request.POST['ink3']
#         ink4 = request.POST['ink4']
#         ink5 = request.POST['ink5']
#         ink6 = request.POST['ink6']
#         ink7 = request.POST['ink7']
#         ink8 = request.POST['ink8']
#         ink9 = request.POST['ink9']
#         ink10 = request.POST['ink10']
#         note = request.POST['note']

#         formulario = Formulario(
#             date = date,
#             typeCo = typeCo,
#             folio = folio,
#             customerCode = customerCode,
#             customers = customers,
#             press = press,
#             request = request,
#             quotation = quotation,
#             codeUyeda = codeUyeda,
#             description	= description,
#             variant	= variant,
#             development	= development,
#             axis = axis,
#             output = output,
#             suaje = suaje,
#             substrate = substrate,
#             adhesive = adhesive,
#             backup = backup,
#             inkFront = inkFront,
#             inkAdhesive	= inkAdhesive,
#             inkBackup = inkBackup,
#             typeInk	= typeInk,
#             finished = finished,
#             specialty = specialty,
#             delivery = delivery,
#             place = place,
#             letterColor	= letterColor,
#             typeDelivery = typeDelivery,
#             speed = speed,
#             test = test,
#             packaging = packaging,
#             prodpackaging = prodpackaging,
#             annual = annual,
#             price = price,
#             ink1 = ink1,
#             ink2 = ink2,
#             ink3 = ink3,
#             ink4 = ink4,
#             ink5 = ink5,
#             ink6 = ink6,
#             ink7 = ink7,
#             ink8 = ink8,
#             ink9 = ink9,
#             ink10 = ink10,
#             note = note,
#         )

#         formulario.save()
#         return HttpResponse("Cotizacion Guardada")

#     else:
#         return HttpResponse("<h2> No se Guardo la Cotización </h2>") 



def cotizaciones(request):

    cotizaciones = Cotizacion.objects.all()

    return render(request, 'mainapp/cotizaciones.html', {
        'cotizaciónes': cotizaciones
        
    })


# def register_page(request):

#     if request.user.is_autenticated:
#         return redirect('inicio')
#     else:
#         register_form = RegisterForm()
#         if request.method == "POST":
#             register_form = RegisterForm(request.POST)
#             if register_form.is_valid():
#                 register_form.save()
#                 return redirect('inicio')
#         return render(request, 'users/register.html',{
#             'title': 'Registro',
#             'register_form': register_form
#         })

#def editar_cotizacion(request, id):

#    cotizacion = Cotizacion.objects.get(pk = id)








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