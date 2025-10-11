from rest_framework import serializers
from django.contrib.auth.models import User as DjangoUser
from Book.models import Publisher, Book, Author, Translator
from rest_framework.fields import Field
from rest_framework.response import Response
from user.models import User


class PublisherSerializer(serializers.ModelSerializer) :
    PublisherBooks = serializers.SerializerMethodField('getBooks')

    def getBooks(self, Publisher) :
        return Book.objects.filter(BookPublisher = Publisher).values('id', 'BookName')

    class Meta :
        model = Publisher
        fields = ['id', 'PublisherName', 'PublisherBooks']


class PrimaryPublisherSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Publisher
        fields = ['id', 'PublisherName']


class AuthorSerializer(serializers.ModelSerializer) :
    AuthorBooks = serializers.SerializerMethodField('getBooks')

    def getBooks(self, Author) :
        return Book.objects.filter(BookAuthor = Author).values("id", "BookName")

    class Meta :
        model = Author
        fields = ["id", 'AuthorName', 'AuthorBooks', 'AuthorBio']


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
        fields = ['id', 'TranslatorName', 'TranslatorBooks', 'TranslatorBio']


class PrimaryTranslatorSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Translator
        fields = ['id', 'TranslatorName']


class BookSerializer(serializers.ModelSerializer) :
    BookAuthor = PrimaryAuthorSerializer()
    BookTranslator = PrimaryTranslatorSerializer()
    BookPublisher = PrimaryPublisherSerializer()

    def validate(self, attrs) :
        publisher = Publisher.objects.filter(PublisherName = attrs['BookPublisher']['PublisherName']).first()
        author = Author.objects.filter(AuthorName = attrs['BookAuthor']['AuthorName']).first()
        translator = Translator.objects.filter(TranslatorName = attrs['BookTranslator']['TranslatorName']).first()
        name = attrs['BookName']

        if publisher is None :
            raise serializers.ValidationError({
                "message" : "Publisher Does not Exist"
            })
        elif author is None :
            raise serializers.ValidationError({
                "message" : "Author Does not Exist"
            })
        elif translator is None :
            raise serializers.ValidationError({
                "message" : "Translator Does not Exist"
            })

        else :
            return attrs

    def create(self, validated_data) :
        publisher = Publisher.objects.filter(PublisherName = validated_data['BookPublisher']['PublisherName']).first()
        author = Author.objects.filter(AuthorName = validated_data['BookAuthor']['AuthorName']).first()
        translator = Translator.objects.filter(
            TranslatorName = validated_data['BookTranslator']['TranslatorName']).first()
        name = validated_data['BookName']
        image = validated_data['BookImage']
        date = validated_data['BookDateOfPublish']
        count = validated_data['BookPageCount']

        return Book.objects.create(
                BookName = name,
                BookPublisher = publisher,
                BookAuthor = author,
                BookTranslator = translator,
                BookImage = image,
                BookDateOfPublish = date,
                BookPageCount = count
            )
        # return Book.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     print("***************", validated_data)
        instance.save(**validated_data)
        # Book.objects.update_or_create(validated_data)
    class Meta :
        model = Book
        fields = ['id', 'BookName', 'BookAuthor', 'BookTranslator', 'BookPublisher',
                  'BookSummary', 'BookPageCount', 'BookImage', 'BookDateOfPublish']

        error_messages = {"username" : {"required" : "Give yourself a username"}}


class DjangoUserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = DjangoUser
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer) :
    django_user = DjangoUserSerializer()
    books = BookSerializer()

    class Meta :
        model = User
        # fields = ['id', 'django_user','name', 'family_name',
        #           'location', 'phone_number', 'bio', 'birth_date']
        fields = '__all__'
