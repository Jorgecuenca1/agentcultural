# Generated by Django 3.2 on 2021-07-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqrsd',
            name='identification',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='5.Identificación'),
        ),
        migrations.AlterField(
            model_name='pqrsd',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='7.Identificación'),
        ),
    ]