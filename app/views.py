from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from app.models import Series
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# have fun.
class SeriesView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Series
    title = "Series List"
    template_name = "series_index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # set the title of the page
        context['title'] = self.title

        # get the series model objects
        context['series'] = Series.objects.all().order_by('-id')

        # return the context object
        return context

    # end get_context_data
# end class

class ReadingView(LoginRequiredMixin, ListView):
    model = Reading
    title = "Reading List"
    template_name = "reading_index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        _series = context['object']

        # get the reading objects for the series
        reading_objects = Reading.objects.filter(series=_series)

        # set the title of the page
        context['title'] = self.title

        # get the reading model objects
        context['reading'] = Series.objects.all()

        # return the context object
        return context
    # end get_context_data
# end class
