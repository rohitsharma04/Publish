from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from articles.models import Article
from django.contrib.auth.models import User


class ArticleResource(ModelResource):
	class Meta:
		queryset = Article.objects.all()
		resource_name = 'article'
		authorization = Authorization()


class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
		