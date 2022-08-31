from rest_framework import viewsets
from carros.api import serializers
from carros import models

class CarrosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CarrosSerializer
    queryset = models.Carros.objects.all()