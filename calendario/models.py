from django.db import models

# Create your models here.

class Evento(models.Model):
    relevancia = (
        ('leve','Leve'),
        ('importante','Importante'),
        ('urgente','Urgente')
    )
    nombre_e = models.CharField(max_length=30)
    nota_e = models.TextField()
    hora_fecha_e = models.DateTimeField()
    finalizado_e = models.BooleanField(blank=True)
    valoracion_e = models.CharField(max_length=10, choices=relevancia)
