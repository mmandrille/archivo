from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'corejujuy'
urlpatterns = [
    url(r'^$', views.home, name='home'),

    path('repositorio/<int:archivo_id>/', views.mostrar_archivo, name='mostrar_archivo'),
]