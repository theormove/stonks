from django.db import models
from django.contrib.postgres.fields import JSONField

class StockPrice(models.Model):
	name = models.CharField(max_length=100, blank=False)
	data = JSONField()
	def __str__(self):
		return self.name
