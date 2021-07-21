# Generated by Django 3.2 on 2021-06-02 20:06

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('agentcultural', '0031_auto_20210602_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='area_artistica',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Artes Visuales', 'Artes Visuales'), ('Cine y audiovisuales', 'Cine y audiovisuales'), ('Circo', 'Circo'), ('Danza', 'Danza'), ('Literatura y editorial', 'Literatura y editorial'), ('Musica ', 'Musica '), ('Teatro', 'Teatro'), ('Bibliotecas', 'Bibliotecas'), ('Bibliotecas patrimoniales', 'Bibliotecas patrimoniales'), ('Audiovisual', 'Audiovisual'), ('Editorial', 'Editorial'), ('Fonográfica', 'Fonográfica'), ('Museos ', 'Museos '), ('Museos patrimoniales', 'Museos patrimoniales'), ('Actos festivos y lúdicos', 'Actos festivos y lúdicos'), ('Conocimientos tradicionales sobre la naturaleza y el universo', 'Conocimientos tradicionales sobre la naturaleza y el universo'), ('Conocimientos y técnicas tradicionales asociadas al hábitat', 'Conocimientos y técnicas tradicionales asociadas al hábitat'), ('Cultura culinaria', 'Cultura culinaria'), ('Eventos religiosos tradicionales de carácter colectivo', 'Eventos religiosos tradicionales de carácter colectivo'), ('Juegos y deportes tradicionales', 'Juegos y deportes tradicionales'), ('Lenguas, lenguajes y tradición oral', 'Lenguas, lenguajes y tradición oral'), ('Medicina tradicional', 'Medicina tradicional'), ('PCI asociado a espacios culturales', 'PCI asociado a espacios culturales'), ('PCI asociado a los eventos de la vida cotidiana', 'PCI asociado a los eventos de la vida cotidiana'), ('Producción tradicional y propia', 'Producción tradicional y propia'), ('Sistemas normativos y formas de organización social tradicionales', 'Sistemas normativos y formas de organización social tradicionales'), ('Técnicas y tradicionales asociadas a la fabricación de objetos artesanales', 'Técnicas y tradicionales asociadas a la fabricación de objetos artesanales'), ('Museos patrimoniales', 'Museos patrimoniales')], max_length=82, null=True, verbose_name='6.3. EL ÁREA ARTÍSTICA EN LA QUE LA ORGANIZACIÓN DESARROLLA SU PRINCIPAL ACTIVIDAD ES:'),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='imparte_formacion',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Artes Visuales', 'Artes Visuales'), ('Cine y audiovisuales', 'Cine y audiovisuales'), ('Circo', 'Circo'), ('Danza', 'Danza'), ('Literatura y editorial', 'Literatura y editorial'), ('Musica ', 'Musica '), ('Teatro', 'Teatro'), ('Bibliotecas', 'Bibliotecas'), ('Bibliotecas patrimoniales', 'Bibliotecas patrimoniales'), ('Audiovisual', 'Audiovisual'), ('Editorial', 'Editorial'), ('Fonográfica', 'Fonográfica'), ('Museos ', 'Museos '), ('Museos patrimoniales', 'Museos patrimoniales'), ('Actos festivos y lúdicos', 'Actos festivos y lúdicos'), ('Conocimientos tradicionales sobre la naturaleza y el universo', 'Conocimientos tradicionales sobre la naturaleza y el universo'), ('Conocimientos y técnicas tradicionales asociadas al hábitat', 'Conocimientos y técnicas tradicionales asociadas al hábitat'), ('Cultura culinaria', 'Cultura culinaria'), ('Eventos religiosos tradicionales de carácter colectivo', 'Eventos religiosos tradicionales de carácter colectivo'), ('Juegos y deportes tradicionales', 'Juegos y deportes tradicionales'), ('Lenguas, lenguajes y tradición oral', 'Lenguas, lenguajes y tradición oral'), ('Medicina tradicional', 'Medicina tradicional'), ('PCI asociado a espacios culturales', 'PCI asociado a espacios culturales'), ('PCI asociado a los eventos de la vida cotidiana', 'PCI asociado a los eventos de la vida cotidiana'), ('Producción tradicional y propia', 'Producción tradicional y propia'), ('Sistemas normativos y formas de organización social tradicionales', 'Sistemas normativos y formas de organización social tradicionales'), ('Técnicas y tradicionales asociadas a la fabricación de objetos artesanales', 'Técnicas y tradicionales asociadas a la fabricación de objetos artesanales'), ('Museos patrimoniales', 'Museos patrimoniales')], max_length=82, null=True, verbose_name='7.1.  ¿AREAS ARTÍSTICAS EN LAS QUE IMPARTE FORMACIÓN?'),
        ),
    ]
