from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.
PRACTICA_CHOICES = (
        ('DANZA - CONTEMPORANEA', 'DANZA - CONTEMPORANEA'),
        ('DANZA - BALLET', 'DANZA - BALLET'),
        ('DANZA - URBANA', 'DANZA - URBANA'),
        ('DANZA - FOLCLOR', 'DANZA - FOLCLOR'),
        ('MÚSICA - BANDAS', 'MÚSICA - BANDAS'),
        ('MÚSICA - COROS', 'MÚSICA - COROS'),
        ('MÚSICA - ORQUESTA SINFÓNICA', 'MÚSICA - ORQUESTA SINFÓNICA'),
        ('MÚSICA - AGRUPACIONES MÚSICA TRADICIONAL', 'MÚSICA - AGRUPACIONES MÚSICA TRADICIONAL'),
        ('MÚSICA - POPULAR', 'MÚSICA - POPULAR'),
        ('MÚSICA - AGRUPACIONES MÚSICA ACADÉMICA', 'MÚSICA - AGRUPACIONES MÚSICA ACADÉMICA'),
        ('TEATRO - DE SALA', 'TEATRO - DE SALA'),
        ('TEATRO - TITERES', 'TEATRO - TITERES'),
        ('TEATRO - MUSICAL', 'TEATRO - MUSICAL'),
        ('TEATRO - PARA ESPACIOS NO CONVENCIONALES', 'TEATRO - PARA ESPACIOS NO CONVENCIONALES'),
        ('LITERATURA - EDITORIALES', 'LITERATURA - EDITORIALES'),
        ('LITERATURA - REVISTAS', 'LITERATURA - REVISTAS'),
        ('LITERATURA - TALLERES', 'LITERATURA - TALLERES'),
        ('LITERATURA - INSTITUCIONES LITERARIAS', 'LITERATURA - INSTITUCIONES LITERARIAS'),
        ('TEATRO - UNIVERSIDADES', 'TEATRO - UNIVERSIDADES'),
        ('TEATRO - CÀMARA DEL LIBRO', 'TEATRO - CÀMARA DEL LIBRO'),
        ('ARTES - PLÁSTICA', 'ARTES - PLÁSTICA'),
        ('ARTES - VISUAL', 'ARTES - VISUAL'),
        ('CINEMATOGRAFÍA', 'CINEMATOGRAFÍA'),

    )
AREA_CHOICES = (
        ('Artes Visuales','Artes Visuales'),
        ('Cine y audiovisuales', 'Cine y audiovisuales'),
        ('Circo', 'Circo'),
        ('Danza', 'Danza'),
        ('Literatura y editorial', 'Literatura y editorial'),
        ('Música ', 'Música '),
        ('Teatro', 'Teatro'),
        ('Bibliotecas', 'Bibliotecas'),
        ('Bibliotecas patrimoniales', 'Bibliotecas patrimoniales'),
        ('Audiovisual', 'Audiovisual'),
        ('Editorial', 'Editorial'),
        ('Fonográfica', 'Fonográfica'),
        ('Museos ', 'Museos '),
        ('Museos patrimoniales', 'Museos patrimoniales'),
        ('Actos festivos y lúdicos', 'Actos festivos y lúdicos'),
        ('Conocimientos tradicionales sobre la naturaleza y el universo', 'Conocimientos tradicionales sobre la naturaleza y el universo'),
        ('Conocimientos y técnicas tradicionales asociadas al hábitat', 'Conocimientos y técnicas tradicionales asociadas al hábitat'),
        ('Cultura culinaria', 'Cultura culinaria'),
        ('Eventos religiosos tradicionales de carácter colectivo', 'Eventos religiosos tradicionales de carácter colectivo'),
        ('Juegos y deportes tradicionales', 'Juegos y deportes tradicionales'),
        ('Lenguas, lenguajes y tradición oral', 'Lenguas, lenguajes y tradición oral'),
        ('Medicina tradicional', 'Medicina tradicional'),
        ('PCI asociado a espacios culturales', 'PCI asociado a espacios culturales'),
        ('PCI asociado a los eventos de la vida cotidiana', 'PCI asociado a los eventos de la vida cotidiana'),
        ('Producción tradicional y propia', 'Producción tradicional y propia'),
        ('Sistemas normativos y formas de organización social tradicionales', 'Sistemas normativos y formas de organización social tradicionales'),
        ('Técnicas y tradicionales asociadas a la fabricación de objetos artesanales','Técnicas y tradicionales asociadas a la fabricación de objetos artesanales'),
        ('Museos patrimoniales', 'Museos patrimoniales'),

    )
NIVEL_CHOICES = (
        ('INTERNACIONAL', 'INTERNACIONAL'),
        ('NACIONAL', 'NACIONAL'),
        ('DEPARTAMENTAL', 'DEPARTAMENTAL'),
        ('MUNICIPAL', 'MUNICIPAL'),

    )
FUENTEINGRESO_CHOICES = (
        ('LA ACTIVIDAD ARTÍSTICA Y CULTURAL ES SU PRINCIPAL FUENTE DE INGRESO', 'LA ACTIVIDAD ARTÍSTICA Y CULTURAL ES SU PRINCIPAL FUENTE DE INGRESO'),
        ('LA ACTIVIDAD ARTÍSTICA Y CULTURAL ES SU FUENTE ALTERNATIVA DE INGRESO', 'LA ACTIVIDAD ARTÍSTICA Y CULTURAL ES SU FUENTE ALTERNATIVA DE INGRESO'),
        ('NO RECIBE INGRESO POR CONCEPTO DE SU ACTIVIDAD ARTÍSTICA Y CULTURAL', 'NO RECIBE INGRESO POR CONCEPTO DE SU ACTIVIDAD ARTÍSTICA Y CULTURAL'),
    )
