from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Itinerary(models.Model):
    """
    Data model for an itineary
    """ 
    departure_info = models.TextField()
    places_to_visit = models.TextField()
    recommened_hotel = models.TextField()
    recommened_activities = models.TextField(default='')
    return_info = models.TextField(default='')
    
