from django.urls import path
from . import views
app_name = "pets"
urlpatterns = [
	path("", views.pets, name="all_pets"),
	path("<int:pet_id>/", views.pet_details, name="pet_details"),
	path("pet/", views.pet_add, name="add")
]
