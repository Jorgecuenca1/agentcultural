# Generated by Django 3.2 on 2021-05-25 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agentcultural', '0008_alter_agentcultural_sisben'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidad',
            name='camara',
            field=models.FileField(blank=True, null=True, upload_to='agent/file', verbose_name='Camarade comercio'),
        ),
    ]
