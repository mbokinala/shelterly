from django.db import models

from animals.choices import AGE_CHOICES, ALL_BREED_CHOICES, SEX_CHOICES, SIZE_CHOICES, SPECIES_CHOICES, STATUS_CHOICES
from animals.colors import ALL_COLOR_CHOICES, ALL_PATTERN_CHOICES
from location.models import Location
from hotline.models import ServiceRequest
from people.models import Person


# Create your models here.
class Animal(Location):

    request = models.ForeignKey(ServiceRequest, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True)

    #choice fields
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES, blank=True, null=True)
    breed = models.CharField(max_length=50, choices=ALL_BREED_CHOICES, blank=True, null=True, default='Unknown')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True)
    pcolor = models.CharField(max_length=50, choices=ALL_COLOR_CHOICES, verbose_name='Primary Color' , blank=True, null=True)
    scolor = models.CharField(max_length=50, choices=ALL_COLOR_CHOICES, verbose_name='Secondary Color', blank=True, null=True)
    markings = models.CharField(max_length=50, choices=ALL_PATTERN_CHOICES, blank=True, null=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, blank=True, null=True)
    age = models.CharField(max_length=10, choices=AGE_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True, null=True, default='REPORTED')

    #boolean fields
    fixed = models.BooleanField(blank=True, null=True)
    aggressive = models.BooleanField(blank=True, null=True)
    confined = models.BooleanField(blank=True, null=True)
    chipped = models.BooleanField(blank=True, null=True)
    attended_to = models.BooleanField(blank=True, null=True)

    #text fields
    collar_info = models.TextField(blank=True, null=True)
    behavior_notes = models.TextField(blank=True, null=True)
    chip_info = models.TextField(blank=True, null=True)
    diet_notes = models.TextField(blank=True, null=True)
    med_notes = models.TextField(blank=True, null=True, verbose_name='Medical Notes')
    last_seen = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    @property
    def info(self):
        return '%s (%s, %s, %s)' % (self.name.capitalize(), self.species.capitalize(), self.breed.capitalize(), self.sex)

    @property
    def location_type(self):
        return 'animal'

    class Meta:
        ordering = []
