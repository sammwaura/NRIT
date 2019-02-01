from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'about/$', views.about, name='about'),
	url(r'contact/$', views.contact, name='contact'),
	url(r'ourclientele/$', views.OurClientele, name='Our Clientele'),
	# Kama ungekuwa umechop io coursework ungeona ni kwa nini tuko awake hadi saa hizi
	url(r'corevalues/$', views.corevalues, name='corevalues'),

]
 
if settings.DEBUG:
 	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 	