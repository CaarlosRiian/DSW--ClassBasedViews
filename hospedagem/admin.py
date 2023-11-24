from django.contrib import admin
from .models import Cliente, Quarto, Hospedagem, Consumo

admin.site.register(Cliente)
admin.site.register(Quarto)
admin.site.register(Hospedagem)
admin.site.register(Consumo)

