from django import forms

from django.forms import ModelForm

from django.contrib.auth import authenticate, get_user_model

from django.contrib.auth.forms import UserCreationForm

from django.core.exceptions import ValidationError

# We are using again the get_user_model()
UserModel = get_user_model()

class RegisterForm(UserCreationForm):
	class Meta:
		model = UserModel
		fields = ("email",)


class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(max_length = 15, widget=forms.PasswordInput())

	def clean_password(self):
		self.user = authenticate(
			email = self.cleaned_data['email'],
			password = self.cleaned_data['password'],
		)

		if not self.user:
			raise ValidationError("Username or Password not correct")

	def save(self):
		return self.user



