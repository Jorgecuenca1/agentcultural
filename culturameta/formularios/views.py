from django.shortcuts import render, redirect

# Create your views here.
from .models import Pqrsd, Tiposolicitud, TypeDocument, Nivel, EncuestaTransparencia


def pqrsd(request):
    tipodocumentos = TypeDocument.objects.all().values('id', 'name')
    tiposolicituds = Tiposolicitud.objects.all().values('id', 'name')
    if request.method == 'POST':
        country = Pqrsd()
        country.name = request.POST['name']
        country.last_name = request.POST['last_name']
        country.identification = request.POST['cedula']
        country.email = request.POST['correo_electronico']
        country.phone = request.POST['phone_number']
        country.asunto = request.POST['asunto']
        country.solicitud = request.POST['solicitud']
        tipodocumento = TypeDocument.objects.get(id=request.POST['tipodocumento'])
        country.type_document = tipodocumento
        tiposolicitud = TypeDocument.objects.get(id=request.POST['tiposolicitud'])
        country.typosolicitud = tiposolicitud

        country.save()
        return redirect(f'/users/pqrsd')
    return render(request, 'users/pqrsd.html',{'tiposolicituds': tiposolicituds,'tipodocumentos':tipodocumentos})

def encuestatransparencia(request):
    nivels = Nivel.objects.all().values('id', 'name')

    if request.method == 'POST':
        country = EncuestaTransparencia()
        country.encontro = request.POST['encontro']
        country.noencontro = request.POST['noencontro']
        country.facil = request.POST['facil']
        nivel = Nivel.objects.get(id=request.POST['nivel'])
        country.nivel = nivel
        country.sugerencia = request.POST['sugerencia']

        country.save()
        return redirect(f'/users/encuestatransparencia')
    return render(request, 'users/encuestatransparencia.html',{'nivels': nivels,})