# Generated by Django 3.2 on 2021-06-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agentcultural', '0024_alter_entidad_nombre_representante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='personeria',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, null=True, verbose_name='3.4. TIENE PERSONERÍA JURÍDICA:'),
        ),
    ]
