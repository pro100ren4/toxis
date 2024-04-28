from django.urls import path
from . import views

urlpatterns = [
	path('', views.networkWorms),
	path('<slug:article_slug>', views.article),
]