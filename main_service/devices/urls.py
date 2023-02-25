from django.urls import path, include
from rest_framework.routers import DefaultRouter
from devices.views import ServiceViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'services', ServiceViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]