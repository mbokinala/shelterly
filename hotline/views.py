from django.core.files.storage import FileSystemStorage
from django.db.models import Count, Exists, OuterRef, Q
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from actstream import action
from .serializers import ServiceRequestSerializer

from animals.models import Animal
from hotline.models import ServiceRequest
from rest_framework import filters, permissions, viewsets

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    search_fields = ['address', 'city', 'animal__name', 'owner__first_name', 'owner__last_name', 'owner__address', 'owner__city', 'reporter__first_name', 'reporter__last_name']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ServiceRequestSerializer
    ordering_fields = ['injured', 'animal_count']
    ordering = ['-injured', '-animal_count']

    # When creating, update any animals associated with the SR owner with the created service request.
    def perform_create(self, serializer):
        if serializer.is_valid():
            service_request = serializer.save()
            action.send(self.request.user, verb='created service request', target=service_request)
            if service_request.owner:
                service_request.owner.animal_set.update(request=service_request.id)

    def perform_update(self, serializer):
        if serializer.is_valid():
            service_request = serializer.save()
            action.send(self.request.user, verb='updated service request', target=service_request)

    def get_queryset(self):
        queryset = ServiceRequest.objects.all().annotate(animal_count=Count('animal')).annotate(injured=Exists(Animal.objects.filter(request_id=OuterRef('id'), injured='yes')))

        # Status filter.
        status = self.request.query_params.get('status', '')
        if status in ('open', 'assigned', 'closed'):
            queryset = queryset.filter(status=status).distinct()

        # Filter on aco_required option for the map.
        aco_required = self.request.query_params.get('aco_required', '')
        if aco_required == 'true':
            queryset = queryset.filter(Q(animal__aggressive='yes') | Q(animal__species='other'))

        # Exclude SRs without a geolocation when fetching for a map.
        is_map = self.request.query_params.get('map', '')
        if is_map == 'true':
            queryset = queryset.exclude(Q(latitude=None) | Q(longitude=None))
        return queryset
