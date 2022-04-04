from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
""""""
class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL")
    visible = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add="True", verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now="True", verbose_name="Autualizado el")

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"

    def __str__(self):
        return self.title


class Cotizacion(models.Model):
    date = models.CharField(max_length = 100)
    typeCo = models.CharField(max_length = 100)
    folio = models.CharField(max_length = 100)
    customerCode = models.CharField(max_length = 100)
    customers  = models.CharField(max_length = 100)
    press = models.CharField(max_length = 100)
    request = models.CharField(max_length = 100)
    quote = models.CharField(max_length = 100)
    codeUyeda = models.CharField(max_length = 100) 
    description = models.CharField(max_length = 100)
    variant = models.CharField(max_length = 100)
    development = models.CharField(max_length = 100)
    axis = models.CharField(max_length = 100)
    output = models.CharField(max_length = 100)
    suaje = models.CharField(max_length = 100)
    substrate = models.CharField(max_length = 100)
    adhesive = models.CharField(max_length = 100)
    backup = models.CharField(max_length = 100)
    inkFront = models.CharField(max_length = 100)
    inkAdhesive = models.CharField(max_length = 100)
    inkBackup = models.CharField(max_length = 100)
    typeInk = models.CharField(max_length = 100)
    finished = models.CharField(max_length = 100)
    specialty = models.CharField(max_length = 100)
    delivery = models.CharField(max_length = 100)
    place = models.CharField(max_length = 100)
    letterColor = models.CharField(max_length = 100)
    typeDelivery = models.CharField(max_length = 100)
    speed = models.CharField(max_length = 100)
    test = models.CharField(max_length = 100)
    packaging = models.CharField(max_length = 100)
    prodpackaging = models.CharField(max_length = 100)
    annual = models.CharField(max_length = 100)
    price = models.CharField(max_length = 100)
    ink1 = models.CharField(max_length = 100)
    ink2 = models.CharField(max_length = 100)
    ink3 = models.CharField(max_length = 100)
    ink4 = models.CharField(max_length = 100)
    ink5 = models.CharField(max_length = 100)
    ink6 = models.CharField(max_length = 100)
    ink7 = models.CharField(max_length = 100)
    ink8 = models.CharField(max_length = 100)
    ink9 = models.CharField(max_length = 100)
    ink10 = models.CharField(max_length = 100)
    craete_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.TextField()