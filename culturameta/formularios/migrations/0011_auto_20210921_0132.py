# Generated by Django 3.2 on 2021-09-21 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0010_filarmonica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='country',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
