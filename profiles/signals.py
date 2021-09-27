# Signal is basically a code executed depending on a condition
# we can use it to bind the User model to the Profile model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from profiles.models import Profile

UserModel = get_user_model()

# When User model is being created, I want to execute the
# function bellow

#We do this after saving the information in the model
@receiver(post_save, sender = UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = Profile(
            # Relation from profiles.views, OneToOneField with User model
            id=instance

        )
        profile.save()

# We do this before saving the information in the model
# in pre-save we do not have created
@receiver(pre_save, sender = Profile)
def check_is_complete(sender, instance, **kwargs):
    if instance.first_name and instance.last_name and instance.age:
        instance.is_complete = True
    else:
        instance.is_complete = False


# Signals are used when we always wants in a certain situation
# to make something happen. It's also used for verifying the email
# address
