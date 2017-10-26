from rest_framework import serializers
from django.contrib.auth.models import User as DjangoUser
from Book.models import Publisher, Book, Author, Translator
from rest_framework.fields import Field
from user.models import User


class PublisherSerializer(serializers.ModelSerializer) :
    PublisherBooks = serializers.SerializerMethodField('getBooks')

    def getBooks(self, Publisher):
            return Book.objects.filter(BookPublisher = Publisher).values('id', 'BookName')
    class Meta :
        model = Publisher
        fields = ['id', 'PublisherName', 'PublisherBooks']


class PrimaryPublisherSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Publisher
        fields = ['id', 'PublisherName']


class AuthorSerializer(serializers.ModelSerializer):
    AuthorBooks = serializers.SerializerMethodField('getBooks')

    def getBooks(self, Author):
        return Book.objects.filter(BookAuthor = Author).values("id", "BookName")

    class Meta :
        model = Author
        fields = ["id", 'AuthorName', 'AuthorBooks']


class PrimaryAuthorSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Author
        fields = ['id', 'AuthorName']


class TranslatorSerializer(serializers.ModelSerializer) :
    TranslatorBooks = serializers.SerializerMethodField('getBooks')

    def getBooks(self, Translator) :
        return Book.objects.filter(BookTranslator = Translator).values("id", "BookName")

    class Meta :
        model = Translator
        fields = ['id', 'TranslatorName', 'TranslatorBooks']

class PrimaryTranslatorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Translator
        pass



class BookSerializer(serializers.ModelSerializer) :
    BookAuthor = PrimaryAuthorSerializer()
    BookTranslator = TranslatorSerializer()
    BookPublisher = PrimaryPublisherSerializer()
    class Meta :
        model = Book
        fields = ['id', 'BookName', 'BookAuthor', 'BookTranslator','BookPublisher',
                  'BookSummary',  'BookPageCount',  'BookImage']


# class PrimaryBookSerializer(serializers.ModelSerializer) :
#     BookPublisher = PrimaryPublisherSerializer()
#     BookAuthor = PrimaryAuthorSerializer()
#     BookTranslator = TranslatorSerializer()
#
#     class Meta :
#         model = Book
#         fields = ['id', 'BookName', 'BookSummary',  'BookImage'
#                     , 'BookAuthor', 'BookTranslator']

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

