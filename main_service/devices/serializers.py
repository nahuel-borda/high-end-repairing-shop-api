from devices.models import *
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Service
        depth = 3
        fields = "__all__"


class OperatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operator
        depth = 3
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        depth = 1
        fields = "__all__"

class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        depth = 3
        fields = "__all__"

class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        depth = 3
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        depth = 3
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        depth = 3
        fields = "__all__"

class PartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Part
        depth = 3
        fields = "__all__"