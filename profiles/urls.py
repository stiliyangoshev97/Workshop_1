from django.urls import path

from profiles import views



app_name = "profiles"

urlpatterns = [

    path("profile_details/", views.profile_details, name = "profile_details"),


]

import profiles.signals