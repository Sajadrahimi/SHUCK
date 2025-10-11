from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login, name = "Login"),
    url(r'^register/$', views.registration_form, name = "Registration Form"),
    url(r'^register/submit_registration/$', views.registration, name = "Registration"),
    # url(r'^getReads/$', views.getReads),
    # url(r'^getReadings/$', views.getReadings),
    # url(r'^getToReads/$', views.getToReads),
    url(r'^', views.loign_form, name = "Login Form"),


]
