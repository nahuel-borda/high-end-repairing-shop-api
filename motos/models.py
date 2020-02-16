from django.db import models
from django_currentuser.middleware import (
    get_current_user,
    get_current_authenticated_user
)


SERVICE_STATUS_CHOICES = (
    ("En espera", "En espera"),
    ("En proceso", "En proceso"),
    ("Demorado", "Demorado"),
    ("Finalizado", "Finalizado"),
)

class Marca(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class Modelo(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    dni = models.IntegerField()
    numero_celular = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Proveedor(models.Model):
    name = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Moto(models.Model):
    patente = models.CharField(max_length=250)
    modelo = models.ForeignKey(Marca, on_delete=models.CASCADE)
    marca = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patente} - {self.modelo} - {self.marca}"

class Repuesto(models.Model):
    nombre = models.CharField(max_length=250)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    costo = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.proveedor}"


class Mecanico(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    dni = models.IntegerField()
    numero_celular = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Servicio(models.Model):
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=SERVICE_STATUS_CHOICES, default='En espera')
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    respuestos = models.ManyToManyField(
        Repuesto, blank=True, related_name="servicios"
    )
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(max_length=400, null=True, blank=True, help_text="Una breve descripcion del servicio a realizar")

    def tomar_servicio(self):
        self.mecanico = get_current_authenticated_user()
        self.estado = SERVICE_STATUS_CHOICES[1]

    def demorar_servicio(self):
        self.estado = SERVICE_STATUS_CHOICES[2]

    def terminar_servicio(self):
        self.estado = SERVICE_STATUS_CHOICES[3]

    def __str__(self):
        return f"{self.moto} - {self.estado}"

