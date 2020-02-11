from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
	title = models.CharField(max_length = 1000) 
	category = models.CharField(max_length = 1000, default = 'global')
	source = models.CharField(max_length = 1000)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	image = models.ImageField(upload_to = "", default = None, null = True)

	def __str__(self):
		return self.title

	
