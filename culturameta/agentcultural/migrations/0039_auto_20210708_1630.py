# Generated by Django 3.2 on 2021-07-08 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agentcultural', '0038_auto_20210621_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentcultural',
            name='adress',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='2.3. DIRECCIÓN DE VIVIENDA'),
        ),
        migrations.AlterField(
            model_name='agentcultural',
            name='adress2',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='2.4. DIRECCIÓN DE CORRESPONDENCIA'),
        ),
    ]