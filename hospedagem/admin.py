from django.contrib import admin
from .views import HospedagemCriar, HospedagemDetalhe, HospedagemEditar, HospedagemRemover, HospedagemListar

@admin.register(HospedagemCriar)
class HospedagemAdmin(admin.ModelAdmin):
    list_display=('','endereco','email')

@admin.register(HospedagemDetalhe)
class HospedagemAdmin(admin.ModelAdmin):
    list_display=('nome',)

@admin.register(HospedagemEditar)
class HospedagemAdmin(admin.ModelAdmin):
    list_display=('nome','sigla_estado',)

@admin.register(HospedagemRemover)
class HospedagemAdmin(admin.ModelAdmin):
    list_display=('nome','sigla_estado',)

@admin.register(HospedagemListar)
class HospedagemAdmin(admin.ModelAdmin):
    list_display=('nome','sigla_estado',)

