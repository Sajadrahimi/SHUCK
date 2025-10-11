from django.shortcuts import render
from .serializers import BookSerializer, UserSerializer, DjangoUserSerializer
from rest_framework import viewsets
from Book.models import Book
from user.models import User
from django.contrib.auth.models import User as DjangoUser

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DjangoUserViewSet(viewsets.ModelViewSet):
    queryset = DjangoUser.objects.all()
    serializer_class = DjangoUserSerializer
