# Generated by Django 4.0.4 on 2022-05-26 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integrantes', '0002_delete_lider_i'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=100)),
                ('n_identificacion', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='integrantes.integrante')),
            ],
        ),
    ]