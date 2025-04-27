from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')
    search_fields = ('full_name', 'email', 'phone_number')
    list_filter = ('enrolled_programs',)
# Register your models here.
