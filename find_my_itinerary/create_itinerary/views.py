from django.http import HttpResponse
from .models import Itinerary
from .serializers import ItinerarySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# function based views with api_view decorator
@api_view(['GET'])
def get_itinerary(request):
    """
    get list of all itinearies
    """    
    if request.method == 'GET':
        iti = Itinerary.objects.all()
        serializer = ItinerarySerializer(iti, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def post_itinerary(request):
    """
    add a new itineary
    """ 
    if request.method == 'POST':
        serializer = ItinerarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_itinerary_by_id(request,pk):
    """
    get an itineary based on id
    """ 
    try:
        iti = Itinerary.objects.get(pk=pk)
    except Itinerary.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = ItinerarySerializer(iti)
        return Response(serializer.data)
    
@api_view(['PUT'])
def put_itinerary(request,pk):
    """
    update an itineary
    """ 
    if request.method == 'PUT':
        iti = Itinerary.objects.get(pk=pk)
        serializer = ItinerarySerializer(iti, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_itinerary(request,pk):
    """
    delete an itineary
    """ 
    if request.method == 'DELETE':
        iti = Itinerary.objects.get(pk=pk)
        iti.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
