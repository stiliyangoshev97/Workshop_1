from animals.models import Animal, Comment, OtherPhotos

from django.forms import ModelForm
from django import forms


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ("animal_name", "is_mammal", "animal_photo")

        widgets = {
            "animal_name": forms.TextInput(attrs={'class': 'form-control'}),
            "animal_photo": forms.FileInput(attrs={'class': 'custom-file-input'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)


        widgets = {
            "text": forms.Textarea(attrs={'class': 'form-control'}),
        }


class AddPhotosForm(ModelForm):
    class Meta:
        model = OtherPhotos
        fields = ("photo",)

        widgets = {
            "photo": forms.FileInput(attrs={'class': 'custom-file-input'}),
        }



























