from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout


from accounts.forms import LoginForm, RegisterForm
from django.urls import reverse 

from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
	if request.POST:
		form = RegisterForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect("index")

	else:
		form = RegisterForm()

	context = {
		"form": form,
	}
	return render(request, "accounts/register.html", context)

def sign_in(request):
	if request.POST:
		form = LoginForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('index')
	else:
		form = LoginForm()

	context = {"form": form}

	return render(request, 'accounts/login.html', context)

''' 	
	user = authenticate(username = "admin", password = "admin")
	login(request, user)
	return redirect("index")
'''
@login_required
def sign_out(request):
	logout(request)
	return redirect("index")