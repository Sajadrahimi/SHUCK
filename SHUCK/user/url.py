from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^login/$', views.login, name = "Login"), # Does Login
    url(r'^register/$', views.registration_form, name = "Registeration Form"), # Loads Registration Form
    url(r'^submit_registration/$', views.registeration, name = "Registration"), # Does Registration
    url(r'^', views.loign_form, name = "Login Form"), # Loads Login Form (default)

]
