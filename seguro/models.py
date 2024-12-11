from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Ciudad")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        db_table = "ciudad"
        ordering = ['id']


class Customer(models.Model):
    names = models.CharField(max_length=150, verbose_name="Nombres", unique=True)  # Evita nombres repetidos
    dni = models.CharField(max_length=13, verbose_name="RUC o Cédula", unique=True)  # Evita duplicados
    email = models.EmailField(max_length=150, verbose_name="Correo Electrónico", unique=True)  # Evita duplicados
    address = models.TextField(verbose_name="Dirección")
    phone = models.CharField(max_length=15, verbose_name="Teléfono")
    movil = models.CharField(max_length=15, verbose_name="Celular")
    avatar = models.ImageField(upload_to="avatar", verbose_name="Foto del Cliente", null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True, verbose_name="Ciudad")  # Relación con Ciudad
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Modificación")

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = "customer"
        ordering = ['id']


class Cotizacion(models.Model):
    cliente = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Cliente")
    vigencia = models.DateField(verbose_name="Vigencia")
    plazo = models.PositiveIntegerField(verbose_name="Plazo (días)")
    vencimiento = models.DateField(verbose_name="Vencimiento")
    tipo_poliza = models.CharField(max_length=100, verbose_name="Tipo de Póliza")
    valor_asegurado = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Asegurado")
    tasa = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Tasa (%)")
    prima_minima = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prima Mínima", default=0)
    prima = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prima", default=0)
    derecho = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Derecho", default=0)
    iva = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="IVA", default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total", default=0)

    def __str__(self):
        return f"Cotización para {self.cliente}"

    class Meta:
        verbose_name = "Cotización"
        verbose_name_plural = "Cotizaciones"
        db_table = "cotizacion"
        ordering = ['id']
