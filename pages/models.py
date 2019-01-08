# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Pages(models.Model):
	pages_image = models.ImageField(upload_to = 'pages/')
	
	@classmethod
	get_all_images(cls):
  		images = Pages.images.objects.all()

	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
