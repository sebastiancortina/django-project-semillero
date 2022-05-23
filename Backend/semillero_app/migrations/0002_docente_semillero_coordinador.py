# Generated by Django 4.0.4 on 2022-05-23 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('semillero_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('n_identificacion', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('lugar_expedicion', models.CharField(max_length=100)),
                ('lugar_nacimiento', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('f_nacimiento', models.CharField(max_length=100)),
                ('direcccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('celular', models.IntegerField()),
                ('c_emergencia', models.CharField(max_length=100)),
                ('n_emergencia', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='semillero',
            name='coordinador',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='semillero_app.docente'),
            preserve_default=False,
        ),
    ]
