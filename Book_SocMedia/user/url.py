from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login, name = "Login"),
    url(r'^register/$', views.registration_form, name = "Registeration Form"),
    url(r'^submit_registration/$', views.registeration, name = "Registration"),
    url(r'^', views.loign_form, name = "Login Form"),
]
