from django.shortcuts import render
from pages.models import Pages  

def home(request):
	images = Pages.get_all_images()

	return render(request, "home.html", {'images':images})


def about(request):
	return render(request, "about.html", {})


def contact(request):
	return render(request, "contact.html", {})

def OurClientele(request):
	return render(request, "Our Clientele.html", {})

