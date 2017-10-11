
from django.shortcuts import render
from django.contrib.auth import authenticate, login as DjangoLogin, logout
from django.http import request, HttpResponse
from .forms import SignUpForm
from django.template import loader


# Login and check re-Captcha
def login(request) :
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username = username, password = password)

    if user is not None and request.POST["g-recaptcha-response"] != '':
        print("VERIFIED")
        DjangoLogin(request, user)
        return HttpResponse("Logged in")
    elif request.POST["g-recaptcha-response"] == '':
        return HttpResponse("You Bastard ROBOT")
    else :
        return HttpResponse("Wrong Username or Password")

# Registration and Automatic Login
def registeration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username = username, password = password)
            DjangoLogin(request, user)
            return HttpResponse("Signed Up " + username + " as " + form.cleaned_data.get("name") + "<img src = "
                                                                                                   "\"+ reuqest.FILES +\"/>")

        else:
            return HttpResponse(form.error_messages)
#Loads Login Form
def loign_form(request) :
    template = loader.get_template('user/login_form.html')
    return HttpResponse(template.render({}, request))

#Loads Registration Form
def registration_form(request):

    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'user/registration_form.html', {'form' : form})

