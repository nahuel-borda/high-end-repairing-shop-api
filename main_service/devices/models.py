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

class Brand(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class Model(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class Client(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    personal_id = models.IntegerField()
    celphone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Provider(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    celphone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname}"

class Device(models.Model):
    patent = models.CharField(max_length=250)
    model = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand = models.ForeignKey(Model, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patent} - {self.model} - {self.brand}"

class Part(models.Model):
    name = models.CharField(max_length=250)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.provider} - {self.price}"


class Operator(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    personal_id = models.IntegerField()
    celphone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Service(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=SERVICE_STATUS_CHOICES, default='En espera')
    ingress_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    parts = models.ManyToManyField(Part, blank=True, related_name="services")
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True, help_text="Una breve descripcion del service a realizar")

    def take_service(self):
        self.operator = get_current_authenticated_user()
        self.status = SERVICE_STATUS_CHOICES[1]
        self.save()

    def delay_service(self):
        self.status = SERVICE_STATUS_CHOICES[2]
        self.save()

    def finalize_service(self):
        self.status = SERVICE_STATUS_CHOICES[3]
        self.save()

    def __str__(self):
        return f"{self.device} - {self.status}"

