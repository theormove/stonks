from django.shortcuts import render
from .models import Post


def home(request):
	context = {
		'news' : Post.objects.all()
	}
	return render(request,'news/home.html', context)

# Create your views here.

def about(request):
	return render(request,'news/about.html')