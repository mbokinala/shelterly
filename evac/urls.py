from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from evac import views

app_name = 'evac'
router = DefaultRouter()
router.register(r'evacteammember', views.EvacTeamMemberViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/evacteammember/list', views.EvacTeamMemberSelectionList)
]