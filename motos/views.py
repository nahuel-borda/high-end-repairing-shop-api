from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from motos.models import *
from motos.serializers import *

class ServicioViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Servicio.objects.all()
	serializer_class = ServicioSerializer