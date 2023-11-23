from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.ForeignKey(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150)

class Quarto(models.Model):
    apartamento = models.IntegerField(max_length=200)
    valor = models.FloatField(max_length=200)

class Hospedagem(models.Model):
    data_entrada = models.DateField(max_length=100)
    data_saida = models.DateField(max_length=100)
    valor = models.FloatField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)

class Consumo(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField(max_length=100)
    valor = models.FloatField(max_length=100)
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)
