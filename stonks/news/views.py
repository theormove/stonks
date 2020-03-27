from django.shortcuts import render
from .models import Article


def home(request):
	if request.user.is_anonymous:
		context = {
			'news' : Article.objects.all(),
		}
	else:
		cats = []
		for field in request.user.profile._meta.fields:
			if field.value_from_object(request.user.profile) == True:
				cats.append(field.name)
		arts = []
		for art in Article.objects.all():
			for cat in  art.category:
				if cat in cats:
					arts.append(art)
		context = {
			'news' : arts,
		}	
	return render(request,'news/home.html', context)

# Create your views here.

def about(request):
	return render(request,'news/about.html')

def financial(request):
	if request.user.is_anonymous:
		context = {
			'news' : Article.objects.all(),
		}
	else:
		cats = []
		for field in request.user.profile._meta.fields:
			if field.value_from_object(request.user.profile) == True:
				cats.append(field.name)
		arts = []
		for art in Article.objects.all():
			for cat in  art.category:
				if cat in cats:
					arts.append(art)
		context = {
			'news' : arts,
		}	
	return render(request, 'news/financial.html', context)	


def rub(request):
	if request.user.is_anonymous:
		context = {
			'news' : Article.objects.all(),
		}
	else:
		cats = []
		for field in request.user.profile._meta.fields:
			if field.value_from_object(request.user.profile) == True:
				cats.append(field.name)
		arts = []
		for art in Article.objects.all():
			for cat in  art.category:
				if cat in cats:
					arts.append(art)
		context = {
			'news' : arts,
		}	
	return render(request,'news/rub.html', context)
