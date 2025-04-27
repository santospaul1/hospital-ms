from django.db import models
from programs.models import HealthProgram

class Client(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    date_of_birth = models.DateField()
    enrolled_programs = models.ManyToManyField(HealthProgram, related_name='clients', blank=True)

    def __str__(self):
        return self.full_name
    