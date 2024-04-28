from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string


def index(request): # HttpResponse
	# t = render_to_string('main_page/index.html')
	# return HttpResponse(t)
	return render(request, 'main_page/index.html')


# def page_not_found(request, exeption):
# 	return HttpResponseNotFound("<h1>Страница не найдена!!!</h1>")