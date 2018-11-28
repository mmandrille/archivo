from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q
#Import Personales
from .models import Archivo
from .forms import BuscarForm

#@login_required
def home(request):
    #Obtenemos los archivos que se van a mostrar:
    if request.method == 'POST': #En caso de que se haya realizado una busqueda
        form = BuscarForm(request.POST)
        if form.is_valid():
            #Realizamos la busqueda
            archivos = Archivo.objects.filter(
                Q(nombre__icontains=form.cleaned_data['texto'])|
                Q(etiquetas__icontains=form.cleaned_data['texto'])|
                Q(resumen__icontains=form.cleaned_data['texto']))
            buscado = True
    else:
        archivos = Archivo.objects.order_by('fecha_aprobacion')[:12]
        buscado = False
    #Obtenemos form de busqueda
    form = BuscarForm
    #Enviamos la pagina
    return render(request, 'home.html', {'archivos': archivos, 'form': form, 'buscado': buscado })

def mostrar_archivo(request, archivo_id):
    #Intentamos cargar el Archivo
    try:
        archivo = Archivo.objects.get(pk=archivo_id)
    except Archivo.DoesNotExist:
        raise Http404("El Archivo No Existe")
    #Si salio bien mostramos el archivo
    return render(request, 'mostrar_archivo.html', {'archivo': archivo, })

def mostrar_archivo_nombre(request, archivo_nombre):
    #Intentamos cargar el Archivo
    try:
        archivo = Archivo.objects.get(nombre=archivo_nombre)
    except Archivo.DoesNotExist:
        raise Http404("El Archivo No Existe")
    #Si salio bien mostramos el archivo
    return render(request, 'mostrar_archivo.html', {'archivo': archivo, })