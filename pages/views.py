from django.shortcuts import render
from django.pages import views  

def home(request):
	images = Image.get_all_images()

	return render(request, "home.html", {'images':images})


def about(request):
	return render(request, "about.html", {})


def contact(request):
	return render(request, "contact.html", {})

def OurClientele(request):
	return render(request, "Our Clientele.html", {})

