from rest_framework.authtoken.models import Token
from .serializers import BookSerializer, UserSerializer,\
    PublisherSerializer, AuthorSerializer, UserSignUpSerializer, TokenSerializer
from rest_framework import viewsets
from Book.models import Book, Publisher, Author
from user.models import Profile

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


class UserViewSetByPrimaryKey(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

class UserViewSetByUserName(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSignUpSerializer
    lookup_field = 'username'


class UserLoginByToken(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    lookup_field = 'key'
