from __future__ import unicode_literals
import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.contenttypes.fields import GenericRelation
#Para api
import requests 
import json

#Import Modulos Extra
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

#Import Personales
from archivo.settings import MEDIA_URL

#Create your choise fields here
TIPOS_DE_ARCHIVOS = (
        (1, 'Resolución'),
        (2, 'Decreto'),
    )

#Funciones API
def obtener_organismos():
	r = requests.get('http://organigrama.jujuy.gob.ar/ws_org/')
	orgs = json.loads(r.text)['data']
	organismos = list()
	for org in orgs:
		organismos.append((org['id'],org['nombre']))
	return organismos

#Create your models here.
class Archivo(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    expediente = models.CharField('Expediente', max_length=20, null=True, blank=True)
    tipo = models.IntegerField(choices=TIPOS_DE_ARCHIVOS, default=1)
    organismo = models.PositiveIntegerField(choices= obtener_organismos(), default=0)
    fecha_aprobacion = models.DateTimeField('Fecha de Aprobacion', default=datetime.datetime.now)
    etiquetas = TaggableManager()
    resumen = models.CharField('Resumen', max_length=200)
    captura = models.ImageField(storage=FileSystemStorage(location=MEDIA_URL), null=True, blank=True)
    archivo = models.FileField(upload_to='')
    contenido = HTMLField(blank=True)
    def __str__(self):
        return self.nombre