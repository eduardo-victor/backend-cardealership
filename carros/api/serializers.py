from dataclasses import field
from rest_framework import serializers
from carros import models

class CarrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carros
        fields = '__all__'