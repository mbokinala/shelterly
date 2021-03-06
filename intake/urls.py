"""RAMS_SKELETON URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from intake import views

app_name = 'intake'

urlpatterns = [
    path('', views.intake_landing, name ='intake_landing'),
    path('owned/', views.intake_owned, name='intake_owned'),
    path('evacreq/select', views.select_evac_req, name='select_evac_req'),
    path('owned/<owner_pk>/<species>/new', views.intake_new_animal, name='intake_new_animal'),
]
