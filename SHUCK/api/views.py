from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .serializers import BookSerializer, UserSerializer, \
    PublisherSerializer, AuthorSerializer, UserSignUpSerializer, TokenSerializer,\
    UserLoginSerializer
from rest_framework import viewsets, serializers
from Book.models import Book, Publisher, Author
from user.models import Profile


class BookViewSetByPrimaryKey(viewsets.ModelViewSet) :
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


class BookViewSetByBookName(viewsets.ModelViewSet) :
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'BookName'


class BookViewSetByBookPublisher(viewsets.ModelViewSet) :
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'PublisherName'


class BookViewSetByBookAuthor(viewsets.ModelViewSet) :
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'AuthorName'


class UserViewSetByPrimaryKey(viewsets.ModelViewSet) :
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'


class UserViewSetByUserName(viewsets.ModelViewSet) :
    queryset = Profile.objects.all()
    serializer_class = UserSignUpSerializer
    lookup_field = 'username'


class UserLoginByToken(viewsets.ModelViewSet) :
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    lookup_field = 'key'


class UserLoginByUserName(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer,)

    def retrieve(self, request, format = None):
        username = request.data['username']
        password = request.data['password']
        print(username, password)
        # if Profile.objects.filter(username = username).count() == 0:
        #     raise serializers.ValidationError({
        #         "message" : "wrong username"
        #     })
        # else:
        # u = Profile.objects.get(username = username, password = password)
        u = authenticate(username = username, password = password)
        return Response(UserSerializer(u).data)
        # except Profile.DoesNotExist:
        #     raise serializers.ValidationError({
        #         "message" : "RIDIM"
        #     })
