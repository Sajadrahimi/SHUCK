from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login$', auth_views.login, {'template_name': 'core/cover.html'}, name = 'login'),
    url(r'^logout/', auth_views.logout, {'next_page' : '/'}, name = 'logout'),
    url(r'^register/$', views.registration_form, name = "signup"),
    url(r'^register/submit_registration/$', views.registration),
    # url(r'^getReads/$', views.getReads),
    # url(r'^getReadings/$', views.getReadings),
    # url(r'^getToReads/$', views.getToReads),
    # url(r'^', views.loign_form, name = "Login Form"),


]
