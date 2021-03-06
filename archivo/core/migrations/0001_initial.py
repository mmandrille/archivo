# Generated by Django 2.0.2 on 2018-10-21 23:37

import datetime
import django.core.files.storage
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('expediente', models.CharField(max_length=20, verbose_name='Expediente')),
                ('tipo', models.IntegerField(choices=[(1, 'Resolución'), (2, 'Decreto')], default=1)),
                ('organismo', models.PositiveIntegerField(choices=[(1, 'Gobierno de Jujuy'), (2, 'Ministerio de Educacion'), (3, 'Ministerio de Salud'), (4, 'Subdirección Provincial de Epidemiología'), (5, 'Unidad Bromatológica Provincial'), (16, 'Ministerio de Seguridad'), (17, 'Ministerio de Desarrollo Humano'), (18, 'Instituto Superior de Seguridad Publica'), (19, 'Policia de la Provincia de Jujuy'), (20, 'Secretaría de Niñez, Adolescencia y Familia'), (21, 'Secretaría de Asistencia Directa y Calidad de Vida'), (25, 'Ministerio de Gobierno y Justicia'), (26, 'Ministerio de Hacienda y Finanzas'), (27, 'Ministerio de Desarrollo Económico y Producción'), (28, 'Ministerio de Infraestructura, Servicios Publicos, Tierra y Vivienda'), (29, 'Ministerio de Trabajo y Empleo'), (30, 'Ministerio de Cultura y Turismo'), (31, 'Ministerio de Ambiente'), (32, 'Secretaria General de la Gobernacion'), (33, 'Fiscalia de Estado'), (34, 'Secretaria de Comunicaciones y Gobierno Abierto'), (35, 'Direccion de Unificacion Informatica'), (36, 'Dirección Provincial de Transparencia y Gobierno Abierto'), (38, 'Direccion de Medios Digitales'), (39, 'Direccion de Prensa')], default=0)),
                ('fecha_aprobacion', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de Aprobacion')),
                ('etiquetas', models.CharField(max_length=200, verbose_name='Etiquetas')),
                ('resumen', models.CharField(max_length=200, verbose_name='Resumen')),
                ('captura', models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='archivos/'), upload_to='')),
                ('archivo', models.FileField(upload_to='')),
                ('contenido', tinymce.models.HTMLField()),
            ],
        ),
    ]
