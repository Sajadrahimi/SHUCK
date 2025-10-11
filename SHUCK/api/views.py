from django.shortcuts import render
from .serializers import BookSerializer, UserSerializer, DjangoUserSerializer, PublisherSerializer, AuthorSerializer
from rest_framework import viewsets
from Book.models import Book, Publisher, Author
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
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'PublisherName'

class BookViewSetByBookAuthor(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'AuthorName'


class UserViewSetByName(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'name'
