from rest_framework import serializers
from django.contrib.auth.models import User as DjangoUser
from Book.models import Publisher, Book, Author, Translator
from rest_framework.fields import Field
from user.models import User

class PrimaryPublisherSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Publisher
        fields = ['id', 'PublisherName']


class PrimaryAuthorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Author
        fields = ['id', 'AuthorName']



class TranslatorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Translator
        fields = ['id', 'TranslatorName']


class PrimaryBookSerializer(serializers.ModelSerializer) :
#     BookPublisher = PrimaryPublisherSerializer()
    # BookAuthor = PrimaryAuthorSerializer()
    # BookTranslator = TranslatorSerializer()

    class Meta :
        model = Book
        fields = ['id', 'BookName', 'BookSummary',  'BookImage']
                  # 'BookAuthor', 'BookTranslator']
class BookSerializer(serializers.ModelSerializer) :
    # BookAuthor = PrimaryAuthorSerializer()
    # BookTranslator = TranslatorSerializer()
    BookPublisher = PrimaryPublisherSerializer()
    class Meta :
        model = Book
        fields = ['id', 'BookName', 'BookSummary', 'BookPublisher', 'BookImage']
                  # 'BookAuthor', 'BookTranslator']


class PublisherSerializer(serializers.ModelSerializer) :
    PublisherBooks = serializers.SerializerMethodField('getBooks')
    def getBooks(self, Publisher):
            return Book.objects.filter(BookPublisher = Publisher).values('BookName', 'id')
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

