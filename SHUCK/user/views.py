from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as DjangoLogin
from django.http import request, HttpResponse

from Book.models import Book
from rest_framework.authtoken.models import Token

from .models import Profile, Shelf
from .forms import SignUpForm
from django.template import loader


def login(request) :
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username = username, password = password)

    # if user is not None and request.POST["g-recaptcha-response"] != '':
    if user is not None:
        print("VERIFIED")
        DjangoLogin(request, user)
        return HttpResponse("Logged in")
    # elif request.POST["g-recaptcha-response"] == '':
    #     return HttpResponse("You Bastard ROBOT")
    else :
        return HttpResponse("Wrong Username or Password")


def getReads(request):
    print("**********************")
    books = Profile.objects.filter(username = 'sajad2').values('Reads')
    out = []
    for b in books:
        book = Book.objects.get(pk = b['Reads'])
        out.append(book)
    return HttpResponse(out)
def getReads(request):
    print("**********************")
    books = Profile.objects.filter(username = 'sajad2').values('Reads')
    out = []
    for b in books:
        book = Book.objects.get(pk = b['Reads'])
        out.append(book)
    return HttpResponse(out)
def getToReads(request):
    print("**********************")
    books = Profile.objects.filter(username = 'sajad2').values('toReads')
    out = []
    for b in books:
        book = Book.objects.get(pk = b['toReads'])
        out.append(book)
    return HttpResponse(out)
def getReadings(request):
    print("**********************")
    books = Profile.objects.filter(username = 'sajad2').values('Readings')
    out = []
    for b in books:
        book = Book.objects.get(pk = b['Readings'])
        out.append(book)
    return HttpResponse(out)

def registration(request):
    if request.method == 'POST':
        print("is POST")
        form = SignUpForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            first_name = "" #form.cleaned_data.get("first_name")
            last_name = "" #form.cleaned_data.get("last_name")
            email = "" #form.cleaned_data.get("email")
            print(username, password, first_name, last_name)
            u = Profile.objects.create(username = username, password = password,
                                       email = email, first_name = first_name,
                                       last_name = last_name)
            u.save()
            u.token = Token.objects.create(user = u)
            u.save()
            return HttpResponse("Hello " + u.username)

        else:
            print(form.cleaned_data.get('password1'), form.cleaned_data.get('password2'))
            return HttpResponse(form.error_messages)

def loign_form(request) :

    template = loader.get_template('user/login.html')
    return HttpResponse(template.render({}, request))

def registration_form(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'user/registration_form.html', {'form' : form})

