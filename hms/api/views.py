from django.shortcuts import render
from rest_framework import generics
from clients.models import ClientSerializer


class ClientProfileView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_object(self):
        return self.request.user.client
# Create your views here.
