# serializers.py
from rest_framework import serializers
from .models import Estaciones

class Estaciones_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Estaciones
        fields = "__all__"
        

