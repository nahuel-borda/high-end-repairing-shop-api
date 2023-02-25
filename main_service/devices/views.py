from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from devices.models import *
from devices.serializers import *

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer