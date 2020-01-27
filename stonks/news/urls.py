from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'news-home'),
    path('about/', views.about, name = 'news-about'),
    path('financial/', views.financial, name = 'news-financial'),
    path('markets/rub/', views.rub, name = 'news-rub'),
]
