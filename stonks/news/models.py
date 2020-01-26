from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length = 100) 
	category = models.CharField(max_length = 100)
	source = models.CharField(max_length = 100)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	image = models.FileField(upload_to = "", null = True)

	def __str__(self):
		return self.title