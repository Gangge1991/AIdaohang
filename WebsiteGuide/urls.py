"""WebsiteGuide URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from pathlib import Path


def index(request):
    frontend_index = Path(settings.BASE_DIR) / "websitefronted" / "dist" / "index.html"
    if settings.DEBUG and not frontend_index.exists():
        return HttpResponseRedirect("http://localhost:8080/")
    try:
        return TemplateView.as_view(template_name="index.html")(request)
    except Exception:
        return HttpResponse("index.html not found. Build frontend or use http://localhost:8080/", status=500)
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/',include('websiteapp.urls')),
    path('', index)
]
