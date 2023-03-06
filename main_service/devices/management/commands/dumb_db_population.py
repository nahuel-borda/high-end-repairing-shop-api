# setup_test_data.py
import random

from django.db import transaction
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from devices.models import *
from devices.factories import *

NUM_BRANDS = 30
NUM_MODELS = 30
NUM_CLIENTS = 50
NUM_PROVIDERS = 20
NUM_DEVICES = 20
NUM_PARTS = 60
NUM_OPERATORS = 7
NUM_SERVICES = 100


def generate_fake_dates():
    start_dt = datetime.now() - timedelta(days=30)
    end_dt = datetime.now() + timedelta(days=30)

    # difference between current and previous date
    delta = timedelta(days=1)

    # store the dates between two dates in a list
    dates = []

    while start_dt <= end_dt:
        # add current date to list by converting  it to iso format
        dates.append(start_dt)
        # increment start date by timedelta
        start_dt += delta
    return dates

DATES = generate_fake_dates()


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        self.stdout.write("Deleting old data...")

        for m in [Brand, Model, Client, Provider, Device, Part, Operator, Service]:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        
        brands_list = []
        for _ in range(NUM_BRANDS):
            brand = BrandFactory()
            brands_list.append(brand)

        models_list = []
        for _ in range(NUM_MODELS):
            model = ModelFactory()
            models_list.append(model)
        
        clients_list = []
        for _ in range(NUM_CLIENTS):
            client = ClientFactory()
            clients_list.append(client)
        
        provider_list = []
        for _ in range(NUM_PROVIDERS):
            provider = ProviderFactory()
            provider_list.append(provider)

        devices_list = []
        for _ in range(NUM_DEVICES):
            device = DeviceFactory()
            device.brand = random.choice(brands_list)
            device.model = random.choice(models_list)
            device.client = random.choice(clients_list)
            device.save()
            devices_list.append(device)

        parts_list = []
        for _ in range(NUM_PARTS):
            part = PartFactory()
            part.provider = random.choice(provider_list)
            part.brand = random.choice(brands_list)
            part.save()
            parts_list.append(part)
        
        operators_list = []
        for _ in range(NUM_OPERATORS):
            operator = OperatorFactory()
            operators_list.append(operator)

        for _ in range(NUM_SERVICES):
            service = ServiceFactory()
            service.device = random.choice(devices_list)
            service.operator = random.choice(operators_list)
            service.status = random.choice(Service.Status.choices)
            service.ingress_date = random.choice(DATES)
            for instance_id in random.choices(
                list(
                    map(
                        lambda x: x.pk, 
                        parts_list
                    )
                ), 
                k=4
            ):
                service.parts.add(instance_id) 
            service.save()
