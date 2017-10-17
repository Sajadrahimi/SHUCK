from django.shortcuts import render
from .serializers import BookSerializer, UserSerializer, DjangoUserSerializer
from rest_framework import viewsets
from Book.models import Book
from user.models import User
from django.contrib.auth.models import User as DjangoUser

class BookViewSetByPrimaryKey(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

class BookViewSetByBookName(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'BookName'

class BookViewSetByBookPublisher(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'BookPublisher'

class BookViewSetByBookAuthor(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'BookAuthor'


class UserViewSetByName(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'name'
