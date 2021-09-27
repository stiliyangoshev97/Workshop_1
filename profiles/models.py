from django.contrib.auth import get_user_model
from django.db import models

# We must use get_user_model() and not the original User model
# because the original User model should remain pure
UserModel = get_user_model()

# Create your models here.

class Profile(models.Model):
	first_name = models.CharField(
		max_length = 24,
		blank = True,
	)
	last_name = models.CharField(
		max_length = 24,
		blank=True,
	)
	age = models.IntegerField(
		null=True,
	)
	profile = models.ImageField(
		upload_to = 'profiles',
		blank=True,
	)

	user = models.OneToOneField(
		UserModel,
		on_delete = models.CASCADE,
		primary_key = True,
		name = 'id',
	)

	is_complete = models.BooleanField(
		default = False,
	)

	def __str__(self):
		return self.first_name


