from django.shortcuts import render
from .models import Post

def home(request):
	context = {
		'news' : Post.objects.all(),
	}
	return render(request,'news/home.html', context)

# Create your views here.

def about(request):
	return render(request,'news/about.html')

def financial(request):
	if request.user.is_anonymous:
		context = {
			'news' : Post.objects.all(),
		}
	else:
		cats = []
		for field in request.user.profile._meta.fields:
			if field.value_from_object(request.user.profile) == True:
				cats.append(field.name)
		articles = []
		for article in Post.objects.all():
			if article.category in cats:
				articles.append(article)
		context = {
			'news' : articles,
		}	
	return render(request, 'news/financial.html', context)	


def rub(request):
	if request.user.is_anonymous:
		context = {
			'news' : Post.objects.all(),
		}
	else:
		cats = []
		for field in request.user.profile._meta.fields:
			if field.value_from_object(request.user.profile) == True:
				cats.append(field.name)
		articles = []
		for article in Post.objects.all():
			if article.category in cats:
				articles.append(article)
		context = {
			'news' : articles,
		}	
	return render(request,'news/rub.html', context)
