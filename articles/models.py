from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models

import itertools
from django.utils.text import slugify


# Create your models here.
class Article(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=120)
	content = models.TextField(null=True,blank=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now = False)
	updated = models.DateTimeField(auto_now_add=False,auto_now = True)
	active = models.BooleanField(default=True)

	class Meta:
		unique_together = ('title', 'slug')

	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse("single_article",kwargs={"slug":self.slug})

	def edit_article_url(self):
		return reverse("edit_article",kwargs={"slug":self.slug})

from django.forms import ModelForm

class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ['title','content']

	def save(self,user,commit=True):
		instance = super(ArticleForm, self).save(commit=False)
		max_length = Article._meta.get_field('slug').max_length
		instance.slug = orig = slugify(instance.title)[:max_length]
		instance.user = user
		for x in itertools.count(1):
			if not Article.objects.filter(slug=instance.slug).exists():
				break
			instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)
		instance.save()
		return instance

	def save(self,commit=True):
		instance = super(ArticleForm, self).save(commit=False)
		instance.save()
		return instance

