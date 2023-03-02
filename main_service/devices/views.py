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

	@action(detail=False, methods=['GET'], name='Get Status Accumulation')
	def status_accumulate(self, request, *args, **kwargs):
		queryset = models.Service.objects.all()
		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)
		# Falta hacer la transformacion a tabla de Status: #Cardinal
		# Algo asi:
		# 'En espera': 10
		# 'En proceso': 20
        # 'Finalizado': 30
		# 'Demorado': 40
		