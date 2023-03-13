"""Stud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include


from .import views
from django.contrib import admin
from django.urls import path
from .import Hod_views, views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin', admin.site.urls),
    path('base', views.Base, name='base'),
    path('home', Hod_views.Home, name='home'),
    # path('foncier_home', Staff_views.Home, name='foncier_home'),
    # profile
    path('', views.LOGIN, name='login'),
    path('doLogout', views.doLogout, name='logout'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

    # url home
    path('home', include('home.urls')),
    path('education/', include('education.urls')),

    path('sante/', include('sante.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
