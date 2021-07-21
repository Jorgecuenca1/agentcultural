"""culturameta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from agentcultural import views as agentcultural_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/signup/',agentcultural_views.signup,name='signup'),
    path('users/login/',agentcultural_views.login_view,name='login'),
    path('users/datos/',agentcultural_views.datos, name='datos'),
    path('users/portafolio/',agentcultural_views.portafolio, name='portafolio'),
    path('users/entidad/',agentcultural_views.entidad, name='entidad'),
    path('users/logout/', agentcultural_views.logout_view, name='logout'),
    path('users/agenteoentidad/',agentcultural_views.agenteoentidad, name='agenteoentidad'),
    path('users/agentcultural/<int:id>/edit', agentcultural_views.edit_agentcultural, name='edit_agentcultural'),
    path('users/entidad/<int:id>/edit', agentcultural_views.edit_entidad, name='edit_entidad'),
    path('export/', agentcultural_views.export_pdf, name="export-pdf" ),
    path('exporte/', agentcultural_views.export_pdfe, name="export-pdfe" ),
    path('portafoliopdf/', agentcultural_views.export_pdfp, name="export-pdfp" )

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
