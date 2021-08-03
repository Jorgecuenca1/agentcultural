# Generated by Django 3.2 on 2021-08-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agentcultural', '0044_alter_disability_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentcultural',
            name='ano_titulo',
            field=models.DateField(blank=True, null=True, verbose_name='3.11. AÑO '),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='expedicion_passport',
            field=models.DateField(blank=True, null=True, verbose_name='1.13. FECHA DE EXPEDICIÓN'),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='expedicion_tarjeta',
            field=models.DateField(blank=True, null=True, verbose_name='1.11. FECHA DE EXPEDICIÓN'),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='vencimiento_passport',
            field=models.DateField(blank=True, null=True, verbose_name='1.14. FECHA DE VENCIMIENTO'),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='vinculacion_entidad',
            field=models.DateField(blank=True, null=True, verbose_name='3.6. ¿DESDE QUÉ AÑO ESTÁ VINCULADO A LA ORGANIZACIÓN ARTÍSTICA O CULTURAL?'),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='1.4. AÑO DE CONSTITUCIÓN'),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='vinculacion_representante',
            field=models.DateField(blank=True, null=True, verbose_name='1.9. AÑO DE VINCULACIÓN'),
        ),
    ]