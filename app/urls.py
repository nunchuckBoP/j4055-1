from django.urls import path, re_path
from app.views import ReadingView, SeriesView, LoginView, LogoutView
from django.contrib import admin

urlpatterns = [
                  re_path(r'^$', SeriesView.as_view(), name='series_list'),
                  re_path(r'^reading/$', ReadingView.as_view(), name='reading_list'),
                  re_path(r'^admin/', admin.site.urls),
                  re_path(r'^login/$', LoginView.as_view(), name='login'),
                  re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
              ]
