from django.urls import path, include
from rest_framework.routers import DefaultRouter
from devices.views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'operators', OperatorViewSet)
router.register(r'providers', ProviderViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'model', ModelViewSet)
router.register(r'brand', BrandViewSet)
router.register(r'parts', PartViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]