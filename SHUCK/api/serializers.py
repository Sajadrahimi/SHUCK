from rest_framework import serializers
from django.contrib.auth import authenticate
from Book.models import Publisher, Book, Author, Translator
from user.models import User


class PrimaryUserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'avatar']


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
    UsersReadThisBook = serializers.SerializerMethodField('getReads')

    def getReads(self, Book) :
        return User.objects.filter(Reads = Book).values('id', 'username', 'avatar')

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
                  'BookSummary', 'BookPageCount', 'BookImage', 'BookDateOfPublish',
                  'UsersReadThisBook']


class PrimaryBookSerializer(serializers.ModelSerializer) :
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

class UserSignUpSerializer(serializers.ModelSerializer):
    def validate(self, attrs) :
        print("************", attrs)
        username = attrs['username']
        email = attrs['email']

        if User.objects.filter(username = username).count() != 0 :
            raise serializers.ValidationError({
                "message" : "username is taken."
            })
        elif User.objects.filter(email = email).count() != 0 :
            raise serializers.ValidationError({
                "message" : "email is taken"
            })
        else :
            return attrs

    def create(self, validated_data) :
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        location = validated_data['location']
        phone_number = validated_data['phone_number']
        bio = validated_data['bio']
        birth_date = validated_data['birth_date']
        avatar = validated_data['avatar']
        u = User.objects.create(
            username = username, password = password,
            email = email, first_name = first_name ,
            last_name = last_name, location = location,
            phone_number = phone_number, bio = bio,
            birth_date = birth_date, avatar = avatar
        )
        authenticate(u)
        return u

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name',
                  'last_name', 'location', 'phone_number', 'bio',
                  'birth_date', 'avatar']

# @login_required
class UserSerializer(serializers.ModelSerializer) :
    Reads = PrimaryBookSerializer(many = True)
    toReads = PrimaryBookSerializer(many = True)
    Readings = PrimaryBookSerializer(many = True)
    class Meta :
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'last_login',
                  'location', 'phone_number', 'bio', 'birth_date', 'is_staff', 'is_active',
                  'avatar', 'groups', 'Reads', 'toReads', 'Readings']
