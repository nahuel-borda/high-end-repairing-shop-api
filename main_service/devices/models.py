from ast import literal_eval
from django.db import models
from django.db.models import Count, Sum, IntegerField
from django_currentuser.middleware import (
    #get_current_user,
    get_current_authenticated_user
)



def display_status(status_field):
    return literal_eval(status_field)[0] 

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

    @classmethod
    def top_by_services(cls):
        return [
            {
                'count': obj["services"],
                'name': f"{obj['firstname']} {obj['lastname']}" 
            } for obj in cls.objects.exclude(devices__isnull=True).values('firstname', 'lastname').annotate(
                services=Count('devices__services')
            ).order_by('-services').all()[:7]
        ]
    
    @classmethod
    def by_services(cls):
        return [
            {
                'count': obj["services"],
                'name': f"{obj['firstname']} {obj['lastname']}" 
            } for obj in cls.objects.exclude(devices__isnull=True).values('firstname', 'lastname').annotate(
                services=Count('devices__services')
            ).order_by('-services').all()[:20]
        ]

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Provider(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    celphone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True, blank=True)

    @classmethod
    def top_by_participation(cls):
        return [
            {
                'count': obj["participation"],
                'name': obj['name']
            } for obj in cls.objects.exclude(parts__isnull=True).values('name').annotate(
                participation=Count('parts')
            ).order_by('-participation').all()[:7]
        ]
    
    @classmethod
    def by_participation(cls):
        return [
            {
                'count': obj["participation"],
                'name': obj['name']
            } for obj in cls.objects.exclude(parts__isnull=True).values('name').annotate(
                participation=Count('parts')
            ).order_by('-participation').all()[:25]
        ]

    def __str__(self):
        return f"{self.name}"

class Device(models.Model):
    patent = models.CharField(max_length=250)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="devices")

    def __str__(self):
        return f"{self.patent} - {self.model} - {self.brand}"

class Part(models.Model):
    name = models.CharField(max_length=250)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank=True, related_name="parts")
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.provider} - {self.price}"


class Operator(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    personal_id = models.IntegerField()
    celphone = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True, blank=True)

    @classmethod
    def top_by_workload(cls):
        return [
            {
                'count': obj["workload"],
                'name': f"{obj['firstname']} {obj['lastname']}" 
            } for obj in cls.objects.exclude(services__isnull=True).values('firstname', 'lastname').annotate(
                workload=Count('services')
            ).order_by('-workload').all()[:5]
        ]
    
    @classmethod
    def by_workload(cls):
        return [
            {
                'count': obj["workload"],
                'name': f"{obj['firstname']} {obj['lastname']}" 
            } for obj in cls.objects.exclude(services__isnull=True).values('firstname', 'lastname').annotate(
                workload=Count('services')
            ).all()
        ]

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Service(models.Model):
    class Status(models.TextChoices):
        WAITING = "En espera", "En espera"
        PROCESSING = "En proceso", "En proceso"
        DELAYED = "Demorado", "Demorado"
        FINISHED = "Finalizado", "Finalizado"

    status = models.CharField(max_length=50, choices=Status.choices, default=Status.WAITING)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name="services")
    ingress_date = models.DateField()
    ingress_time = models.TimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    parts = models.ManyToManyField(Part, blank=True, related_name="service")
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, null=True, blank=True, related_name="services")
    description = models.CharField(max_length=400, null=True, blank=True, help_text="Una breve descripcion del service a realizar")

    @classmethod
    def status_count(cls):
        return [
            {
                'name': display_status(obj["status"]),
                'count': obj["status_count"]
            } for obj in cls.objects.values('status').annotate(
                status_count=Count('status')
            ).order_by('-status').all()
        ]
    
    @classmethod
    def status_count_by_date(cls):
        return [
            {
                'count': obj["status_count"],
                'date': obj["ingress_date"]
            } for obj in cls.objects.values('ingress_date').annotate(
                status_count=Count('status')
            ).all()
        ]
    
    @classmethod
    def services_ingress_by_date(cls):
        return [
            {
                'count': obj["count"],
                'date': obj["ingress_date"]
            } for obj in cls.objects.values('ingress_date').annotate(
                count=Count("id")
            ).all()
        ]
    
    def take_service(self):
        self.operator = get_current_authenticated_user()
        self.status = self.Status.PROCESSING
        self.save()

    def delay_service(self):
        self.status = self.Status.DELAYED
        self.save()

    def finalize_service(self):
        self.status = self.Status.FINISHED
        self.save()

    def get_status_display(self):
        return display_status(self.status) 

    def __str__(self):
        return f"{self.device} - {self.status}"

