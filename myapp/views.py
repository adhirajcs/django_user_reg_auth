from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
	return render(request, 'myapp/index.html')


def register(request):
	return render(request, 'myapp/register.html')


def my_login(request):
	return render(request, 'myapp/my-login.html')


def dashboard(request):
	return render(request, 'myapp/dashboard.html')
