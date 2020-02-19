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
from django.urls import include, path, re_path

from hotline import views
from rest_framework.routers import DefaultRouter

from hotline.views import ServiceRequestViewSet


app_name = 'hotline'
router = DefaultRouter()
router.register(r'servicerequests', views.ServiceRequestViewSet)

urlpatterns = [
    path('', views.hotline_landing, name='hotline_landing'),
    path('api/', include(router.urls)),
    path('owner/new', views.hotline_new_owner, name='hotline_new_owner'),
    path('owner/<rep_pk>/new', views.hotline_new_owner, name = 'hotline_new_owner'),
    path('reporter/new', views.hotline_new_reporter, name = 'hotline_new_reporter'),
    path('request/list', views.service_request_list, name='service_request_list'),
    path('request/list/search/', views.service_request_search, name='service_request_search'),
    path('request/list/search/<query>', views.service_request_search, name='service_request_search'),
    path('request/list/<status>', views.service_request_list, name='service_request_list'),
    re_path(r'^request/(?P<owner_pk>\d+)(?:/(?P<rep_pk>\d+))?/new', views.service_request_new, name = 'service_request_new'),
    path('request/<int:service_request_pk>/', views.service_request_detail, name = 'service_request_detail'),
    path('request/<int:service_request_pk>/update', views.service_request_update, name = 'service_request_update'),
    path('request/<int:service_request_pk>/add/owner', views.service_request_add_owner, name = 'service_request_add_owner'),
    path('request/<service_request_pk>/animal/<species>/add', views.service_request_add_animal, name = "service_request_add_animal"),
]
