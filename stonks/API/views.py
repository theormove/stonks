from django.shortcuts import render
from rest_framework import viewsets, permissions
from news.models import Article
from users.models import Profile
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, ProfileSerializer, UserSerializer


class ArticleView(viewsets.ModelViewSet): 
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class ProfileView(viewsets.ModelViewSet): 
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

class UserView(viewsets.ModelViewSet): 
	queryset = User.objects.all()
	serializer_class = UserSerializer
# Create your views here.
