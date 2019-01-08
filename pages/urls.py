from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url('^$', views.home, name='home'),
	url('about/', views.about, name='about'),
	url('contact/', views.contact, name='contact'),
	url('Our Clientele/', views.OurClientele, name='Our Clientele'),
]
 
if settings.DEBUG:
 	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 	