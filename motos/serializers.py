from motos.models import *
from rest_framework import serializers

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        depth = 2
        fields = "__all__"