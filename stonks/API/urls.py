from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = routers.DefaultRouter()
router.register('article', views.ArticleView)
router.register('profile', views.ProfileView)
router.register('stock', views.StockPriceView)
urlpatterns = [
	path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
   	path('auth/', include('djoser.urls')),
]
