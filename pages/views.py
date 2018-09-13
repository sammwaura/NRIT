from django.shortcuts import render

def home(request):
	return render(request, "home.html", {})


def home(request):
	return render(request, "about.html", {})


def home(request):
	return render(request, "contact.html", {})

