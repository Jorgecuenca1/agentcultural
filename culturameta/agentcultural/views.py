from django.db.utils import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import AgentCultural, Entidad
from .forms import AgentCulturalForm, EntidadForm

from django.utils import timezone
from weasyprint import HTML
from weasyprint.fonts import FontConfiguration
from django.http import HttpResponse
from django.template.loader import render_to_string



def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        user.first_name = request.POST['name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        agentcultural = AgentCultural(user=user)
        agentcultural.name = request.POST['name']
        agentcultural.last_name = request.POST['last_name']
        agentcultural.save()
        entidad = Entidad(user=user)
        entidad.save()

        return redirect('login')

    return render(request, 'users/signup.html')

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('agenteoentidad')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')
def agenteoentidad(request):


    return render(request, 'users/agenteoentidad.html')
def datos(request):
    user = request.user


    profiles = AgentCultural.objects.filter(user=user, created__lte=timezone.now()).order_by('created')

    return render(request, 'users/datos.html',
                  {'profiles': profiles,})

def portafolio(request):
    user = request.user


    profiles = AgentCultural.objects.filter( created__lte=timezone.now()).order_by('created')

    return render(request, 'users/portafolio.html',
                  {'profiles': profiles,})

def informacion(request):
    user = request.user


    profiles = AgentCultural.objects.filter( created__lte=timezone.now()).order_by('created')

    return render(request, 'users/informacion.html',
                  {'profiles': profiles,})

def entidad(request):
    user = request.user


    entidads = Entidad.objects.filter(user=user, created__lte=timezone.now()).order_by('created')

    return render(request, 'users/entidad.html',
                  {'entidads': entidads,})

def edit_agentcultural(request, id):
    post = get_object_or_404(AgentCultural, id=id)
    if request.method == "POST":
        # update DB
        form = AgentCulturalForm(request.POST, request.FILES,  instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('datos')
    else:
        # show the form
        form = AgentCulturalForm(instance=post)

    context = {'form': form}
    return render(request, 'users/edit_agentcultural.html', context)


def edit_entidad(request, id):
    post = get_object_or_404(Entidad, id=id)
    if request.method == "POST":
        # update DB
        form = EntidadForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('entidad')
    else:
        # show the form
        form = EntidadForm(instance=post)

    context = {'form': form}
    return render(request, 'users/edit_entidad.html', context)

def export_pdf(request):

    user = request.user
    profiles = AgentCultural.objects.filter(user=user, created__lte=timezone.now()).order_by('created')
    context = {'profiles':profiles}
    html = render_to_string("users/pdf.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; datos.pdf"

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)

    return response
def export_pdfp(request):

    user = request.user
    profiles = AgentCultural.objects.filter(created__lte=timezone.now()).order_by('created')
    context = {'profiles':profiles}
    html = render_to_string("users/portafolio.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; portafolio.pdf"

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)

    return response
def export_pdfe(request):

    user = request.user
    entidades = Entidad.objects.filter(user=user, created__lte=timezone.now()).order_by('created')
    context = {'entidades':entidades}
    html = render_to_string("users/pdfe.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; datos.pdf"

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)

    return response
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')