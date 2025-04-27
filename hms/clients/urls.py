from django.urls import path
from .views import add_client, delete_client, edit_client, list_clients

urlpatterns = [
    path('add/', add_client, name='add_client'),
    path('list/', list_clients, name='list_clients'),
    path('edit/<int:client_id>/', edit_client, name='edit_client'),
    path('delete/<int:client_id>/', delete_client, name='delete_client'),
]