NIVELEDUCACION_CHOICES = (
        ('PRIMARIA INCOMPLETA', 'PRIMARIA INCOMPLETA'),
        ('PRIMARIA COMPLETA', 'PRIMARIA COMPLETA'),
        ('SECUNDARIA INCOMPLETA', 'SECUNDARIA INCOMPLETA'),
        ('SECUNDARIA COMPLETA', 'SECUNDARIA COMPLETA'),
        ('UNIVERSITARIO SIN TÍTULO', 'UNIVERSITARIO SIN TÍTULO'),
        ('UNIVERSITARIO CON TÍTULO', 'UNIVERSITARIO CON TÍTULO'),
        ('AUTODIDACTA', 'AUTODIDACTA'),
        ('TÉCNICO/TECNÓLOGO', 'TÉCNICO/TECNÓLOGO'),
        ('POSTGRADO', 'POSTGRADO'),
        ('OTRA', 'OTRA'),

)
AGENTEAREA_CHOICES = (
        ('MÚSICA', 'MÚSICA'),
        ('DANZA', 'DANZA'),
        ('TEATRO', 'TEATRO'),
        ('CIRCO', 'CIRCO'),
        ('ARTES PLÁSTICAS Y VISUALES', 'ARTES PLÁSTICAS Y VISUALES'),
        ('CINEMATOGRAFÍA', 'CINEMATOGRAFÍA'),
        ('GASTRONIMÍA', 'GASTRONOMÍA'),
        ('LITERATURA', 'LITERATURA'),
        ('PATRIMONIO', 'PATRIMONIO'),

    )
AGENTEPRACTICA_CHOICES = (
        ('DIRECTOR', 'DIRECTOR'),
        ('GESTOR', 'GESTOR'),
        ('TÉCNICO', 'TÉCNICO'),
        ('FORMADOR', 'FORMADOR'),
        ('PRODUCTOR', 'PRODUCTOR'),
        ('COMPOSITOR', 'COMPOSITOR'),
        ('CRÍTICO', 'CRÍTICO'),
        ('PROMOTOR', 'PROMOTOR'),
        ('INVESTIGADOR', 'INVESTIGADOR'),
        ('INGENIERO DE SONIDO', 'INGENIERO DE SONIDO'),
        ('INTÉRPRETE', 'INTÉRPRETE'),
        ('LUTHIER', 'LUTHIER'),
        ('ARREGLISTA', 'ARREGLISTA'),
        ('GUIONISTA', 'GUIONISTA'),
        ('REALIZADOR', 'REALIZADOR'),
        ('EXHIBIDOR', 'EXHIBIDOR'),
        ('DISTRIBUIDOR', 'DISTRIBUIDOR'),
        ('RESTAURADOR', 'RESTAURADOR'),
        ('PINTOR', 'PINTOR'),
        ('ESCULTOR', 'ESCULTOR'),
        ('CURADOR', 'CURADOR'),
        ('GALERISTA', 'GALERISTA'),
        ('DISEÑADOR', 'DISEÑADOR'),
        ('FOTÓGRAFO', 'FOTÓGRAFO'),
        ('VIDEO ARTISTA', 'VIDEO ARTISTA'),
        ('ACTOR/ACTRIZ', 'ACTOR/ACTRIZ'),
        ('VESTUARISTA', 'VESTUARISTA'),
        ('ESCENÓGRAFO', 'ESCENÓGRAFO'),
        ('BAILARÍN', 'BAILARÍN'),
        ('COREÓGRAFO', 'COREÓGRAFO'),
        ('DRAMATURGO', 'DRAMATURGO'),
        ('EDITOR', 'EDITOR'),
        ('ESCRITOR', 'ESCRITOR'),
        ('LIBRERO', 'LIBRERO'),
        ('OTRAS', 'OTRAS'),
    )
ZONA_CHOICES = (
        ('URBANA', 'URBANA'),
        ('RURAL', 'RURAL'),
    )
TIPOVINCULACION_CHOICES = (
        ('LABORAL PERMANENTE', 'LABORAL PERMANENTE'),
        ('CONTRATISTA', 'CONTRATISTA'),
        ('OTRO', 'OTRO'),
    )
TIPO_CHOICES = (
        ('PRODUCCIÓN, COMERCIALIZACIÓN Y DIVULGACIÓN', 'PRODUCCIÓN, COMERCIALIZACIÓN Y DIVULGACIÓN'),
        ('EMPRESA FONOGRÁFICA', 'EMPRESA FONOGRÁFICA'),
        ('EDITORIAL', 'EDITORIAL'),
        ('EMPRESA EN CONSTRUCCIÓN Y REPARACIÓN DE INSTITUCIÓN', 'EMPRESA EN CONSTRUCCIÓN Y REPARACIÓN DE INSTITUCIÓN'),
        ('PRODUCTORA DE EVENTOS', 'PRODUCTORA DE EVENTOS'),
        ('REPRESENTACIÓN ARTÍSTICA', 'REPRESENTACIÓN ARTÍSTICA'),
        ('DISTRIBUIDORA', 'DISTRIBUIDORA'),
        ('GALERISTA', 'GALERISTA'),

    )
EDAD_CHOICES = (
        ('INFANCIA', 'INFANCIA'),
        ('JUVENTUD', 'JUVENTUD'),
        ('ADULTOS', 'ADULTOS'),
        ('TERCERA EDAD', 'TERCERA EDAD'),
        ('TODOS', 'TODOS'),

    )
