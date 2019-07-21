from django.shortcuts import render
from .models import Article
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import ArticleForm, CommentForm
import operator

def index(request):

	templates = 'homepage.html'

	return render(request, templates)

def about(request):

	templates = 'about.html'

	return render(request, templates)


def article_list(request):

	articles = Article.objects.all()

	return render(request, 'article_list.html', {'articles':articles})


def article_details(request, slug):
	
	article = Article.objects.get(slug=slug)
	return render(request,'article_detail.html', {'article':article})

def article_add(request):
	template = "article_add.html"

	if request.method == "POST":
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:article-list'))
	else:
		context = {
			'article_form': ArticleForm(),
		}

	return render(request, template, context)

def article_update(request, slug):
	template = "article_update.html"
	article = Article.objects.get(slug=slug)

	if request.method == "POST":
		form = ArticleForm(request.POST, instance=article)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:article-list'))
	else:
		context = {
			'article_form': ArticleForm(instance=article),
		}

	return render(request, template, context)

def article_delete(request, slug):
	article = Article.objects.get(slug=slug)
	article.delete()
	return HttpResponseRedirect(reverse_lazy("blog:article-list"))

def comment_add(request, slug):
	template = "comment_add.html"
	article = Article.objects.get(slug=slug)

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			o = form.save()
			article.comments.add(o)
		return HttpResponseRedirect(reverse_lazy('blog:article-list'))
	else:
		context = {
			'comment_form': CommentForm(),
		}

	return render(request, template, context)

