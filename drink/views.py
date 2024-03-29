#from django
from django.http import JsonResponse

#from rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#from Project
from .models import Drink
from .serializers import DrinkSerializer
from drink import serializers

@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    
    #get all the drinks
    #serialize them
    #return jeson
    
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)  # Or👇👇
        #return JsonResponse({'drinks':serializer.data})
        # if it is not returning a dictionary: return JsonResponse(serializer.data, safe=False) 
        
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
        
        
@api_view(['GET', 'PUT', 'DELETE'])    
def drink_details(request, id, format=None):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
