from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Formulario/', views.Formulario, name="form"),
    path('cotizaciones/', views.cotizaciones, name="cotizaciones"),
    path('inicio/', views.index, name="inicio"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    #path('save-form/', views.save_form, name="save"),
    path('crear-cotizacion/', views.crear_cotizacion, name="crear_cotizacion"),
    
    
]
