from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from animals.models import Animal, OtherPhotos, Comment

from animals.forms import AnimalForm, CommentForm, AddPhotosForm


# Create your views here.


def list_animals(request):
    animals = Animal.objects.all()

    context = {
        "animals": animals,
    }

    return render(request, "animals/list_animals.html", context)

def create_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = AnimalForm()

    context = {
        "form": form,
    }

    return render(request, "animals/create_animals.html", context)

@login_required
def animal_details(request, pk):
    animal = Animal.objects.get(pk = pk)

    context = {"animal": animal}

    return render(request, 'animals/animal_details.html', context)


def animal_photos(request, animal_name):
    animals_photos = OtherPhotos.objects.all()
    animal = Animal.objects.get(animal_name = animal_name)


    context = {
        "animals_photos": animals_photos,
        "animal": animal
    }

    return render(request, 'animals/animals_photos.html', context)



def update_animal(request, pk):
    animal = Animal.objects.get(pk = pk)

    if request.POST:
        form = AnimalForm(request.POST, request.FILES, instance=animal)

        if form.is_valid():
            form.save()
            return redirect("animals:animals_list")
    else:
        form = AnimalForm(instance=animal)

    context = {
        "form": form,
        "animal": animal,
    }

    return render(request, "animals/update_animals.html", context)

def delete_animal(request, pk):
    animal = Animal.objects.get(pk=pk)
    animal.delete()

    return redirect("animals:animals_list")


# Make a comment for a specific animal by a specific user
def CommentView(request, pk):
    animal = Animal.objects.get(pk=pk)
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            # Comment is now the form with the posted data but still not committed to the database
            comment = form.save(commit=False)
            comment.user = request.user
            comment.animal = animal
            comment.save()
            return redirect("index")
    else:
        form = CommentForm()

    context = {"comment_form": form}

    return render(request, "animals/comment_form.html", context)


def CommentsList(request, pk):
    comments = Comment.objects.all()
    animal = Animal.objects.get(pk=pk)

    # We only want to filter the comments where the object animal of comments is equal to the
    # animal we are currently viewing in the template
    # and its compared by its primary key
    for comment in comments:
        comments = Comment.objects.filter(animal=animal)


    context = {
        "comments": comments,
        "animal": animal,
               }

    return render(request, "animals/animal_details.html", context)


# Photo is being added according to the animal
def add_photos(request,pk):
    animal = Animal.objects.get(pk=pk)
    if request.POST:
        form = AddPhotosForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.animal = animal
            photo.save()
            return redirect("index")
    else:
        form = AddPhotosForm()

    context = {
        "add_photos_form": form,
    }

    return render(request, "animals/add_photos.html", context)



