from django.shortcuts import render
from django.views.generic import TemplateView,UpdateView,CreateView,DeleteView,ListView
from .models import Hospedagem, Cliente, Consumo, Quarto 

# Create your views here.
class HospedagemQuarto(CreateView):
    template_name = 'templates/hospedagem.html'
    

