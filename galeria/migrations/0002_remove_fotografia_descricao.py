# Generated by Django 5.2.3 on 2025-06-19 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotografia',
            name='descricao',
        ),
    ]
