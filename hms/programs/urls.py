from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_program, name='add-program'),
    path('list/', views.list_programs, name='list-programs'),
]
