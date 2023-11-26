# urls.py
from django.urls import path
from .views import add_event

urlpatterns = [
    # Your existing patterns
    path('add/', add_event, name='add_event'),
]
