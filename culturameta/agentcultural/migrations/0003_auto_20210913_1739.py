# Generated by Django 3.2 on 2021-09-13 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agentcultural', '0002_alter_agentcultural_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentcultural',
            name='ano_titulo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='3.11. AÑO '),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='artistic_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='1.3. NOMBRE ARTÍSTICO'),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='birthday',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='1.5. FECHA DE NACIMIENTO'),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='expedicion_passport',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='1.13. FECHA DE EXPEDICIÓN'),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='expedicion_tarjeta',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='1.11. FECHA DE EXPEDICIÓN'),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='1.2. APELLIDOS'),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='1.1. NOMBRES'),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='porcentaje',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='4.6. ¿QUÉ PORCENTAJE DE SUS INGREOS PROVIENEN DE LA ACTIVIDAD ARTÍSTICA Y CULTURAL?'),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='vencimiento_passport',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='1.14. FECHA DE VENCIMIENTO'),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='vinculacion_entidad',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='3.6. ¿DESDE QUÉ AÑO ESTÁ VINCULADO A LA ORGANIZACIÓN ARTÍSTICA O CULTURAL?'),
        ),
    ]
