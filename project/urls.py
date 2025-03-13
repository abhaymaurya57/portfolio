"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('/',include('abhay.urls')),
    path('admin/', admin.site.urls),
    # path('',views.home,name='home'),
    # path('index/',views.index,name='index'),
    path('',include('abhay.urls')),
    # path('home/',include('abhay.urls')),
    # path('about/',include('abhay.urls')),
    # path('signin/',include('abhay.urls')),
    # path('signup/',include('abhay.urls')),
    # path('skill/',include('abhay.urls')),
    # path('contact/',include('abhay.urls')),
    # path('comment/',include('abhay.urls')),





    path("__reload__/", include("django_browser_reload.urls")),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
