from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'corearchivo'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('etiqueta/<int:etiqueta_id>/', views.mostrar_archivos_etiqueta, name='mostrar_archivos_etiqueta'),
    path('repositorio/<int:archivo_id>/', views.mostrar_archivo, name='mostrar_archivo'),
    path('repositorio/<str:archivo_nombre>/', views.mostrar_archivo_nombre, name='mostrar_archivo_nombre'),
]