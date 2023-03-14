from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from devices.models import *
from devices.serializers import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class HelloWorld(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        return JsonResponse({'message': 'Hello, World!'})

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer

	@action(detail=False, methods=['GET'], name='Get Status Count')
	def status_count(self, request, *args, **kwargs):
		return Response(data=Service.status_count(), status=200)
	
	@action(detail=False, methods=['GET'], name='Get Status Count by Date')
	def status_count_by_date(self, request, *args, **kwargs):
		return Response(data=Service.status_count_by_date(), status=200)
	
	@action(detail=False, methods=['GET'], name='Get New Services Count by Date')
	def service_ingress_count_by_date(self, request, *args, **kwargs):
		return Response(data=Service.services_ingress_by_date(), status=200)
	
class OperatorViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Operator.objects.all()
	serializer_class = OperatorSerializer

	@action(detail=False, methods=['GET'], name='Get Top Operator by Workload')
	def top_operator_by_workload(self, request, *args, **kwargs):
		return Response(data=Operator.top_by_workload(), status=200)
	
	@action(detail=False, methods=['GET'], name='Get Operator by Workload')
	def operator_by_workload(self, request, *args, **kwargs):
		return Response(data=Operator.by_workload(), status=200)
	
class ProviderViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Provider.objects.all()
	serializer_class = ProviderSerializer

	@action(detail=False, methods=['GET'], name='Get Top Provider by Participation')
	def top_provider_by_participation(self, request, *args, **kwargs):
		return Response(data=Provider.top_by_participation(), status=200)

	@action(detail=False, methods=['GET'], name='Get Provider by Participation')
	def provider_by_participation(self, request, *args, **kwargs):
		return Response(data=Provider.by_participation(), status=200)

class DeviceViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Device.objects.all()
	serializer_class = DeviceSerializer

class ModelViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Model.objects.all()
	serializer_class = ModelSerializer

class BrandViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer

class ClientViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

	@action(detail=False, methods=['GET'], name='Get Top Client by Services')
	def top_client_by_services(self, request, *args, **kwargs):
		return Response(data=Client.top_by_services(), status=200)

	@action(detail=False, methods=['GET'], name='Get Client by Services')
	def client_by_services(self, request, *args, **kwargs):
		return Response(data=Client.by_services(), status=200)

class PartViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Part.objects.all()
	serializer_class = PartSerializer


class Dashboard(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, format=None):
        return JsonResponse({
		'clients': ClientViewSet.as_view({'get': 'list'})(request._request).data,
		'brands': BrandViewSet.as_view({'get': 'list'})(request._request).data,
		'devices': DeviceViewSet.as_view({'get': 'list'})(request._request).data,
		'parts': PartViewSet.as_view({'get': 'list'})(request._request).data,
		'providers': ProviderViewSet.as_view({'get': 'list'})(request._request).data,
		'operators': OperatorViewSet.as_view({'get': 'list'})(request._request).data,
		'models': ModelViewSet.as_view({'get': 'list'})(request._request).data,
		'services': ServiceViewSet.as_view({'get': 'list'})(request._request).data,
		'clients_by_services': Client.by_services(),
		'top_clients_by_services': Client.top_by_services(),
		'provider_by_participation': Provider.by_participation(),
		'top_provider_by_participation': Provider.top_by_participation(),
		'operator_by_workload': Operator.by_workload(),
		'top_operator_by_workload': Operator.top_by_workload(),
		'service_ingress_count_by_date': Service.services_ingress_by_date(),
		'services_by_status': Service.status_count(),
		'status_count_by_date': Service.status_count_by_date(),
	})
