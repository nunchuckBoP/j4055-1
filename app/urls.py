from django.urls import path
from . import views

url_patterns = [

		path(r'^index/$', SeriesView.as_view(), name='series_index'),

		]
