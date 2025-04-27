from rest_framework import serializers
from clients.models import Client
from programs.models import HealthProgram

class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = ['id', 'name', 'description']

class ClientSerializers(serializers.ModelSerializer):
        enrolled_programs = HealthProgramSerializer(many=True)

        class Meta:
            model = Client
            fields = ['id', 'full_name', 'date_of_birth']