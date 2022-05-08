from rest_framework import serializers
from .models import Itinerary

class ItinerarySerializer(serializers.ModelSerializer):
    """
    Serializer class for an itineary
    """ 
    class Meta:
        model = Itinerary
        fields = ['id','departure_info', 'places_to_visit', 'recommened_hotel', 'recommened_activities','return_info']