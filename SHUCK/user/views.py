from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import login as DjangoLogin
from django.http import request, HttpResponse

from Book.models import Book
from rest_framework.authtoken.models import Token
from feeds.models import Feed
from .models import Profile
from .forms import SignUpForm
from django.template import loader


def login(request) :
    print("+++++++++++++++ CALLED")
    print(request.POST)
    username = request.POST.get("username")
    password = request.POST.get("password")
    print("USERNAME: ", username)
    print("PASSWORD: ", password)
    user = authenticate(request, username = username, password = password)

    if user is not None:
        DjangoLogin(request, user)
        return redirect('/feeds/feeds')

    else :
        return HttpResponse("Wrong Username or Password")


def registration(request):
    if request.method == 'POST':
        print("is POST: ", request.POST)
        form = SignUpForm(request.POST)
        print("FORM: ", form)
        if form.is_valid():
            print("FORM IS VALID")
        username = form.cleaned_data.get("username", "")
        password = form.cleaned_data.get("password")
        first_name = form.cleaned_data.get("first_name")
        last_name = "" #form.cleaned_data.get("last_name")
        email = "" #form.cleaned_data.get("email")
        print("USERNAME: ", username)
        print("PASSWORD: ", password)
        Profile.objects.create_user(username = username, password = password,
                                 email = email)
        user = authenticate(username = username, password = password)
        auth_login(request, user)
        welcome_post = '{0} has joined SHUCK.'.format(user.username)
        feed = Feed(user = user, post = welcome_post)
        feed.save()
        return redirect('/')
# else:
#     pass
#
def loign_form(request) :

    template = loader.get_template('user/login.html')
    return HttpResponse(template.render({}, request))

def registration_form(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'user/signup.html', {'form' : form})

