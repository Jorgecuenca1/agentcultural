# Generated by Django 3.2 on 2021-05-14 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agentcultural', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentcultural',
            name='image',
            field=models.ImageField(default=1, upload_to='campaigns/images/', verbose_name='Imagen del agente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agentcultural',
            name='tipo',
            field=models.CharField(blank=True, choices=[('AGENTE CULTURAL', 'AGENTE CULTURAL'), ('GESTOR CULTURAL', 'GESTOR CULTURAL')], max_length=17, null=True, verbose_name='Agente o Gestor Cultural'),
        ),
    ]
