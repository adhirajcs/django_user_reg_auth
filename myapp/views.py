from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginForm

# Authentication Models and methods
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def homepage(request):
	return render(request, 'myapp/index.html')


def register(request):

	form = CreateUserForm()

	if request.method == "POST":
		form = CreateUserForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect("login")
		
	context = {'registerform': form}

	return render(request, 'myapp/register.html', context=context)


def my_login(request):

	form = LoginForm()

	if request.method == "POST":

		form = LoginForm(request, data=request.POST)

		if form.is_valid():
			username =  request.POST.get('username')
			password =  request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect("dashboard")
	
	context = {'loginform': form}

	return render(request, 'myapp/my-login.html', context=context)


def dashboard(request):
	return render(request, 'myapp/dashboard.html')
