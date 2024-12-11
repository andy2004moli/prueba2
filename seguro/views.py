from django.shortcuts import render
from.models import Customer
from.models import Ciudad
from.models import Cotizacion
from django.views.generic import ListView
# Create your views here.

class CotizacionListView(ListView):
    model = Cotizacion  # Modelo que utilizará la vista
    template_name = 'cotizacion_visualizar.html'  # Plantilla que renderizará la vista
    context_object_name = 'cotizaciones'  # Nombre de la variable para usar en la plantilla