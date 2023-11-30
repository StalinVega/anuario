# serializers.py
from rest_framework import serializers
from .models import HUMEDAD_RELATIVA_DEL_AIRE_max

class Humedad_Serializer(serializers.ModelSerializer):
    class Meta:
        model = HUMEDAD_RELATIVA_DEL_AIRE_max
        fields = "__all__"
        

