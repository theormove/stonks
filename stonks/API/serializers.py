from rest_framework import serializers
from news.models import Article
from users.models import Profile
from django.contrib.auth.models import User

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Article
		read_only_fields = ('id','title','category','source','content','date_posted')
		fields = '__all__'

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Profile
		read_only_fields = ('subscription_plan','url','url','id')
		fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		read_only_fields = ('date_joined','url','id',)
		fields = ('email','first_name','last_name','username','date_joined','url','id',)
