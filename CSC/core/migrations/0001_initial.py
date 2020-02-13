# Generated by Django 2.2.9 on 2020-02-11 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='nombre')),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=10, verbose_name='telefono')),
                ('message', models.TextField(verbose_name='mensaje')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'contacto',
                'ordering': ['-created'],
            },
        ),
    ]
