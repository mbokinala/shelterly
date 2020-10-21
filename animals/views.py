from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from rest_framework import filters, viewsets
from actstream import action

from people.models import Person
from animals.models import Animal, AnimalImage
from animals.forms import AnimalForm, ImageForm
from animals.serializers import AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):

    queryset = Animal.objects.all()
    search_fields = ['name', 'species', 'status', 'request__address', 'request__city', 'owner__first_name', 'owner__last_name', 'owner__address', 'owner__city']
    filter_backends = (filters.SearchFilter,)
    serializer_class = AnimalSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            animal = serializer.save()
            action.send(self.request.user, verb='created animal', target=animal)

            # Set room to null if not present, or if status is changed to REUNITED
            if not serializer.validated_data.get('room'):
                serializer.validated_data['room'] = None

            images_data = self.request.FILES
            for key, image_data in images_data.items():
                # Strip out extra numbers from the key (e.g. "extra1" -> "extra")
                category = key.translate({ord(num): None for num in '0123456789'})
                # Create image object.
                AnimalImage.objects.create(image=image_data, animal=animal, category=category)
            # If the animal does not have an owner, create a dummy unknown owner and assign it.
            if not animal.owner:
                owner = Person.objects.create(first_name="Unknown")
                animal.owner = owner
                animal.save()

    def perform_update(self, serializer):
        if serializer.is_valid():
            animal = serializer.save()
            action.send(self.request.user, verb='updated animal', target=animal)
            old_images = serializer.data['extra_images']
            updated_images = self.request.data['extra_images'].split(',') if self.request.data.get('extra_images', None) else []
            # Compare old vs updated extra images to identify ones that have been removed and should be deleted.
            # Strip out MEDIA_URL so that we can compare to image filename using a filter().
            images_to_delete = [image_to_delete.replace(settings.MEDIA_URL, '') for image_to_delete in set(old_images) - set(updated_images)]
            AnimalImage.objects.filter(animal=animal, category="extra", image__in=images_to_delete).delete()
            for key in ['front_image', 'side_image']:
                if serializer.data.get(key, '') != self.request.data.get(key, ''):
                    try:
                        AnimalImage.objects.get(animal=animal, category=key).delete()
                    except ObjectDoesNotExist:
                        pass

            # Only brand new files should show up in request.FILES.
            images_data = self.request.FILES
            for key, image_data in images_data.items():
                # If we have a new front or side image, delete the old one and create a new one.
                if key in ("front_image", "side_image"):
                    AnimalImage.objects.create(image=image_data, animal=animal, category=key)
                # Otherwise create a new extra image.
                else:
                    AnimalImage.objects.create(image=image_data, animal=animal, category="extra")
