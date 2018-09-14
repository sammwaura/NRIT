from django.conf.urls import url
from . import views

urlpatterns = [
	url('^$', views.home, name='home'),
	url('about/', views.about, name='about'),
	url('contact/', views.contact, name='contact'),
	url('Our Clientele/', views.OurClientele, name='Our Clientele'),
]