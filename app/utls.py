from django.urls import path
from . import views

url_patterns = [
		path('', views.ReadingIndex.as_view(), name='index'),

		]
