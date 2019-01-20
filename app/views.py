from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.base import RedirectView
from django.views.generic import ListView, FormView, View
from app.models import Reading, Series
from app.forms import LoginForm
from braces import views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(FormView, views.AnonymousRequiredMixin):
    form_class = LoginForm
    success_url = reverse_lazy('series_list')
    template_name = 'app/login.html'
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)
        # end if
    # end form_valid
# end LoginView


class LogoutView(RedirectView, views.LoginRequiredMixin):
    url = reverse_lazy('login')
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
    # end get
# end LogoutView


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

class ReadingView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    title = "Reading List"
    template_name = "app/reading_list.html"

    def get(self, request, pk, *args, **kwargs):

       if request.user.is_authenticated:
           series = get_object_or_404(Series, pk=pk)
           readings = Reading.objects.filter(series=series)
           context = {"reading":readings, "title":self.title}
           return render(request, self.template_name, context)
       else:
           return HttpResponseRedirect(reverse_lazy('login'))
       # end if
    # end get
# end class
