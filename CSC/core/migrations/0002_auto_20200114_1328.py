# Generated by Django 2.2.9 on 2020-01-14 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-created'], 'verbose_name': 'contacto'},
        ),
    ]
