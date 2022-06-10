from django.db import models

# Create your models here.

class Cotizacion(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    typeCo = models.CharField(max_length = 25)
    folio = models.IntegerField(unique=True)
    customerCode = models.PositiveSmallIntegerField()
    customers  = models.CharField(max_length = 50)
    press = models.CharField(max_length = 25)
    request = models.CharField(max_length = 50)
    coti = models.IntegerField()
    codeUyeda = models.IntegerField()
    description = models.CharField(max_length = 100)
    variant = models.CharField(max_length = 50)
    development = models.FloatField(max_length = 15)
    axis = models.FloatField(max_length = 15)
    output = models.CharField(max_length = 25)
    suaje = models.CharField(max_length = 25)
    substrate = models.CharField(max_length = 25)
    adhesive = models.CharField(max_length = 25)
    backup = models.CharField(max_length = 25)
    inkFront = models.PositiveSmallIntegerField()
    inkAdhesive = models.PositiveSmallIntegerField()
    inkBackup = models.PositiveSmallIntegerField()
    typeInk = models.CharField(max_length = 25)
    finished = models.CharField(max_length = 25)
    specialty = models.CharField(max_length = 25)
    delivery = models.CharField(max_length = 50)
    place = models.CharField(max_length = 50)
    letterColor = models.CharField(max_length = 25)
    typeDelivery = models.CharField(max_length = 25)
    speed = models.PositiveSmallIntegerField()
    test = models.CharField(max_length = 25)
    packaging = models.CharField(max_length = 25)
    prodpackaging = models.CharField(max_length = 25)
    annual = models.IntegerField()
    price = models.FloatField(max_length = 15)
    ink1 = models.PositiveSmallIntegerField()
    ink2 = models.PositiveSmallIntegerField()
    ink3 = models.PositiveSmallIntegerField()
    ink4 = models.PositiveSmallIntegerField()
    ink5 = models.PositiveSmallIntegerField()
    ink6 = models.PositiveSmallIntegerField()
    ink7 = models.PositiveSmallIntegerField()
    ink8 = models.PositiveSmallIntegerField()
    ink9 = models.PositiveSmallIntegerField()
    ink10 = models.PositiveSmallIntegerField()
    craete_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.TextField()

    # class Meta:
    #     verbose_name = "Cotizacion"
    #     verbose_name_plural = "Cotizaciones"

    # def __str__(self):
    #     return self.folio