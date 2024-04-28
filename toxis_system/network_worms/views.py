from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import NetWormsArticle

def networkWorms(request): # HttpResponse
	return render(request, 'network_worms/worms.html')


def article(request, article_slug):
	post = get_object_or_404(NetWormsArticle, title=article_slug)

	data = {
		'title': post.title,
		'content': post.content,
		'post': post
	}

	return render(request, 'network_worms/worms_article.html', data)