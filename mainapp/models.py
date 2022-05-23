from django.db import models

# Create your models here.

class Cotizacion(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    typeCo = models.CharField(max_length = 25)
    folio = models.PositiveSmallIntegerField(max_length=25)
    customerCode = models.PositiveSmallIntegerField(max_length=25)
    customers  = models.CharField(max_length = 50)
    press = models.CharField(max_length = 25)
    request = models.CharField(max_length = 50)
    quotation = models.PositiveSmallIntegerField(max_length=25)
    codeUyeda = models.PositiveSmallIntegerField(max_length=25)
    description = models.CharField(max_length = 100)
    variant = models.CharField(max_length = 50)
    development = models.FloatField(max_length = 15)
    axis = models.FloatField(max_length = 15)
    output = models.CharField(max_length = 25)
    suaje = models.CharField(max_length = 25)
    substrate = models.CharField(max_length = 25)
    adhesive = models.CharField(max_length = 25)
    backup = models.CharField(max_length = 25)
    inkFront = models.PositiveSmallIntegerField(max_length=25)
    inkAdhesive = models.PositiveSmallIntegerField(max_length=25)
    inkBackup = models.PositiveSmallIntegerField(max_length=25)
    typeInk = models.CharField(max_length = 25)
    finished = models.CharField(max_length = 25)
    specialty = models.CharField(max_length = 25)
    delivery = models.CharField(max_length = 50)
    place = models.CharField(max_length = 50)
    letterColor = models.CharField(max_length = 25)
    typeDelivery = models.CharField(max_length = 25)
    speed = models.PositiveSmallIntegerField(max_length=25)
    test = models.CharField(max_length = 25)
    packaging = models.CharField(max_length = 25)
    prodpackaging = models.CharField(max_length = 25)
    annual = models.PositiveSmallIntegerField(max_length=25)
    price = models.FloatField(max_length = 15)
    ink1 = models.PositiveSmallIntegerField(max_length=25)
    ink2 = models.PositiveSmallIntegerField(max_length=25)
    ink3 = models.PositiveSmallIntegerField(max_length=25)
    ink4 = models.PositiveSmallIntegerField(max_length=25)
    ink5 = models.PositiveSmallIntegerField(max_length=25)
    ink6 = models.PositiveSmallIntegerField(max_length=25)
    ink7 = models.PositiveSmallIntegerField(max_length=25)
    ink8 = models.PositiveSmallIntegerField(max_length=25)
    ink9 = models.PositiveSmallIntegerField(max_length=25)
    ink10 = models.PositiveSmallIntegerField(max_length=25)
    craete_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.TextField()

    class Meta:
        verbose_name = "Cotizacion"
        verbose_name_plural = "Cotizaciones"

    def __str__(self):
        return self.folio