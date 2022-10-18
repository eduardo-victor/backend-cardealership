from django.db import models
from uuid import uuid4
from pictures.models import PictureField

class Carros(models.Model):
    id_carro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_carro = models.CharField(max_length=255)
    marca_carro = models.CharField(max_length=255)
    potencia_carro = models.IntegerField()
    ano_carro = models.IntegerField()
    preco_carro = models.DecimalField(max_digits=13 ,decimal_places=2)
    foto_carro = PictureField(upload_to="media/cars/images")

