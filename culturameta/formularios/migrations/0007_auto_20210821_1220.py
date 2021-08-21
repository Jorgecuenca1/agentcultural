# Generated by Django 3.2 on 2021-08-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0006_alter_torneo_agrupacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='torneo',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Adjuntar el link del archivo de wetranfer donde envia el audio formato punto wav, mp3 etc... y vídeo y/o videos (mínimo una cámara máximo tres cámaras grabando simultáneamente) FHD, 1080p o superior de la propuesta según sea la modalidad seleccionada: *'),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='archivo2',
            field=models.FileField(blank=True, null=True, upload_to='torneo/file', verbose_name=''),
        ),
    ]
