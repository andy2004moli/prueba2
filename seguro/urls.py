from django.urls import path
from .views import CotizacionListView

urlpatterns = [
    path('cotizaciones/', CotizacionListView.as_view(), name='visualizar_cotizaciones'),
]