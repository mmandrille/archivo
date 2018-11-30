from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q, Count
#Import incluidos
from taggit.models import Tag
#Import Personales
from .models import Archivo, obtener_organismos
from .forms import BuscarForm

#@login_required
def home(request, etiqueta_id=None, organismo_id=None):
    #Obtenemos los archivos que se van a mostrar:
    if request.method == 'POST': #En caso de que se haya realizado una busqueda
        form = BuscarForm(request.POST)
        if form.is_valid():
            #Realizamos la busqueda
            archivos = Archivo.objects.filter(
                Q(nombre__icontains=form.cleaned_data['texto'])|
                Q(etiquetas__name=form.cleaned_data['texto'])|
                Q(resumen__icontains=form.cleaned_data['texto'])).distinct()
            buscado = True
    else:
        if etiqueta_id is not None:
                #Obtenemos etiqueta
                etiqueta = Tag.objects.get(pk=etiqueta_id)
                #Obtenemos Archivos Taggeados
                archivos = Archivo.objects.filter(etiquetas=etiqueta)
        if organismo_id is not None:
                #Obtenemos Archivos del organismo
                archivos = Archivo.objects.filter(organismo=organismo_id)
        if etiqueta_id is None and organismo_id is None:
                archivos = Archivo.objects.order_by('fecha_aprobacion')[:12]
        buscado = False
    #ETIQUETAS
    #Obtenemos las 5 tags mas usadas
    etiquetas = Archivo.etiquetas.most_common()[:5]
    #ORGANISMOS
    #obtenemos los 10 Organismos mas usados
    ranking_organismos = Archivo.objects.values("organismo").annotate(count=Count('organismo')).order_by("-count")[:10]
    #Obtenemos desde el sitio de organigrama todos los organismos > Ver models.py
    organismos = obtener_organismos()
    #lista_organismos= [organismo for organismo in organismos if organismo[0] == ranking_organismos[0]['organismo']]
    lista_organismos=   [organismo #SI, acabas de ver la listcompression mas loca de la historia xD
                        for organismo_ranking in [ranking['organismo']
                        for ranking in ranking_organismos]
                        for organismo in organismos
                        if organismo[0] == organismo_ranking]
    print(lista_organismos)
    #Obtenemos form de busqueda
    form = BuscarForm
    #Enviamos la pagina
    return render(request, 'home.html', {'archivos': archivos, 'etiquetas': etiquetas, 'organismos': lista_organismos, 'form': form, 'buscado': buscado })

def mostrar_archivo(request, archivo_id):
    #Intentamos cargar el Archivo
    try:
        archivo = Archivo.objects.get(pk=archivo_id)
    except Archivo.DoesNotExist:
        raise Http404("El Archivo No Existe")
    organismos = obtener_organismos()
    #Si salio bien mostramos el archivo
    return render(request, 'mostrar_archivo.html', {'archivo': archivo, 'organismos': organismos})

def mostrar_archivo_nombre(request, archivo_nombre):
    #Intentamos cargar el Archivo
    try:
        archivo = Archivo.objects.get(nombre=archivo_nombre)
    except Archivo.DoesNotExist:
        raise Http404("El Archivo No Existe")
    #Si salio bien mostramos el archivo
    return render(request, 'mostrar_archivo.html', {'archivo': archivo, })