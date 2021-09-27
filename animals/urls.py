from django.urls import path
from animals import views

app_name = 'animals'

urlpatterns = [

    path("animals_list/", views.list_animals, name = "animals_list"),
    path("create_animal", views.create_animal, name = "create_animal"),
    path("animal_details/<pk>", views.animal_details, name = "animal_details"),
    path("animal_photos/<animal_name>", views.animal_photos, name = "animal_photos"),
    path("update_animal/<pk>", views.update_animal, name = "update_animal"),
    path("delete_animal/<pk>", views.delete_animal, name = "delete_animal"),
    path("comment/<pk>", views.CommentView, name = "comment"),
    path("comments_list/<pk>", views.CommentsList, name = "comments_list"),
    path("add_photos/<pk>", views.add_photos, name = "add_photos"),

]