from django.shortcuts import render, redirect

# Create your views here.
from .forms import TorneoForm, EncuestaTransparenciaForm, PqrsdForm, PresupuestoForm, FilarmonicaForm
from .models import Pqrsd, Tiposolicitud, TypeDocument, Nivel, EncuestaTransparencia, Modalidad, Propuesta, Torneo
def rutaturistica(request):


    return render(request, 'users/rutaturistica.html')
def votar(request):


    return render(request, 'users/votar.html')
def torneo2022(request):


    return render(request, 'users/torneo2022.html')
def chiguire(request):


    return render(request, 'users/chiguire.html')
def exito(request):


    return render(request, 'users/exito.html')
def pqrsd(request):
    if request.method == "POST":
        # update DB
        form = PqrsdForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('https://culturameta.gov.co')
    else:
        # show the form
        form = PqrsdForm()

    context = {'form': form}
    return render(request, 'users/pqrsd.html', context)

def encuestatransparencia(request):
    if request.method == "POST":
        # update DB
        form = EncuestaTransparenciaForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('https://culturameta.gov.co')
    else:
        # show the form
        form = EncuestaTransparenciaForm()

    context = {'form': form}
    return render(request, 'users/encuestatransparencia.html', context)
def torneo(request):
    if request.method == "POST":
        # update DB
        form = TorneoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('https://culturameta.gov.co')
    else:
        # show the form
        form = TorneoForm()

    context = {'form': form}
    return render(request, 'users/torneo.html', context)

def presupuesto(request):
    if request.method == "POST":
        # update DB
        form = PresupuestoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('https://culturameta.gov.co')
    else:
        # show the form
        form = PresupuestoForm()

    context = {'form': form}
    return render(request, 'users/presupuesto.html', context)

def filarmonica(request):
    if request.method == "POST":
        # update DB
        form = FilarmonicaForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('https://culturameta.gov.co')
    else:
        # show the form
        form = FilarmonicaForm()

    context = {'form': form}
    return render(request, 'users/filarmonica.html', context)