from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	subscription_plan = models.CharField(max_length = 100, default = "NONE", blank = True)
	categories = models.TextField()
	recieve_source = models.TextField()
	category = models.BooleanField(default = True)
	glob = models.BooleanField('Global', default = True)

	rub = models.BooleanField('RUB', default = True)
	gbp = models.BooleanField('GBP', default = True)
	usd = models.BooleanField('USD', default = True)
	eur = models.BooleanField('EUR', default = True)
	cny = models.BooleanField(default = True)

	nyse_composite = models.BooleanField(default = True)
	sp_500 = models.BooleanField(default = True)
	nasdaq_100 = models.BooleanField(default = True)
	russel_2000 = models.BooleanField(default = True)
	nikkei_225 = models.BooleanField(default = True)

	crude_oil = models.BooleanField(default = True)
	natural_gas = models.BooleanField(default = True)
	brent_crude = models.BooleanField(default = True)
	coal = models.BooleanField(default = True)

	gold = models.BooleanField(default = True)
	silver = models.BooleanField(default = True)
	platinum = models.BooleanField(default = True)
	iron = models.BooleanField(default = True)
	copper = models.BooleanField(default = True)

	corn = models.BooleanField(default = True)
	soybean = models.BooleanField(default = True)
	cattle = models.BooleanField(default = True)
	sugar = models.BooleanField(default = True)

	bitcoin = models.BooleanField(default = True)
	ethereum = models.BooleanField(default = True)
	dash = models.BooleanField(default = True)
	litecoin = models.BooleanField(default = True)
	zash = models.BooleanField(default = True)
	monero = models.BooleanField(default = True)
	ripple = models.BooleanField(default = True)

	telegram = models.BooleanField(default = True)
	email = models.BooleanField(default = True)
	viber = models.BooleanField(default = True)

	def __str__(self):
		return f'{self.user.username} Profile'