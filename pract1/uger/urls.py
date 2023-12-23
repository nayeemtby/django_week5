"""
URL configuration for pract1 project.

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
from django.urls import path

from uger.views import changePassword, home, loginView, logout, profile, register, resetPass

urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('login', loginView, name='login'),
    path('logout', logout, name='logout'),
    path('profile', profile, name='profile'),
    path('cngpass', changePassword, name='cngpass'),
    path('resetPass', resetPass, name='resetPass'),
]
