#from rest_framework
from rest_framework import serializers

#from the project
from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
