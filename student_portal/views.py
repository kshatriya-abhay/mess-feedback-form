from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView, UpdateView

from iitgauth.views import WebmailLoginView
from .models import *
from datetime import datetime
# Create your views here.

    # Views for Webmail Login

class LoginView(WebmailLoginView, TemplateView):

    template_name = 'student_portal/login.html'
    success_url = reverse_lazy('home') #url change

    # toggle below 3 lines comment status to make login necessary
# class HomeView(LoginRequiredMixin, TemplateView):
class HomeView(TemplateView):
    # login_url = reverse_lazy('login')
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



class NewFeedback(CreateView):
    model = MessFeedback
    fields = ['hostelName','username','cleanliness','qual_b','qual_l', 'qual_d','catering']
    success_url = reverse_lazy('home')
    # def get(self, request):
    #     tags=['Hostel','User','Cleanliness and Hygiene','Breakfast','Lunch','Dinner','Catering']
    #     tag_count=0
    #
    #     for field in :
    #         field.label_tag = tags[tag_count]
    #         tag_count = tag_count+1;

class UpdateFeedback(UpdateView):
    model = MessFeedback
    fields = ['hostelName','username','cleanliness','qual_b','qual_l', 'qual_d','catering']

def check_filled_feedback(request):
    # use m1, y1, uname to check distinct
    uname = request.user.username
    # request.POST['user']
    # fbform = MessFeedback.objects.get(username=uname) #,month=curr_month,year=curr_year
    if MessFeedback.objects.filter(username=uname).count() == 0:
        # how to pass parameters...
        return redirect('new_feedback')
    if MessFeedback.objects.filter(username=uname).count() == 1:
        # how to pass parameters...
        if MessFeedback.objects.filter(username=uname,month=m1,year=y1).count() == 1:
            return redirect('update_feedback')
        else:
            return redirect('new_feedback')

    #ideally this should not happen
    return redirect('home')

class NewPreference(CreateView):
    model = Preference
    fields = ['hostelName','username','h1','h2','h3']
    success_url = reverse_lazy('home')
    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
    # Find out which variable would be storing the fields value
# See once line no.826 in django/forms/fields.py

def check_filled_preference(request):
    # use m2, y2, uname to check distinct
    # Extract current mess subscription from HAB database
    return redirect('new_preference')
