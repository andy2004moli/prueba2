from django.contrib import admin
from seguro.models import Customer, Ciudad, Cotizacion

# Personaliza la vista del modelo Customer
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('names', 'dni', 'email', 'phone', 'ciudad', 'created')  # Campos visibles en la lista
    search_fields = ('names', 'dni', 'email')  # Campos para buscar
    list_filter = ('ciudad', 'created')  # Filtros en el lateral
    ordering = ('-created',)  # Ordena por fecha de creación descendente
    date_hierarchy = 'created'  # Barra de navegación por fechas

# Personaliza la vista del modelo Ciudad
@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # Campos visibles en la lista
    search_fields = ('nombre',)  # Permite buscar por nombre

# Personaliza la vista del modelo Cotizacion
@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'vigencia', 'vencimiento', 'tipo_poliza', 'total')  # Campos visibles en la lista
    search_fields = ('cliente__names', 'tipo_poliza')  # Permite buscar por nombre de cliente y tipo de póliza
    list_filter = ('tipo_poliza', 'vigencia')  # Filtros por tipo y vigencia
    ordering = ('-vigencia',)  # Ordena por vigencia descendente
