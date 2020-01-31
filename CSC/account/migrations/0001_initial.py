# Generated by Django 2.2.9 on 2020-01-30 17:27

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlNumber',
            fields=[
                ('control_number', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='numero de control')),
                ('is_active', models.BooleanField(default=False, verbose_name='activado')),
            ],
            options={
                'verbose_name': 'numero de control',
                'verbose_name_plural': 'numeros de control',
                'ordering': ['control_number'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_last_name', models.CharField(blank=True, max_length=50, verbose_name='apellido paterno')),
                ('photo', models.ImageField(blank=True, upload_to=account.models.photo_account, verbose_name='foto de perfil')),
                ('semester', models.CharField(blank=True, choices=[('1', 'Primero'), ('2', 'Segundo'), ('3', 'Tercero'), ('4', 'Cuarto'), ('5', 'Quinto'), ('6', 'Sexto'), ('7', 'Séptimo'), ('8', 'Octavo'), ('9', 'Noveno'), ('10', 'Décimo'), ('11', 'Onceavo'), ('12', 'Doceavo')], max_length=1, verbose_name='semestre')),
                ('birthday', models.DateField(null=True, verbose_name='fecha de nacimiento')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='genero')),
                ('phone', models.CharField(blank=True, max_length=10, verbose_name='telefono')),
                ('facebook', models.URLField(blank=True, verbose_name='facebook')),
                ('instagram', models.URLField(blank=True, verbose_name='instagram')),
                ('github', models.URLField(blank=True, verbose_name='gitHub')),
                ('gitlab', models.URLField(blank=True, verbose_name='gitLab')),
                ('control_number', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.ControlNumber', verbose_name='número de control')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'cuenta',
                'ordering': ['control_number'],
            },
        ),
    ]
