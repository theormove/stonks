from django.shortcuts import render
from rest_framework import viewsets, permissions
from news.models import Article
from users.models import Profile
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, ProfileSerializer, UserSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS

class isOwner(BasePermission):
	def has_object_permission(self, request, view, obj):
		return	obj.user == request.user 


class ArticleView(viewsets.ModelViewSet): 
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


class ProfileView(viewsets.ModelViewSet): 
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = [isOwner,]

class UserView(viewsets.ModelViewSet): 
	queryset = User.objects.all()
	serializer_class = UserSerializer
	#permission_classes = [isOwner,]
# Create your views here.
