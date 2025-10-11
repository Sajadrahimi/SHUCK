from rest_framework import serializers
from django.contrib.auth.models import User as DjangoUser
from Book.models import Publisher, Book, Author, Translator
from user.models import User

class PrimaryPublisherSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Publisher
        fields = ['id', 'PublisherName', 'PublisherBooks']


class PrimaryAuthorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Author
        fields = ['id', 'AuthorName']



class TranslatorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Translator
        fields = ['id', 'TranslatorName']


class BookSerializer(serializers.ModelSerializer) :
    BookPublisher = PrimaryPublisherSerializer()
    BookAuthor = PrimaryAuthorSerializer()
    BookTranslator = TranslatorSerializer()

    class Meta :
        model = Book
        fields = ['id', 'BookName', 'BookSummary', 'BookPublisher',
                  'BookAuthor', 'BookTranslator', 'BookImage']
class PrimaryBookSerializer(serializers.ModelSerializer) :
    BookAuthor = PrimaryAuthorSerializer()
    BookTranslator = TranslatorSerializer()

    class Meta :
        model = Book
        fields = ['id', 'BookName', 'BookSummary',
                  'BookAuthor', 'BookTranslator', 'BookImage']

class PublisherSerializer(serializers.ModelSerializer) :
    PublisherBooks = BookSerializer()
    class Meta :
        model = Publisher
        fields = ['id', 'PublisherName', 'PublisherBooks']

class AuthorSerializer(serializers.ModelSerializer) :
    AuthorBooks = BookSerializer()
    class Meta :
        model = Author
        fields = ['id', 'AuthorName', 'AuthorBooks']

class DjangoUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjangoUser
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    django_user = DjangoUserSerializer()
    books = BookSerializer()
    class Meta :
        model = User
        # fields = ['id', 'django_user','name', 'family_name',
        #           'location', 'phone_number', 'bio', 'birth_date']
        fields = '__all__'

