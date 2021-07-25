"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import include, path, re_path

from .views import RegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # blog
    url(r'^blog/', include('blog.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
]
