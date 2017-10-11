from rest_framework import serializers
from django.contrib.auth.models import User as DjangoUser
from Book.models import Publisher, Book, Author, Translator
from user.models import User

class PublisherSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Publisher
        fields = ['id', 'PublisherName']


class AuthorSerializer(serializers.ModelSerializer) :

    def create(self, validated_data):
        a = Author
        a.AuthorName = validated_data.get("AuthorName")

    class Meta :
        model = Author
        fields = ['id', 'AuthorName']


class AuthorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Author
        fields = ['id', 'AuthorName']


class TranslatorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Translator
        fields = ['id', 'TranslatorName']


class BookSerializer(serializers.ModelSerializer) :
    BookPublisher = PublisherSerializer()
    BookAuthor = AuthorSerializer()
    BookTranslator = TranslatorSerializer()

    # def create(self, validated_data):
    #     b = Book()
    #     b.BookName = validated_data.get("BookName")
    #     b.BookSummary = validated_data.get("BookSummary")
    #     b.BookAuthor = AuthorSerializer.create(validated_data)
    #     b.BookPublisher = validated_data.get("BookPublisher")
    #     b.BookTranslator = validated_data.get("BookTranslator")


    class Meta :
        model = Book
        fields = ['id', 'BookName', 'BookSummary', 'BookPublisher',
                  'BookAuthor', 'BookTranslator', 'BookImage']

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

