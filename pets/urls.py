from django.urls import path
from .views import *

urlpatterns = [
    path("pets/", PetView.as_view()),
    path("pets/<pet_id>/", PetDetailView.as_view()),
    
]