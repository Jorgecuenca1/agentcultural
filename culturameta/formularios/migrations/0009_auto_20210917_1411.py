# Generated by Django 3.2 on 2021-09-17 19:11

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0008_auto_20210917_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuesto',
            name='identification',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Identificación'),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='type_document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='formularios.typedocument', verbose_name='Tipo de documento'),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='area',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('MÚSICA', 'MÚSICA'), ('DANZA', 'DANZA'), ('TEATRO', 'TEATRO'), ('CIRCO', 'CIRCO'), ('ARTES PLÁSTICAS Y VISUALES', 'ARTES PLÁSTICAS Y VISUALES'), ('CINEMATOGRAFÍA', 'CINEMATOGRAFÍA'), ('LITERATURA', 'LITERATURA'), ('PATRIMONIO', 'PATRIMONIO'), ('RED DE BIBLIOTECAS PÚBLICAS DEL META', 'RED DE BIBLIOTECAS PÚBLICAS DEL META')], max_length=82, null=True, verbose_name='9. Área (s) Artísticas + Patrimonio + Red de bibliotecas: '),
        ),
        migrations.AlterField(
            model_name='presupuesto',
            name='perfil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='formularios.perfil', verbose_name='Perfil *'),
        ),
    ]
