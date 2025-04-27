from django.shortcuts import render
from rest_framework import generics
from .serializers import ClientSerializers
from clients.models import Client

class ClientProfileView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers

    def get_object(self):
        return self.request.user.client
# Create your views here.
