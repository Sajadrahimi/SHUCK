from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login as DjangoLogin, logout
from django.http import request, HttpResponse
from .forms import SignUpForm
from django.template import loader


def login(request) :
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username = username, password = password)

    if user is not None :
        print("VERIFIED")
        DjangoLogin(request, user)
        return HttpResponse("Logged in")
    else :
        # ERR
        return HttpResponse("Wrong username or password")

def registeration(request):
    #
    # name = request.POST.get("name")
    # family_name = request.POST.get("family_name")
    # phone_number = request.POST.get("phone_number")
    # bio = request.POST.get("bio")
    # location = request.POST.get("location")
    # birth_date = request.POST.get("birth_date")
    #
    if request.method == 'POST':
        print("_________________ I'm HERE ________________")
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("_____________ Form is Valid _____________")
            form.save()
            print("_____ PASSWORD: ", form.cleaned_data.get("password"))
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username = username, password = password)
            DjangoLogin(request, user)
            return HttpResponse("Signed Up " + username + " as " + form.cleaned_data.get("name"))

        else:
            return HttpResponse(form.error_messages)

def loign_form(request) :
    template = loader.get_template('user/login_form.html')
    return HttpResponse(template.render({}, request))

def registration_form(request):
    # template = loader.get_template("user/registration_form.html")
    # return HttpResponse(template.render({}, request))
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'user/registration_form.html', {'form' : form})
