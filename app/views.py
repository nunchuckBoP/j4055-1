from django.shortcuts import render
from django.views.generic import ListView
from app.models import Series
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# have fun.
class SeriesView(LoginRequiredMixin, ListView):
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

        # get the reading objects for the series
        reading_objects = Reading.objects.filter(id=?)

        # set the title of the page
        context['title'] = self.title

        # get the reading model objects
        context['reading'] = Series.objects.all()

        # return the context object
        return context
    # end get_context_data
# end class
