# Generated by Django 2.2.6 on 2020-04-25 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='foto_portada',
        ),
    ]
