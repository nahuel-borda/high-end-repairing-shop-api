# factories.py
import random
import factory
from factory.django import DjangoModelFactory

from .models import Brand, Model, Client, Provider, Device, Part, Operator, Service, SERVICE_STATUS_CHOICES

# Defining a factory
class BrandFactory(DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Faker("name")

# Defining a factory
class ModelFactory(DjangoModelFactory):
    class Meta:
        model = Model

    name = factory.Faker("name")

# Defining a factory
class ClientFactory(DjangoModelFactory):
    class Meta:
        model = Client

    firstname = factory.Faker("first_name")
    lastname = factory.Faker("last_name")
    personal_id = factory.Faker("random_int")
    celphone = factory.Faker("random_int")
    email = factory.Faker("email")

# Defining a factory
class ProviderFactory(DjangoModelFactory):
    class Meta:
        model = Provider

    firstname = factory.Faker("first_name")
    lastname = factory.Faker("last_name")
    address = factory.Faker("address")
    celphone = factory.Faker("random_int")
    email = factory.Faker("email")

# Defining a factory
class DeviceFactory(DjangoModelFactory):
    class Meta:
        model = Device

    patent = factory.Faker("random_int")
    brand = factory.SubFactory(BrandFactory)
    model = factory.SubFactory(ModelFactory)
    client = factory.SubFactory(ClientFactory)

# Defining a factory
class PartFactory(DjangoModelFactory):
    class Meta:
        model = Part

    name = factory.Faker("first_name")
    provider = factory.SubFactory(ProviderFactory)
    price = factory.Faker("random_int")

# Defining a factory
class OperatorFactory(DjangoModelFactory):
    class Meta:
        model = Operator

    firstname = factory.Faker("first_name")
    lastname = factory.Faker("last_name")
    personal_id = factory.Faker("random_int")
    celphone = factory.Faker("random_int")
    email = factory.Faker("email")

# Defining a factory
class ServiceFactory(DjangoModelFactory):
    class Meta:
        model = Service

    device = factory.SubFactory(DeviceFactory)
    operator = factory.SubFactory(OperatorFactory)
    parts = factory.RelatedFactoryList(
        PartFactory,
        size=4
    )
    description = factory.Faker("sentence")
    ingress_date = factory.Faker("date")
    end_date = factory.Faker("date")
    


# Using a factory with auto-generated data
 
# You can optionally pass in your own data
#u = UserFactory(name="Alice")
#u.name # Alice
#u.id # 52