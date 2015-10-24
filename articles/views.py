from django.contrib.auth.models import User
from django.shortcuts import render, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
# Create your views here.
from articles.models import Article,ArticleForm

def home(request):
	articles = Article.objects.order_by('-updated').all()
	context = {'articles':articles}
	template = "home.html"
	return render(request,template,context)



#For Single Article
def single_article(request, slug):
	#try:
	article = Article.objects.get(slug=slug)
	context = {'article':article}
	template = 'articles/single_article.html'
	return render(request,template,context)
	# except:
	# 	raise Http404

def search_article(request):
	query = request.GET.get('query')

	if query:
		articles = Article.objects.filter(title__icontains=query).order_by('-updated').all()
		context = {'articles':articles}
		template = "articles/search_articles.html"
		return render(request,template,context)
	else:
		return HttpResponseRedirect(reverse("home"))


@login_required(login_url='/login')
def user_home(request):
	form = ArticleForm(request.POST or None)
	if form.is_valid():
		new_article = form.save(user=request.user,commit=False)
		new_article.save()
		return HttpResponseRedirect(reverse("user_home"))

	context = {'form':form}
	template = "articles/userhome.html"
	return render(request,template,context)


@login_required(login_url='/login')
def my_articles(request):
	articles = Article.objects.filter(user=request.user).order_by('-updated').all()
	context = {'articles':articles}
	template = "articles/my_articles.html"
	return render(request,template,context)
