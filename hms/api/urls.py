from django.urls import path, include
from .views import ClientProfileView

urlpatterns = [
    path('client/<int:pk>/', ClientProfileView.as_view(), name='client-profile'),

]
