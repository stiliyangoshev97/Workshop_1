from django import forms

from profiles.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('id', 'is_complete')