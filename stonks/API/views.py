from django.shortcuts import render
from rest_framework import viewsets, permissions
from news.models import Article
from users.models import Profile
from .models import StockPrice
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, ProfileSerializer, StockPriceSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

		

class IsOwner(BasePermission):
	def has_object_permission(self, request, view, obj):
		return	obj.user == request.user 
class StockPriceView(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication,JWTAuthentication] 
	queryset = StockPrice.objects.all()
	serializer_class = StockPriceSerializer

class ArticleView(viewsets.ModelViewSet):
	authentication_classes = [JWTAuthentication,] 
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


class ProfileView(viewsets.ModelViewSet):
	authentication_classes = [JWTAuthentication,] 
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = [IsOwner,IsAuthenticated]