AGENTE_CHOICES = (
        ('AGENTE CULTURAL', 'AGENTE CULTURAL'),
        ('GESTOR CULTURAL', 'GESTOR CULTURAL'),
    )
FORMAPRACTICA_CHOICES = (
        ('AFICIONADO', 'AFICIONADO'),
        ('PROFESIONAL', 'PROFESIONAL'),
    )
CARACTER_CHOICES = (
        ('GRATUITO Y PÚBLICO', 'GRATUITO Y PÚBLICO'),
        ('GRATUITO RESTRINGIDO', 'GRATUITO RESTRINGIDO'),
        ('PAGO', 'PAGO'),
        ('APORTE', 'APORTE'),
        ('VOLUNTARIO', 'VOLUNTARIO'),
        ('OTRO', 'OTRO'),

    )

ACTIVIDAD_CHOICES = (
        ('FORMACIÓN', 'FORMACIÓN'),
        ('PRÁCTICA ARTISTICA', 'PRÁCTICA ARTISTICA'),
        ('GESTIÓN', 'GESTIÓN'),
        ('CIRCULACIÓN Y COMERCIALIZACIÓN', 'CIRCULACIÓN Y COMERCIALIZACIÓN'),

    )
MODALIDAD_CHOICES = (
        ('FORMAL', 'FORMAL'),
        ('NO FORMAL', 'NO FORMAL'),

    )



DURACION_CHOICES = (
        ('1 - 4 MESES', 'INTERNACIONAL'),
        ('5 - 8 MESES', 'NACIONAL'),
        ('MAS DE 8 MESES', 'DEPARTAMENTAL'),
    )
SEX_CHOICES = (
        ('F', 'Femenino',),
        ('M', 'Masculino',),
        ('O', 'Otro',),
    )
TIPOEMPLEO_CHOICES = (
        ('REMUNERADO', 'REMUNERADO',),
        ('NO REMUNERADO', 'NO REMUNERADO',),
        ('AMBOS', 'AMBOS',),
    )
ESPACIO_CHOICES = (
        ('PROPIO', 'PROPIO',),
        ('EN ARRIENDO', 'EN ARRIENDO',),
        ('EN COMODATO', 'EN COMODATO',),
        ('PRESTAMO', 'PRESTAMO',),
        ( 'NO TIENE', 'NO TIENE',),
    )
ESPACIOACTIVIDADES_CHOICES = (
        ('AUDITORIOS', 'AUDITORIOS',),
        ('AULAS', 'AULAS',),
        ('BIBLIOTECAS', 'BIBLIOTECAS',),
        ('CENTROS DE DOCUMENTACIÓN', 'CENTROS DE DOCUMENTACIÓN',),
        ( 'ESTUDIOS DE PRODUCCIÓN', 'ESTUDIOS DE PRODUCCIÓN',),
        ('GALERÍAS', 'GALERÍAS',),
        ('MUSEOS', 'MUSEOS',),
        ('OFICINAS', 'OFICINAS',),
        ('PUNTOS DE VENTA', 'PUNTOS DE VENTA',),
        ( 'SALAS DE ENSAYO', 'SALAS DE ENSAYO',),
        ('SALAS DE ESTUDIO INDIVIDUAL', 'SALAS DE ESTUDIO INDIVIDUAL',),
        ('SALAS DE EXHIBICIÓN', 'SALAS DE EXHIBICIÓN',),
        ('SALAS DE REUNIÓN', 'SALAS DE REUNIÓN',),
        ('TALLERES', 'TALLERES',),
        ( 'TEATROS', 'TEATROS',),
    )
BOOLEAN_CHOICES = (
        ('SI', 'SI',),
        ('NO', 'NO',),

    )
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Nombre del país', max_length=254)
    phone_code = models.CharField(verbose_name='Código número telefónico', max_length=5)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(verbose_name='Nombre del departamento', max_length=254)

    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='País')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return '{} | {}'.format(self.country.name, self.name)


class City(models.Model):

    name = models.CharField(verbose_name='Nombre municipio', max_length=254)
    state = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Departamento')

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return '{} | {} | {}'.format(self.state.country.name, self.state.name, self.name)

    def save(self, *args, **kwargs):
        super(City, self).save(*args, **kwargs)


class Zone(models.Model):

    name = models.CharField(verbose_name='COmuna', max_length=254)
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Municipio')

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

    def __str__(self):
        return '{} | {} | {} | {}'.format(self.city.state.country.name, self.city.state.name, self.city.name, self.name)

