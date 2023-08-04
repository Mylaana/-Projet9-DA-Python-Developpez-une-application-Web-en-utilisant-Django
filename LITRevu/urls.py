"""
URL configuration for LITRevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

import blog.views
import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.display_index, name="index"),
    path('index/', authentication.views.display_index, name="index"),
    path('flux/', blog.views.display_flux, name="flux"),
    path('posts/', blog.views.display_posts, name="posts"),
    path('abonnements/', blog.views.display_abonnements, name="abonnements"),
    path('sign-in/', authentication.views.display_sign_in, name="sign-in"),
    path('index/', authentication.views.log_out, name="log_out"),
]
