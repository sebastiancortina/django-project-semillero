# Generated by Django 4.0.4 on 2022-05-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semillero_app', '0009_remove_actividad_i_actividad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semillero',
            name='facultad',
            field=models.CharField(max_length=250, verbose_name='FACULTAD'),
        ),
        migrations.AlterField(
            model_name='semillero',
            name='investigacion',
            field=models.CharField(max_length=250, verbose_name='GRUPO DE INVESTIGACIÓN AL CUAL ESTÁ VINCULADO EL SEMILLERO'),
        ),
        migrations.AlterField(
            model_name='semillero',
            name='investigacion_asociado',
            field=models.CharField(max_length=250, verbose_name='LÍNEA Y SUBLÍNEA DE INVESTIGACIÓN ASOCIADOS'),
        ),
        migrations.AlterField(
            model_name='semillero',
            name='justificacion',
            field=models.TextField(max_length=2000, verbose_name=' JUSTIFICACIÓN DEL SEMILLERO DE INVESTIGACIÓN'),
        ),
        migrations.AlterField(
            model_name='semillero',
            name='nombre',
            field=models.CharField(max_length=250, verbose_name='NOMBRE DEL SEMILLERO'),
        ),
        migrations.AlterField(
            model_name='semillero',
            name='programa_academico',
            field=models.CharField(max_length=250, verbose_name='PROGRMA ACADÉMICO'),
        ),
        migrations.AlterField(
            model_name='semillero',
            name='tematica',
            field=models.CharField(max_length=250, verbose_name='TÉMATICA DE ESTUDIO DEL SEMILLERO'),
        ),
    ]
