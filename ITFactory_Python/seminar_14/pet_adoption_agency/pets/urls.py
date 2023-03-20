from django.urls import path
from . import views
app_name = "pets"
# urlpatterns = [
# 	path("", views.pets, name="all_pets"),
# 	path("<int:pet_id>/", views.pet_details, name="pet_details"),
# 	path("pet/", views.pet_add, name="add")
# ]

#for VERSION 02
urlpatterns = [
	path("", views.PetsView.as_view(), name="all_pets"),
	path("<int:pk>/", views.PetDetailView.as_view(), name="pet_details"),
	path("pet/", views.PetCreateView.as_view(), name="add")
]
