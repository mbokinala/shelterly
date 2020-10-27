from django.db.models import Count, Exists, OuterRef, Q
from .serializers import ServiceRequestSerializer

from animals.models import Animal
from hotline.models import ServiceRequest
from rest_framework import filters, permissions, serializers, viewsets


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
            for service_request in ServiceRequest.objects.filter(latitude=serializer.validated_data['latitude'], longitude=serializer.validated_data['longitude'], status='open'):
                raise serializers.ValidationError(['Multiple open Requests may not exist with the same address.', service_request.id])
            service_request = serializer.save()
            if service_request.owner:
                service_request.owner.animal_set.update(request=service_request.id)

    def perform_update(self, serializer):
        if serializer.is_valid():
            for service_request in ServiceRequest.objects.filter(latitude=serializer.validated_data['latitude'], longitude=serializer.validated_data['longitude'], status='open').exclude(id=self.kwargs['pk']):
                raise serializers.ValidationError(['Multiple open Requests may not exist with the same address.', service_request.id])
            service_request = serializer.save()
            if service_request.owner:
                service_request.owner.animal_set.update(request=service_request.id)

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
