from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Quarto(models.Model):
    apartamento = models.IntegerField()
    valor = models.FloatField(null=True)

    def __str__(self) -> str:
        return f'{self.apartamento} - {self.valor}'

class Hospedagem(models.Model):
    data_entrada = models.DateField(max_length=100)
    data_saida = models.DateField(max_length=100)
    valor = models.FloatField(null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente

class Consumo(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField(max_length=100)
    valor = models.FloatField(null=True)
    hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

# Models feitos!