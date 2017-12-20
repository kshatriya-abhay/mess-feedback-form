from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View

from iitgauth.views import WebmailLoginView
# Create your views here.

    # Views for Webmail Login

class LoginView(WebmailLoginView, TemplateView):

    template_name = 'student_portal/login.html'
    success_url = reverse_lazy('home') #url change

class HomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'student_portal/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class LogoutView(LoginRequiredMixin, View):

    login_url = reverse_lazy('login')
    http_method_names = ['get', 'head', 'options']

    def get(self, request):
        auth.logout(request)
        return redirect('login')

        # end of Views for Webmail Login
