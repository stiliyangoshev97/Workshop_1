from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

# Create your models here.

class Animal(models.Model):
    animal_name = models.CharField(max_length=30, blank=True)
    is_mammal = models.BooleanField(default=False)
    animal_photo = models.ImageField(upload_to="animals", blank=True)

    def __str__(self):
        return self.animal_name


class OtherPhotos(models.Model):
    photo = models.ImageField(
        upload_to='animals/other_photos',
        blank=True
    )

    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE
    )

    def __str__(self):
        photo_id = self.id
        return "Photo of " + self.animal.animal_name + "with id " + str(photo_id)

# connect to user model
class Comment(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)



    def __str__(self):
        return self.animal.animal_name


