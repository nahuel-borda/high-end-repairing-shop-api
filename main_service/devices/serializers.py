from devices.models import *
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        depth = 2
        fields = "__all__"