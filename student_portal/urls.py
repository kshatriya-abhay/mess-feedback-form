from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'home/$', views.HomeView.as_view(), name='home'),
    url(r'logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'messfeedback/$', views.check_filled, name='feedback'),
    url(r'messfeedback/new$', views.NewFeedback.as_view(), name='new_feedback'),
    url(r'messfeedback/update$', views.UpdateFeedback.as_view(), name='update_feedback'),
    url(r'preference/new$', views.NewPreference.as_view(), name='new_preference'),

]