class TypeDocument(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de documento')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'TIpo de documentos'
class Genero(models.Model):
    name = models.CharField(max_length=30, blank= True,verbose_name='TIpo de Identidad de Genero')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de Identidad de  Genero'
        verbose_name_plural = 'TIpo de Identidad de Generos'


class GroupEtnico(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='TIpo de grupo etnico')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TIpo de grupo etnico'
        verbose_name_plural = 'TIpo de grupo etnicos'

class Disability(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='TIpo de Discapacidad')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TIpo de Discapacidad'
        verbose_name_plural = 'TIpo de Discapacidad'

class PopulationGroup(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='TIpo de Grupo poblacional')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TIpo de Grupo poblacional'
        verbose_name_plural = 'TIpo de Grupo poblacional'

class RuralZone(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Zona rural')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Zona rural'
        verbose_name_plural = 'Zonas rurales'

class HousingStratum(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Estrato de vivienda')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estrato de vivienda'
        verbose_name_plural = 'Estratos de vivienda'

class HealthRegimen(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Regimen de salud')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Regimen de salud'
        verbose_name_plural = 'Regimenes de salud'


class PensionRegimen(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Regimen de pension')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Regimen de pension'
        verbose_name_plural = 'Regimenes de pension'

class MonthlyIncome(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Ingresos Mensuales')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ingreso Mensual'
        verbose_name_plural = 'Ingresos Mensuales'

class Sector(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Sector')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'

class Area(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Area')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

class Ocupacion(models.Model):
    ocupacion = models.CharField(max_length=30, blank=True, verbose_name='Ocupacion')

    def __str__(self):
        return self.ocupacion

    class Meta:
        verbose_name = 'Ocupacion'
        verbose_name_plural = 'Ocupaciones'

class Activity(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Actividad')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividad'

class HeritageWatch(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Vigia de Patrimonio')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vigia de patrimonio'
        verbose_name_plural = 'Vigias de patrimonio'
class Formacion(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Formacion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Formacion'
        verbose_name_plural = 'Formacion'
class FormacionE(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Formacion de la entidad')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Formacion Entidad'
        verbose_name_plural = 'Formacion Entidad'
class Manifestation(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Manifestacion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Manifestacion'
        verbose_name_plural = 'Manifestacion'

class Victima(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='HÉCHO VICTIMIZANTE')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hecho victimizante'
        verbose_name_plural = 'Hechos victimizantes'

class AgentCultural(models.Model):
    SECTOR_CHOICES = (
        ('Artes','Artes'),
        ('Bibliotecas', 'Bibliotecas'),
        ('Industrias Culturales','Industrias Culturales'),
        ('Museos', 'Museos'),
        ('Patrimonio cultural inmaterial', 'Patrimonio cultural inmaterial'),
        ('Patrimonio cultural inmueble', 'Patrimonio cultural inmueble'),
        ('Patrimonio cultural mueble', 'Patrimonio cultural mueble'),

    )
    user = models.OneToOneField(User, on_delete=models.PROTECT, blank=True, null=True)
    tipo = models.CharField(max_length=17, choices=AGENTE_CHOICES, verbose_name='1.AGENTE O GESTOR CULTURAL', null=True,
                            blank=True)
    image = models.ImageField(verbose_name='Imagen del agente', upload_to='agent/image',blank=True,null=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='1.1. NOMBRES', null=True)
    last_name = models.CharField(max_length=30, blank=True, verbose_name='1.2. APELLIDOS', null=True)
    artistic_name = models.CharField(max_length=30, blank=True, verbose_name='1.3. NOMBRE ARTÍSTICO', null=True)
    gender = models.ForeignKey(Genero, verbose_name='1.4. GÉNERO', on_delete=models.PROTECT, blank=True, null=True)
    birthday = models.DateField(verbose_name='1.5. FECHA DE NACIMIENTO', auto_now=True, editable=False, blank=True,
                                null=True)
    lugar_nacimiento = models.CharField(max_length=30, blank=True, verbose_name='1.6. LUGAR DE NACIMIENTO', null=True)
    type_document = models.ForeignKey(TypeDocument, verbose_name='1.7. TIPO DOCUMENTO IDENTIDAD', on_delete=models.PROTECT,
                                      blank=True, null=True)
    identification = models.IntegerField(max_length=30, verbose_name='1.8. NÚMERO DE DOCUMENTO', blank=True, null=True)
    lugar_expedicion = models.CharField(max_length=30, blank=True, verbose_name='1.9. LUGAR DE EXPEDICIÓN', null=True)
    tarjeta_profesional = models.CharField(max_length=30, blank=True, verbose_name='1.10. TARJETA PROFESIONAL', null=True)
    expedicion_tarjeta = models.DateField(verbose_name='1.11. FECHA DE EXPEDICIÓN', auto_now=False, editable=True, blank=True,
                                null=True)
    passport = models.CharField(max_length=30, blank=True, verbose_name='1.12. PASAPORTE', null=True)
    expedicion_passport = models.DateField(verbose_name='1.13. FECHA DE EXPEDICIÓN', auto_now=False, editable=True, blank=True,
                                          null=True)
    vencimiento_passport = models.DateField(verbose_name='1.14. FECHA DE VENCIMIENTO', auto_now=False, editable=True, blank=True,
                                           null=True)
    posee_discapacidad = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='1.15. ¿POSEE ALGUNA DISCAPACIDAD FÍSICA?', null=True, blank=True)
    disability = models.ForeignKey(Disability, verbose_name='1.16. ¿CUÁL ?', on_delete=models.PROTECT, blank=True,
                                   null=True)
    posee_etnico = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                          verbose_name='1.17. ¿PERTENECE A UNA MINORÍA ÉTNICA?', null=True,
                                          blank=True)
    etnico = models.ForeignKey(GroupEtnico, verbose_name='1.18. ¿CUÁL?', on_delete=models.PROTECT, blank=True,
                               null=True)
    esvictima = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                    verbose_name='1.19. ¿ES VÍCTIMA?', null=True,
                                    blank=True)
    victima = models.ForeignKey(Victima, verbose_name='1.20. ¿HECHO VICTIMIZANTE?', on_delete=models.PROTECT,
                               blank=True,
                               null=True)
    city = models.ForeignKey(City, verbose_name='2.1. MUNICIPIO', on_delete=models.PROTECT, blank=True, null=True)
    zona = models.CharField(max_length=10, choices=ZONA_CHOICES, verbose_name='2.2. ÁREA', null=True,
                            blank=True)
    adress = models.CharField(max_length=30, blank=True, verbose_name='2.3. DIRECCIÓN DE VIVIENDA',null=True)
    adress2 = models.CharField(max_length=30, blank=True, verbose_name='2.4. DIRECCIÓN DE CORRESPONDENCIA',null=True)
    phone = models.CharField(max_length=30, blank=True, verbose_name='2.5. TELÉFONO', null=True)
    phone_movil = models.CharField(max_length=30, blank=True, verbose_name='2.6. CELULAR ', null=True)
    email = models.EmailField(max_length=30, blank=True, verbose_name='2.7. E-MAIL', null=True)
    web = models.EmailField(max_length=30, blank=True, verbose_name='2.8. PÁGINA WEB', null=True)
    desarrollo_practica= models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='3.1. ¿ACTUALMENTE DESARROLLA ALGUNA PRÁCTICA ARTÍSTICA?', null=True,
                            blank=True)
    forma_practica = models.CharField(max_length=50, choices=FORMAPRACTICA_CHOICES,
                                           verbose_name='3.2. DESARROLLA LA PRÁCTICA ARTÍSTICA DE FORMA', null=True,
                                           blank=True)
    area2 = MultiSelectField(verbose_name='3.3. ÁREA ARTÍSTICA QUE PRACTICA', choices=AGENTEAREA_CHOICES, blank=True, null=True)

    practica = MultiSelectField(verbose_name='3.4. PRÁCTICA ARTÍSTICA', choices=AGENTEPRACTICA_CHOICES, blank=True,
                             null=True)
    cual_practica = models.CharField(max_length=30, blank=True, verbose_name='3.4. ¿CUÁL?', null=True)
    pertenece_entidad = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                           verbose_name='3.5. ¿PERTENECE A UNA ORGANIZACIÓN ARTÍSTICA O CULTURAL?',
                                           null=True,
                                           blank=True)
    vinculacion_entidad = models.DateField(verbose_name='3.6. ¿DESDE QUÉ AÑO ESTÁ VINCULADO A LA ORGANIZACIÓN ARTÍSTICA O CULTURAL?', auto_now=False, editable=True,
                                          blank=True,
                                          null=True)
    name_entity = models.CharField(max_length=30, blank=True, verbose_name='3.7. NOMBRE DE LA ORGANIZACIÓN ARTÍSTICA O CULTURAL', null=True)
    tipo_formacion = models.CharField(max_length=40, choices=MODALIDAD_CHOICES,
                                 verbose_name='3.8. ¿QUÉ TIPO DE FORMACIÓN HA RECIBIDO?:', null=True,
                                 blank=True)
    nivel_educacion = MultiSelectField(verbose_name='3.9. NIVEL DE EDUCACIÓN', choices=NIVELEDUCACION_CHOICES, blank=True,
                                null=True)

    titulo = models.CharField(max_length=30, blank=True, verbose_name='3.10.TÍTULO RECIBIDO', null=True)
    ano_titulo = models.DateField(verbose_name='3.11. AÑO ', auto_now=False, editable=True,
                                           blank=True,
                                           null=True)
    entidad_educativa = models.CharField(max_length=60, blank=True, verbose_name='3.12. NOMBRE DE ENTIDAD EDUCATIVA', null=True)
    reseña_trayectoria = models.TextField(max_length=2000, blank=True,
                                     verbose_name='3.13. RESEÑA TRAYECTORIA ARTÍSTICA',null=True)
    tipo_vivienda = models.CharField(max_length=40, choices=ESPACIO_CHOICES,
                                      verbose_name='4.1. LA VIVIENDA QUE HABITA ES:', null=True,
                                      blank=True)
    housing_stratum = models.ForeignKey(HousingStratum, verbose_name='4.2. ESTRATO DE LA VIVIENDA', on_delete=models.PROTECT,
                                        blank=True, null=True)
    tipo_vinculacion = models.CharField(max_length=40, choices=TIPOVINCULACION_CHOICES,
                                     verbose_name='4.3. ¿TIPO DE VINCULACIÓN EN LA ACTIVIDAD ARTÍSTICA Y CULTURAL?:', null=True,
                                     blank=True)
    cual_vinculacion = models.CharField(max_length=40,
                                      verbose_name='4.3.1. ¿CUÁL TIPO DE VINCULACIÓN?:', null=True,
                                      blank=True)
    otra_actividad = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='4.4. ¿DESARROLLA OTRA ACTIVIDAD PRODUCTIVA DIFERENTE A LA ARTÍSTICA Y CULTURAL?', null=True,
                            blank=True)
    fuente_ingreso = MultiSelectField(verbose_name='4.5. FUENTES DE INGRESO', choices=FUENTEINGRESO_CHOICES,
                                       blank=True,
                                       null=True)
    porcentaje = models.IntegerField(max_length=30, verbose_name='4.6. ¿QUÉ PORCENTAJE DE SUS INGREOS PROVIENEN DE LA ACTIVIDAD ARTÍSTICA Y CULTURAL?', blank=True, null=True)
    regimen_salud = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                         verbose_name='4.7. SE ENCUENTRA ACTUALMENTE AFILIADO AL RÉGIMEN DE SEGURIDAD SOCIAL EN SALUD?',
                                         null=True,
                                         blank=True)
    health_regimen = models.ForeignKey(HealthRegimen, verbose_name='4.8.  A QUE RÉGMIEN DE SALUD', on_delete=models.PROTECT,
                                       blank=True, null=True)
    regimen_pension = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                     verbose_name='4.9. ¿SE ENCUENTRA ACTUALMENTE AFILIADO AL RÉGIMEN DE SEGURIDAD SOCIAL EN PENSIONES?',
                                     null=True,
                                     blank=True)
    pension_regimen = models.ForeignKey(PensionRegimen, verbose_name='4.10. A QUE RÉGIMEN DE PENSIÓN', on_delete=models.PROTECT,
                                        blank=True, null=True)
    regimen_arl = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                       verbose_name='4.11. ¿SE ENCUENTRA ACTUALMENTE AFILIADO AL RÉGIMEN DE RIESGOS PROFESIONALES?:',
                                       null=True,
                                       blank=True)
    vigia_patrimonio = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='VIGIA PATRIMONIO',
                                        null=True, blank=True)
    portador_manifestacion = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                              verbose_name='PORTADOR DE MANIFESTACIÓN PATRIMONIO', null=True,
                                              blank=True)
    manifestation = models.ForeignKey(Manifestation, verbose_name='MANIFESTACIÓN', on_delete=models.PROTECT, blank=True,
                                      null=True)
    servicios=models.TextField(max_length=2000,
                                              verbose_name='Servicios que ofreces', null=True,
                                              blank=True)
    facebook=models.CharField(max_length=200,verbose_name='Facebook', null=True,
                                              blank=True)
    instagram = models.CharField(max_length=200, verbose_name='Instagram', null=True,
                                blank=True)

    sisben = models.FileField(verbose_name='Sisben', upload_to='agent/file', blank=True, null=True)
    beps = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='Tiene BEPS?', null=True,
                            blank=True)
    terminosycondiciones = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                            verbose_name='Acepta terminos y condiciones', null=True,
                                            blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Agente cultural'
        verbose_name_plural = 'Agente Cultural'


"""entidades"""
class Regimen(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='TIpo de Regimen')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Regimen'
        verbose_name_plural = 'Regimen'
class Subregimen(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de Subregimen')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subregimen'
        verbose_name_plural = 'Subregimen'

class Naturaleza(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='TIpo de Naturaleza')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Naturaleza'
        verbose_name_plural = 'Naturaleza'

class Caracterentidad(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de Caracter de la entidad')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Caracter de la entidad'
        verbose_name_plural = 'Caracter de la entidad'



class NivelEntidad(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Niveles')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Nivel de entidad'
        verbose_name_plural = 'Niveles de entidad'

class Entidad(models.Model):
    user = models.OneToOneField(User,verbose_name='Registrador de la entidad', on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(verbose_name='1.1. NOMBRE:', max_length=254, blank=True, null=True)
    sigla = models.CharField(verbose_name='1.2. SIGLA:', max_length=254, blank=True, null=True)
    nit = models.CharField(verbose_name='1.3. NIT:', max_length=10, blank=True, null=True)
    date = models.DateField(verbose_name='1.4. AÑO DE CONSTITUCIÓN',auto_now=False,editable=True,blank=True,null=True)
    reseña = models.TextField(verbose_name='1.5. RESEÑA', blank=True, null=True)
    nombre_representante = models.CharField(verbose_name='1.6. NOMBRES DEL REPRESENTANTE LEGAL: ', max_length=254, blank=True, null=True)
    apellidos_representante = models.CharField(verbose_name='1.7. APELLIDOS DEL REPRESENTANTE LEGAL', max_length=254, blank=True, null=True)
    cargo_representante = models.CharField(verbose_name='1.8. CARGO DEL REPRESENTANTE', max_length=254, blank=True, null=True)
    vinculacion_representante = models.DateField(verbose_name='1.9. AÑO DE VINCULACIÓN', auto_now=False, editable=True, blank=True,
                                   null=True)
    type_document = models.ForeignKey(TypeDocument, verbose_name='1.10. TIPO DOCUMENTO IDENTIDAD:', on_delete=models.PROTECT,
                                      blank=True, null=True)
    identification = models.IntegerField(max_length=30, verbose_name='1.11. NÚMERO DE DOCUMENTO', blank=True, null=True)
    lugar_expedicion = models.CharField(verbose_name='1.12. LUGAR DE EXPEDICIÓN:', max_length=10, blank=True, null=True)
    nombre_contacto = models.CharField(verbose_name='1.13. NOMBRES DEL CONTACTO:', max_length=254, blank=True, null=True)
    apellidos_contacto = models.CharField(verbose_name='1.14. APELLIDOS DEL CONTACTO:', max_length=254, blank=True, null=True)
    cargo = models.CharField(verbose_name='1.15. CARGO DEL CONTACTO:', max_length=254, blank=True, null=True)
    vinculacion = models.DateField(verbose_name='1.16. AÑO DE VINCULACIÓN:', auto_now=True, editable=False, blank=True, null=True)
    state = models.ForeignKey(Region, verbose_name='2.DEPARTAMENTO', on_delete=models.PROTECT, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='2.1. MUNICIPIO', on_delete=models.PROTECT, blank=True, null=True)
    zona = models.CharField(max_length=10, choices=ZONA_CHOICES, verbose_name='2.2. ÁREA', null=True,
                            blank=True)
    direccion = models.CharField(verbose_name='2.3. DIRECCIÓN', max_length=254, blank=True, null=True)
    correspondencia = models.CharField(verbose_name='2.4. DIRECCIÓN CORRESPONDENCIA:', max_length=254, blank=True, null=True)
    phone_movil = models.CharField(max_length=30, blank=True, verbose_name='2.5. TELEFONO:', null=True)
    phone = models.CharField(max_length=30, blank=True, verbose_name='2.6. FAX',  null=True)
    apartado_aereo = models.CharField(max_length=30, blank=True, verbose_name='2.7. APARTADO AÉREO',null=True)
    email = models.EmailField(max_length=30, blank=True, verbose_name='2.8. E-MAIL:',null=True)
    pagina_web = models.CharField(max_length=30, blank=True, verbose_name='2.9. PÁGINA WEB:',null=True)
    practica = MultiSelectField(max_length=82, choices=PRACTICA_CHOICES,
                                      verbose_name='3.1. PRÁCTICA ARTÍSTICA:',
                                      null=True,
                                      blank=True)
    formacion = models.ForeignKey(FormacionE, verbose_name='3.2. FORMACIÓN',
                                on_delete=models.PROTECT, blank=True,
                                null=True)
    tipo_produccion = MultiSelectField(max_length=82, choices=TIPO_CHOICES,
                                verbose_name='3.3. PRODUCCIÓN, COMERCIALIZACIÓN Y DIVULGACIÓN: ',
                                null=True,
                                blank=True)

    personeria = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='3.4. TIENE PERSONERÍA JURÍDICA:', null=True,
                            blank=True)
    naturaleza = models.ForeignKey(Naturaleza, verbose_name='3.5. NATURALEZA:', on_delete=models.PROTECT, blank=True, null=True)
    caracter_entidad = models.ForeignKey(Caracterentidad, verbose_name='3.6. CARÁCTER DE LA ENTIDAD:', on_delete=models.PROTECT, blank=True,
                                   null=True)
    objeto_social = models.TextField(max_length=2000, blank=True,
                                     verbose_name='3.7. OBJETO SOCIAL')
    regimen = models.ForeignKey(Regimen, verbose_name='3.8. TIPO DE REGIMEN',
                                         on_delete=models.PROTECT, blank=True,
                                         null=True)
    subregimen = models.ForeignKey(Subregimen, verbose_name='3.9. SUBREGIMEN:',
                                on_delete=models.PROTECT, blank=True,
                                null=True)
    dependencia=models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='3.10. DEPENDE DE ALGUNA ENTIDAD:', null=True,
                            blank=True)
    entidad_dependiente = models.CharField(max_length=30, blank=True, verbose_name='3.11. NOMBRE DE LA ENTIDAD:')
    nivel = models.CharField(max_length=22, choices=NIVEL_CHOICES, verbose_name=' 3.12. NIVEL:', null=True, blank=True)
    red = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='3.13. LA ENTIDAD PERTENECE A ALGUNA RED?:',
                                   null=True,
                                   blank=True)
    name_red = models.CharField(max_length=30, blank=True, verbose_name='3.14. NOMBRE DE LA RED:',null=True)
    nivel_red = models.CharField(max_length=22, choices=NIVEL_CHOICES, verbose_name='3.15. NIVEL:', null=True, blank=True)
    acceso_internet = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='4.1. ¿TIENE LA ORGANIZACIÓN ACCESOS A INTERNET?',
                           null=True,
                           blank=True)
    espacio = models.CharField(max_length=22, choices=ESPACIO_CHOICES,
                                       verbose_name='4.2. ESPACIO',
                                       null=True,
                                       blank=True)
    infraestructura_discapacitados = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                       verbose_name='4.3. CUENTA LA ENTIDAD CON INFRAESTRUCTURA PARA DISCAPACITADOS:',
                                       null=True,
                                       blank=True)
    interes_cultural = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                                      verbose_name='4.4. OCUPA LA ENTIDAD UN BIEN DE INTERÉS CULTURAL:',
                                                      null=True,
                                                      blank=True)

    nivel_interescultural = models.CharField(max_length=22, choices=NIVEL_CHOICES, verbose_name='4.5. ¿NIVEL DEL BIEN DE INTERES CULTURAL QUE OCUPA?', null=True,
                                 blank=True)

    espacios_actividades = MultiSelectField(max_length=29, choices=ESPACIOACTIVIDADES_CHOICES, verbose_name='4.6. ESPACIOS DISPONIBLES POR LA ORGANIZACIÓN PARA EL DESARROLLO DE SUS ACTIVIDADES', null=True,
                                 blank=True)
    genero_empleo = models.CharField(max_length=22, choices=BOOLEAN_CHOICES,
                                        verbose_name='5.1. ¿SU ORGANIZACIÓN GENERÓ EMPLEO DIRECTO EL ÚLTIMO AÑO?:',
                                        null=True,
                                        blank=True)
    tipo_empleo = models.CharField(max_length=22, choices=BOOLEAN_CHOICES,
                                     verbose_name='5.2. ¿QUÉ TIPO DE EMPLEO DIRECTO GENERÓ?:',
                                     null=True,
                                     blank=True)
    cantidad_noremunerado = models.IntegerField(max_length=22,
                                     verbose_name='5.3. ¿CUÁNTOS EMPLEOS NO REMUNERADOS GENERÓ?:',
                                     null=True,
                                     blank=True)
    duracion_noremunerados= models.CharField(max_length=22, choices=DURACION_CHOICES,
                                   verbose_name='5.4. ¿QUÉ DURACIÓN TUVIERON LOS EMPLEOS NO REMUNERADOS QUE GENERÓ?:',
                                   null=True,
                                   blank=True)
    cantidad_remunerado = models.IntegerField(max_length=22,
                                                verbose_name='5.5. ¿CUÁNTOS EMPLEOS REMUNERADOS GENERÓ?:',
                                                null=True,
                                                blank=True)
    duracion_remunerados = models.CharField(max_length=22, choices=DURACION_CHOICES,
                                              verbose_name='5.6. ¿QUÉ DURACIÓN TUVIERON LOS EMPLEOS REMUNERADOS QUE GENERÓ?:',
                                              null=True,
                                              blank=True)
    cantidadremunerado_ops = models.IntegerField(max_length=22,
                                              verbose_name='5.7. ¿CUÁNTOS EMPLEOS REMUNERADOS GENERÓ POR CONTRATOS DE SERVICIOS?:',
                                              null=True,
                                              blank=True)
    cantidadremunerado_laboral = models.IntegerField(max_length=22,
                                                 verbose_name='5.8. ¿CUÁNTOS EMPLEOS REMUNERADOS GENERÓ POR CONTRATO LABORAL?:',
                                                 null=True,
                                                 blank=True)
    cantidadrecurso_humano = models.IntegerField(max_length=22,
                                                     verbose_name='5.9. ¿CANTIDAD DE RECURSO HUMANO CON EL QUE CUENTA LA ENTIDAD?:',
                                                     null=True,
                                                     blank=True)
    actividad_principal = models.CharField(max_length=42, choices=ACTIVIDAD_CHOICES,
                                            verbose_name='6.1. EL CAMPO DE LA PRINCIPAL ACTIVIDAD ARTÍSTICA O CULTURAL QUE DESARROLLA LA ORGANIZACIÓN ES',
                                            null=True,
                                            blank=True)
    otra_actividad = models.CharField(max_length=42, choices=ACTIVIDAD_CHOICES,
                                           verbose_name='6.2. OTROS CAMPOS DE ACTIVIDADES EN QUE TRABAJA LA ORGANIZACIÓN SON:',
                                           null=True,
                                           blank=True)
    area_artistica = MultiSelectField(max_length=82, choices=AREA_CHOICES,
                                      verbose_name='6.3. EL ÁREA ARTÍSTICA EN LA QUE LA ORGANIZACIÓN DESARROLLA SU PRINCIPAL ACTIVIDAD ES:',
                                      null=True,
                                      blank=True)
    numero_obras = models.IntegerField(max_length=80,
                                                 verbose_name='6.4. ¿NÚMERO DE OBRAS PRODUCIDAS DURANTE EL ÚLTIMO AÑO, COMO EL RESULTADO DE LA PRÁCTICA ARTÍSTICA QUE DESARROLLA LA ORGANIZACIÓN?',
                                                 null=True,
                                                 blank=True)

    practicas = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                        verbose_name='6.5. ¿LAS PRÁCTICAS ASTÍSTICAS QUE REALIZA LA ORGANIZACIÓN INCLUYEN ACTIVIDADES DE FORMACIÓN DE PÚBLICOS? ',
                                        null=True,
                                        blank=True)
    ultimo_año = models.CharField(max_length=22, choices=CARACTER_CHOICES,
                              verbose_name=' 6.6. DURANTE EL ÚLTIMO AÑO EL PROMEDIO MENSUAL APROXIMADO DE PERSONAS (PÚBLICO) QUE ASISTIERON A LA ACTIVIDAD ARTÍSTICA O CULTURAL DE LA ORGANIZACIÓ FUE: ',
                              null=True,
                              blank=True)
    acceso = models.CharField(max_length=22, choices=CARACTER_CHOICES,
                                 verbose_name=' 6.7. EL ACCESO DEL PÚBLICO AL RESULTADO DE LA PRÁCTICA ARTÍSTICA QUE DESARROLLA LA ORGANIZACIÓN ES DE CARÁCTER ',
                                 null=True,
                                 blank=True)
    proyectos = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                 verbose_name=' 6.8. ¿LA ENTIDAD ORGANIZA REGULARMENTE PROGRAMAS O PROYECTOS ENFOCADOS ESPECÍFICAMENTE A ATENDER NIÑOS , JÓVENES, ADULTOS O PERSONAS MAYORES?',
                                 null=True,
                                 blank=True)
    grupos_edad = MultiSelectField(max_length=22, choices=EDAD_CHOICES,
                              verbose_name='6.9. ¿HACIA CUÁLES GRUPOS DE EDAD SE ENFOCAN ESOS PROGRAMAS O PROYECTOS?',
                              null=True,
                              blank=True)
    grupos_poblacion = MultiSelectField(max_length=22, choices=EDAD_CHOICES,
                                   verbose_name='6.10. ¿A QUE GRUPO PERTENECE LA POBLACIÓN BENEFICIARÍA DE LA PRODUCCIÓN ARTISTÍCA Y CULTURAL DE LA ORGANIZACIÓN?',
                                   null=True,
                                   blank=True)
    organizacion_actividades = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                 verbose_name='6.11. ¿DESARROLLA LA ORGANIZACIÓN ACTIVIDADES DIRIGIDAS A MINORÍAS ÉTNICAS?',
                                 null=True,
                                 blank=True)
    etnico = models.ForeignKey(GroupEtnico, verbose_name='6.12. ¿HACÍA CUALES MINORÍAS ÉTNICAS SE ENFOCAN ESTOS PROGRAMAS O PROYECTOS?', on_delete=models.PROTECT, blank=True,
                               null=True)
    personas_discapacidad = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                                verbose_name='6.13. ¿DESARROLLA LA ORGANIZACIÓN ACTIVIDADES ESPECÍFICAMENTE DIRIGIDAS A PERSONAS CON DISCAPACIDAD?',
                                                null=True,
                                                blank=True)

    imparte_formacion = MultiSelectField(max_length=82, choices=AREA_CHOICES,
                                      verbose_name='7.1.  ¿ÁREAS ARTÍSTICAS EN LAS QUE IMPARTE FORMACIÓN?',
                                      null=True,
                                      blank=True)
    modalidad = models.CharField(max_length=82, choices=MODALIDAD_CHOICES,
                                 verbose_name='7.2.  PRINCIPAL MODALIDAD DE FORMACIÓN QUE IMPARTE LA ORGANIZACIÓN',
                                 null=True,
                                 blank=True)
    terminosycondiciones = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='Acepta terminos y condiciones', null=True,
                            blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
