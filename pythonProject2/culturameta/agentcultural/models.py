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
        ('Musica ', 'Musica '),
        ('Teatro', 'Teatro'),
        ('Bibiliotecas', 'Bibiliotecas'),
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
        ('Lenguas, lenguajes y tradicion oral', 'Lenguas, lenguajes y tradicion oral'),
        ('Medicina tradicional', 'Medicina tradicional'),
        ('PCI asociado a espacios culturales', 'PCI asociado a espacios culturales'),
        ('PCI asociado a los evenos de la vida cotidiana', 'PCI asociado a los evenos de la vida cotidiana'),
        ('Produccion tradicional y propia', 'Produccion tradicional y propia'),
        ('Sistemas normativos y formas de organizacion social tradicionales', 'Sistemas normativos y formas de organizacion social tradicionales'),
        ('Técnicas y tradicionales asociadas a la fabricación de objetos artesanales','Técnicas y tradicionales asociadas a la fabricación de objetos artesanales'),
        ('Museos patrimoniales', 'Museos patrimoniales'),

    )
NIVEL_CHOICES = (
        ('INTERNACIONAL', 'INTERNACIONAL'),
        ('NACIONAL', 'NACIONAL'),
        ('DEPARTAMENTAL', 'DEPARTAMENTAL'),
        ('MUNICIPAL', 'MUNICIPAL'),

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
    name = models.CharField(max_length=30, blank=True, verbose_name='TIpo de Discapacidad')

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

    image = models.ImageField(verbose_name='Imagen del agente', upload_to='agent/image',blank=True,null=True)
    tipo = models.CharField(max_length=17, choices=AGENTE_CHOICES, verbose_name='Agente o Gestor Cultural', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT, blank=True, null=True)
    type_document = models.ForeignKey(TypeDocument,verbose_name='TIpode documento',on_delete=models.PROTECT,blank=True,null=True)
    identification = models.IntegerField(max_length=30,verbose_name='Número de identificación',blank=True,null=True )
    name = models.CharField(max_length=30, blank=True, verbose_name='Primer Nombre', null=True)
    other_name = models.CharField(max_length=30, blank=True, verbose_name='Otros Nombres', null=True)
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Primer apellido', null=True)
    last_name2 = models.CharField(max_length=30, blank=True, verbose_name='Segundo apellido', null=True)
    artistic_name = models.CharField(max_length=30, blank=True, verbose_name='Nombre artistico', null=True)
    birthday = models.DateField(verbose_name='Fecha de nacimiento',auto_now=True,editable=False,blank=True,null=True)
    gender = models.ForeignKey(Genero,verbose_name='Genero', on_delete=models.PROTECT,blank=True,null=True)
    etnico = models.ForeignKey(GroupEtnico, verbose_name='Grupo etnico', on_delete=models.PROTECT,blank=True,null=True)
    disability = models.ForeignKey(Disability, verbose_name='Discapacidad', on_delete=models.PROTECT,blank=True,null=True)
    population_group = models.ForeignKey(PopulationGroup, verbose_name='Grupo poblacional', on_delete=models.PROTECT,blank=True,null=True)
    rut = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='RUT', null=True, blank=True)
    code_rut = models.CharField(max_length=30, blank=True, verbose_name='RUT')
    country = models.ForeignKey(Country, verbose_name='País', on_delete=models.CASCADE, blank=True, null=True)
    state = models.ForeignKey(Region, verbose_name='Departamento', on_delete=models.PROTECT, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Municipio', on_delete=models.PROTECT, blank=True, null=True)
    zone = models.ForeignKey(Zone, verbose_name='Centro poblado', on_delete=models.PROTECT, blank=True, null=True)
    adress = models.CharField(max_length=30, blank=True, verbose_name='Direccion')
    zona = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='Zona(rural-urbana)', null=True, blank=True)
    beps = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='Tiene BEPS?', null=True,
                            blank=True)
    housing_stratum = models.ForeignKey(HousingStratum, verbose_name='Estrato vivienda', on_delete=models.PROTECT,blank=True,null=True)
    phone_movil = models.CharField(max_length=30, blank=True, verbose_name='telefono movil', null=True)
    phone = models.CharField(max_length=30, blank=True, verbose_name='telefono', null=True)
    email = models.EmailField(max_length=30, blank=True, verbose_name='Email', null=True)
    health_regimen = models.ForeignKey(HealthRegimen, verbose_name='Regimen de salud', on_delete=models.PROTECT,blank=True,null=True)
    pension_regimen = models.ForeignKey(PensionRegimen, verbose_name='Regimen de pension', on_delete=models.PROTECT,blank=True,null=True)
    monthly_income  = models.ForeignKey(MonthlyIncome, verbose_name='Ingresos mensuales', on_delete=models.PROTECT,blank=True,null=True)
    sector = MultiSelectField(verbose_name='Sector',choices =SECTOR_CHOICES, blank=True,null=True)
    area2= MultiSelectField(verbose_name='Area',choices =AREA_CHOICES, blank=True,null=True)

    activity = models.ForeignKey(Activity, verbose_name='Activity', on_delete=models.PROTECT,blank=True,null=True)
    vigia_patrimonio = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='Vigia patrimonio', null=True, blank=True)
    portador_manifestacion = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='Portador de manifestacion patrimonio', null=True, blank=True)
    manifestation =models.ForeignKey(Manifestation, verbose_name='Manifestacion', on_delete=models.PROTECT,blank=True,null=True)
    formacion = models.ForeignKey(Formacion,verbose_name='Formacion', on_delete=models.PROTECT,blank=True,null=True)
    mas_formacion= models.TextField(max_length=500, blank=True, verbose_name='Describa si tiene mas formacion en un texto')
    experiencia = models.TextField(max_length=2000, blank=True,
                                     verbose_name='Describa su experiencia')
    archivo = models.FileField( null=True, blank=True)
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
    name = models.CharField(verbose_name='Nombre Entidad', max_length=254, blank=True, null=True)
    sigla = models.CharField(verbose_name='Sigla', max_length=254, blank=True, null=True)
    nit = models.CharField(verbose_name='NIt', max_length=10, blank=True, null=True)
    date = models.DateField(verbose_name='Año de constitución',auto_now=True,editable=False,blank=True,null=True)
    reseña = models.TextField(verbose_name='Reseña', blank=True, null=True)
    nombre_representante = models.CharField(verbose_name='Nombre Representante legal', max_length=254, blank=True, null=True)
    apellidos_representante = models.CharField(verbose_name='Apellidos Representante legal', max_length=254, blank=True, null=True)
    type_document = models.ForeignKey(TypeDocument, verbose_name='TIpode documento', on_delete=models.PROTECT,
                                      blank=True, null=True)
    identification = models.IntegerField(max_length=30, verbose_name='Número de identificación', blank=True, null=True)
    lugar_expedicion = models.CharField(verbose_name='Lugar de expendición', max_length=10, blank=True, null=True)
    nombre_contacto = models.CharField(verbose_name='Nombre de contacto', max_length=254, blank=True, null=True)
    apellidos_contacto = models.CharField(verbose_name='Apellidos del contacto', max_length=254, blank=True, null=True)
    cargo = models.CharField(verbose_name='Cargo', max_length=254, blank=True, null=True)
    vinculacion = models.DateField(verbose_name='Año de vinculación', auto_now=True, editable=False, blank=True, null=True)
    state = models.ForeignKey(Region, verbose_name='Departamento', on_delete=models.PROTECT, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Municipio', on_delete=models.PROTECT, blank=True, null=True)
    zone = models.ForeignKey(Zone, verbose_name='Centro poblado', on_delete=models.PROTECT, blank=True, null=True)
    zona = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='Zona(rural-urbana)', null=True,
                            blank=True)
    direccion = models.CharField(verbose_name='Direccion', max_length=254, blank=True, null=True)
    correspondencia = models.CharField(verbose_name='Direccion de correspondencia', max_length=254, blank=True, null=True)
    phone_movil = models.CharField(max_length=30, blank=True, verbose_name='telefono movil', null=True)
    phone = models.CharField(max_length=30, blank=True, verbose_name='telefono',  null=True)
    apartado_aereo = models.CharField(max_length=30, blank=True, verbose_name='Apartado aereo',null=True)
    email = models.EmailField(max_length=30, blank=True, verbose_name='Email',null=True)
    pagina_web = models.CharField(max_length=30, blank=True, verbose_name='Pagina Web',null=True)
    practica = MultiSelectField(max_length=82, choices=PRACTICA_CHOICES,
                                      verbose_name='PRACTICA:',
                                      null=True,
                                      blank=True)
    formacion = models.ForeignKey(FormacionE, verbose_name='Formación',
                                on_delete=models.PROTECT, blank=True,
                                null=True)
    tipo_produccion = MultiSelectField(max_length=82, choices=TIPO_CHOICES,
                                verbose_name='Producción, Comercialización Y Divulgación: ',
                                null=True,
                                blank=True)

    personeria = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='Tiene personería jurídica?', null=True,
                            blank=True)
    naturaleza = models.ForeignKey(Naturaleza, verbose_name='Naturaleza', on_delete=models.PROTECT, blank=True, null=True)
    caracter_entidad = models.ForeignKey(Caracterentidad, verbose_name='Caracter de la entidad', on_delete=models.PROTECT, blank=True,
                                   null=True)
    regimen = models.ForeignKey(Regimen, verbose_name='Tipo de Regimen',
                                         on_delete=models.PROTECT, blank=True,
                                         null=True)
    subregimen = models.ForeignKey(Subregimen, verbose_name='Tipo de Subregimen',
                                on_delete=models.PROTECT, blank=True,
                                null=True)
    dependencia=models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='Depende de alguna entidad', null=True,
                            blank=True)
    entidad_dependiente = models.CharField(max_length=30, blank=True, verbose_name='Nombre de la entidad')
    nivel = models.CharField(max_length=22, choices=NIVEL_CHOICES, verbose_name=' Nivel de la entidad', null=True, blank=True)
    red = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='La entidad pertenece alguna red?',
                                   null=True,
                                   blank=True)
    name_red = models.CharField(max_length=30, blank=True, verbose_name='Nombre de la red',null=True)
    nivel_red = models.CharField(max_length=22, choices=NIVEL_CHOICES, verbose_name='Nivel de la red', null=True, blank=True)
    acceso_internet = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='Tiene la organización acceso a internet?',
                           null=True,
                           blank=True)
    espacio = models.CharField(max_length=22, choices=ESPACIO_CHOICES,
                                       verbose_name='Espacio',
                                       null=True,
                                       blank=True)
    infraestructura_discapacitados = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                       verbose_name='Cuenta la entidad con infraestructura para discapacitados?',
                                       null=True,
                                       blank=True)
    interes_cultural = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                                      verbose_name='Ocupa la entidad un bien de interés cultural?',
                                                      null=True,
                                                      blank=True)

    nivel_interescultural = models.CharField(max_length=22, choices=NIVEL_CHOICES, verbose_name='Nivel del bien de interes cultural que ocupa?', null=True,
                                 blank=True)

    espacios_actividades = MultiSelectField(max_length=29, choices=ESPACIOACTIVIDADES_CHOICES, verbose_name='Espacio disponibles por la organización para el desarrollo de sus actividades', null=True,
                                 blank=True)
    genero_empleo = models.CharField(max_length=22, choices=BOOLEAN_CHOICES,
                                        verbose_name='Su organización generó empleo directo el último año?',
                                        null=True,
                                        blank=True)
    tipo_empleo = models.CharField(max_length=22, choices=BOOLEAN_CHOICES,
                                     verbose_name='Que tipo de empleo directo generó?',
                                     null=True,
                                     blank=True)
    cantidad_noremunerado = models.IntegerField(max_length=22,
                                     verbose_name='Cuántos empleos no remunerados generó?',
                                     null=True,
                                     blank=True)
    duracion_noremunerados= models.CharField(max_length=22, choices=DURACION_CHOICES,
                                   verbose_name='Qué duración tuvieron los empleos no remunerados que generó?',
                                   null=True,
                                   blank=True)
    cantidad_remunerado = models.IntegerField(max_length=22,
                                                verbose_name='Cuántos empleos remunerados generó?',
                                                null=True,
                                                blank=True)
    duracion_remunerados = models.CharField(max_length=22, choices=DURACION_CHOICES,
                                              verbose_name='Qué duración tuvieron los empleos remunerados que generó?',
                                              null=True,
                                              blank=True)
    cantidadremunerado_ops = models.IntegerField(max_length=22,
                                              verbose_name='Cuántos empleos remunerados generó por contratos de servicios?',
                                              null=True,
                                              blank=True)
    cantidadremunerado_laboral = models.IntegerField(max_length=22,
                                                 verbose_name='Cuántos empleos remunerados generó por contrato laboral?',
                                                 null=True,
                                                 blank=True)
    cantidadrecurso_humano = models.IntegerField(max_length=22,
                                                     verbose_name='Cantidad de recurso humano con el que cuenta la entidad?',
                                                     null=True,
                                                     blank=True)
    actividad_principal = models.CharField(max_length=42, choices=ACTIVIDAD_CHOICES,
                                            verbose_name=' EL CAMPO DE LA PRINCIPAL ACTIVIDAD ARTÍSTICA O CULTURAL QUE DESARROLLA LA ORGANIZACIÓN ES',
                                            null=True,
                                            blank=True)
    otra_actividad = models.CharField(max_length=42, choices=ACTIVIDAD_CHOICES,
                                           verbose_name='OTROS CAMPOS DE ACTIVIDADES EN QUE TRABAJA LA ORGANIZACIÓN SON:',
                                           null=True,
                                           blank=True)
    area_artistica = MultiSelectField(max_length=82, choices=AREA_CHOICES,
                                      verbose_name='EL ÁREA ARTÍSTICA EN LA QUE LA ORGANIZACIÓN DESARROLLA SU PRINCIPAL ACTIVIDAD ES:',
                                      null=True,
                                      blank=True)
    numero_obras = models.IntegerField(max_length=80,
                                                 verbose_name='¿NÚMERO DE OBRAS PRODUCIDAS DURANTE EL ÚLTIMO AÑO, COMO EL RESULTADO DE LA PRÁCTICA ARTÍSTICA QUE DESARROLLA LAORGANIZACIÓN?',
                                                 null=True,
                                                 blank=True)

    practicas = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                        verbose_name='¿LAS PRÁCTICAS ASTÍSTICAS QUE REALIZA LA ORGANIZACIÓN INCLUYEN ACTIVIDADES DE FORMACIÓN DE PÚBLICOS? ',
                                        null=True,
                                        blank=True)
    acceso = models.CharField(max_length=22, choices=CARACTER_CHOICES,
                                 verbose_name=' EL ACCESO DEL PÚBLICO AL RESULTADO DE LA PRÁCTICA ARTÍSTICA QUE DESARROLLA LA ORGANIZACIÓN ES DE CARÁCTER ',
                                 null=True,
                                 blank=True)
    proyectos = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                 verbose_name=' ¿LA ENTIDAD ORGANIZA REGULARMENTE PROGRAMAS O PROYECTOS ENFOCADOS ESPECÍFICAMENTE A ATENDER NIÑOS , JO¿ÓVENES, ADULTOS O PERSONAS MAYORES?',
                                 null=True,
                                 blank=True)
    grupos_edad = MultiSelectField(max_length=22, choices=EDAD_CHOICES,
                              verbose_name='¿HACIA CUÁLES GRUPOS DE EDAD SE ENFOCAN ESOS PROGRAMAS O PROYECTOS?',
                              null=True,
                              blank=True)
    grupos_poblacion = MultiSelectField(max_length=22, choices=EDAD_CHOICES,
                                   verbose_name='¿A QUE GRUPO PERTENECE LA POBLACIÓN BENEFICIARÍA DE LA PRODUCCIÓN ARTISTÍCA Y CULTURAL DE LA ORGANIZACIÓN?',
                                   null=True,
                                   blank=True)
    organizacion_actividades = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                 verbose_name='¿DESARROLLA LA ORGANIZACIÓN ACTIVIDADES ESPECÍFICAMENTE DIRIGIDAS A PERSONAS CON DISCAPACIDAD?',
                                 null=True,
                                 blank=True)
    etnico = models.ForeignKey(GroupEtnico, verbose_name='¿HACÍA CUALES MINORÍAS ÉTNICAS SE ENFOCAN ESTOS PROGRAMAS O PROYECTOS?', on_delete=models.PROTECT, blank=True,
                               null=True)
    personas_discapacidad = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                                verbose_name='¿DESARROLLA LA ORGANIZACIÓN ACTIVIDADES ESPECÍFICAMENTE DIRIGIDAS A PERSONAS CON DISCAPACIDAD?',
                                                null=True,
                                                blank=True)

    imparte_formacion = MultiSelectField(max_length=82, choices=AREA_CHOICES,
                                      verbose_name=' ¿AREAS ARTÍSTICAS EN LAS QUE IMPARTE FORMACIÓN?',
                                      null=True,
                                      blank=True)
    modalidad = models.CharField(max_length=82, choices=MODALIDAD_CHOICES,
                                 verbose_name='  PRINCIPAL MODALIDAD DE FORMACIÓN QUE IMPARTE LA ORGANIZACIÓN',
                                 null=True,
                                 blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
