from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as DjangoLogin
from django.http import request, HttpResponse
from .models import User, Shelf
from .forms import SignUpForm
from django.template import loader


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


def registration(request):
    if request.method == 'POST':
        print("is POST")
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            print(username, password, first_name, last_name)
            # user = authenticate(username = username, password = password,
            #                     first_name = first_name, last_name = last_name)
            # print("************", user)
            u = User.objects.create(username = username, password = password)
            u.save()
            # u.shelves.objects.create(shelf_name = 'Read')
            return HttpResponse("Hello " + u.username)

        else:
            return HttpResponse(form.error_messages)

def loign_form(request) :
    template = loader.get_template('user/login_form.html')
    return HttpResponse(template.render({}, request))

def registration_form(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'user/registration_form.html', {'form' : form})

