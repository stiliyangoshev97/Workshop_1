from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from profiles import forms

from profiles.forms import ProfileForm
from profiles.models import  Profile

# Create your views here.


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk = request.user.id)

    if request.method == "POST":
        # Instance = profile, means that in the fields of the form
        # we will see the current profile account based on the
        # pk above
        form = ProfileForm(request.POST, instance = profile)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProfileForm(instance = profile)

    context = {"form": form}

    return render(request, "profiles/profile_details.html", context)




