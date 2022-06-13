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
    path('crear-cotizacion/', views.cotizacion, name="crear_cotizacion"),
    path('save_cotizacion/', views.save_cotizacion, name='save'),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crear-articulo"),
    path('articulo/', views.articulo, name="articulo"),
    path('editar-articulo/<int:id>', views.editar_articulo)
    
]
