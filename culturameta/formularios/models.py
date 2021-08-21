from django.db import models
# Create your models here.
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

class Propuesta(models.Model):
    name = models.CharField(max_length=120, blank=True, verbose_name='Propuesta')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Propuesta'
        verbose_name_plural = 'Propuesta'

class Modalidad(models.Model):
    name = models.CharField(max_length=120, blank=True, verbose_name='Modalidad')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Modalidad'
        verbose_name_plural = 'Modalidad'
class Tiposolicitud(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de solicitud')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de solicitud'
        verbose_name_plural = 'TIpo de solicitud'



class Nivel(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Nivel')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Nivel'

class TypeDocument(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de documento')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'TIpo de documentos'

class Pqrsd(models.Model):
    tiposolicitud = models.ForeignKey(Tiposolicitud, verbose_name='1.Tipo de solicitud', on_delete=models.PROTECT, blank=True, null=True)

    name = models.CharField(max_length=100, blank=True, verbose_name='2.Nombre del remitente', null=True)
    last_name = models.CharField(max_length=100, blank=True, verbose_name='3.Apellidos del remitente', null=True)
    type_document = models.ForeignKey(TypeDocument, verbose_name='4.Tipo de documento',
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    identification = models.CharField(max_length=30, verbose_name='5.Identificación', blank=True, null=True)

    email = models.EmailField(max_length=30, blank=True, verbose_name='6.Correo electrónico', null=True)
    phone = models.CharField(max_length=30, verbose_name='7.Identificación', blank=True, null=True)
    asunto = models.CharField(max_length=100, blank=True, verbose_name='8.Asunto de solicitud', null=True)
    solicitud = models.TextField(max_length=2000,
                                 verbose_name='9.Descripción Solicitud', null=True,
                                 blank=True)
    archivo = models.FileField(verbose_name='10.Archivo adjunto', upload_to='pqrsd/file', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Informe PQRSD'
        verbose_name_plural = 'Informe PQRSD'


class EncuestaTransparencia(models.Model):
    encontro = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                   verbose_name='1. Encontró la información que buscaba?:',
                                   null=True,
                                   blank=True)
    noencontro= models.CharField(max_length=100, blank=True, verbose_name='2. Si no la encontró especifique en este espacio ¿qué buscaba?', null=True)
    facil = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                verbose_name='3. ¿Le resultó fácil la ruta de acceso a la información?:',
                                null=True,
                                blank=True)
    nivel = models.ForeignKey(Nivel, verbose_name='4. ¿A nivel general, cómo define la información contenida en la página web?',
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    sugerencia = models.CharField(max_length=100, blank=True, verbose_name='5. Si tiene alguna sugerencia escribanos en el siguiente espacio, recuerde que su opinión es muy importante para mejorar nuestro servicio.', null=True)

    def __str__(self):
        return self.sugerencia

    class Meta:
        verbose_name = 'Encuesta de satisfacción'
        verbose_name_plural = 'Encuesta de satisfacción'

class Torneo(models.Model):
    email = models.EmailField(max_length=20, blank=True, verbose_name='Correo *', null=True)
    name = models.CharField(max_length=100, blank=True, verbose_name='Nombres y Aepllidos del integrante de la agrupación que hará las veces de representante (si aplica) y/0 participante: *', null=True)
    agrupacion = models.CharField(max_length=100, blank=True, verbose_name='Nombre de la agrupación (si aplica)', null=True)
    seudonimo = models.CharField(max_length=100, blank=True, verbose_name='Seudónimo (si aplica):', null=True)
    type_document = models.ForeignKey(TypeDocument, verbose_name='Tipo de identificación: *',
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    identification = models.CharField(max_length=100, verbose_name='Número de identificación: *', blank=True, null=True)
    expedicion = models.CharField(max_length=100, verbose_name='Lugar de Expedición: *', blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, verbose_name='País de residencia: *', null=True)
    region = models.CharField(max_length=100, blank=True, verbose_name='Ciudad de residencia: *', null=True)
    city = models.CharField(max_length=100, blank=True, verbose_name='Municipio', null=True)

    adress = models.CharField(max_length=100, blank=True, verbose_name='Dirección residencia:', null=True)
    phone = models.CharField(max_length=100, blank=True, verbose_name='Teléfono fijo:', null=True)
    phone_movil = models.CharField(max_length=100, blank=True, verbose_name='Teléfono celular: *', null=True)
    modalidad = models.ForeignKey(Modalidad, verbose_name='Modalidad en la que participará: *',
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    obra1 = models.CharField(max_length=100, blank=True, verbose_name='Escriba el nombre de la obra N°1 y/o arreglo que presentará al concurso según lo solicitado en las bases: (No Aplica para las modalidades de, Pareja de Baile y Copleros). ', null=True)
    obra2 = models.CharField(max_length=100, blank=True, verbose_name='Escriba el nombre de la obra N°2 y/o arreglo que presentará al concurso según lo solicitado en las bases: (No Aplica para las modalidades de, Pareja de Baile y Copleros).', null=True)
    propuesta = models.ForeignKey(Propuesta, verbose_name='Propuesta: *',
                                  on_delete=models.PROTECT,
                                  blank=True, null=True)
    archivo = models.FileField(verbose_name='Seleccione una foto artística haciendo clic en agregar archivo - Por favor ADJUNTE una fotografía artística digital ya sea a color o blanco y negro tamaño mínimo 800 x 600 Pixeles en una resolución mínima de 200 dpi.', upload_to='torneo/file', blank=True, null=True)
    archivo1 = models.FileField(verbose_name='Cargar el Formulario N°1 - Inscripción al 53° Torneo Internacional del Joropo "MIGUEL ÁNGEL MARTÍN" totalmente diligenciado con los siguientes documentos: Fotocopias de la Cédula ciudadanía, extranjería y/o pasaporte del representante y de los integrantes según sea la modalidad y la certificación de residencia de mínimo 3 años emitida por la Alcaldía del municipio respectivo, o las juntas de acción comunal. (aplica solo para los participantes que se presenten por el departamento del Meta). Lo anterior se Adjunta en un solo archivo en formato PDF. *', upload_to='torneo/file', blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, verbose_name='Adjuntar el link del archivo de wetranfer donde envia el audio formato punto wav, mp3 etc... y vídeo y/o videos (mínimo una cámara máximo tres cámaras grabando simultáneamente) FHD, 1080p o superior de la propuesta según sea la modalidad seleccionada: *', null=True)
    archivo2 = models.FileField(verbose_name='', upload_to='torneo/file', blank=True, null=True)
    archivo3 = models.FileField(verbose_name=' Los participantes de las modalidades de Conjunto de Música Tradicional llanera y/o Ensambles Nuevos Formatos deberán enviar una breve, pero sólida justificación escrita de su obra, que incluya: Datos de la obra (forma y estilo), intención y/o concepto musical desarrollado y argumentar el ¿Porqué? del repertorio seleccionado. Esta podrá ser utilizada para presentar la obra ante el público por redes y medios de comunicación. Adjuntar el documento en un solo PDF. ', upload_to='torneo/file', blank=True, null=True)
    archivo4 = models.FileField(verbose_name='Los participantes de las modalidades de Golpe Inédito, Pasaje Inédito, Poema Inédito, deberán enviar una (1) copia del texto de la obra, escrita en computador en letra Arial 12, marcada y firmada únicamente con el seudónimo del compositor. Adjuntar el documento en un solo PDF.  ', upload_to='torneo/file', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Torneo del joropo'
        verbose_name_plural = 'Torneo del joropo'
