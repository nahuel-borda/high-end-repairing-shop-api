from devices.models import *
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Service
        depth = 3
        fields = "__all__"