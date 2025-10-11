from django.db import models


class Author(models.Model) :
    AuthorName = models.CharField(max_length = 50, blank = False)

    # returns an Author with a given name
    @staticmethod
    def getAuthorByName(name):
        return Author.objects.filter(AuthorName = name)

    # returns books of an author with a given AuthorName
    @staticmethod
    def getAuthorBooks(name) :
        return Book.objects.filter(BookAuthor = Author.getAuthorByName(name))

    # checks if an author exists
    @staticmethod
    def isAuthorExists(name):
        if Author.objects.filter(AuthorName = name).count() != 0:
            return True
        else:
            return False

    def __str__(self) :
        return self.AuthorName


class Publisher(models.Model) :
    PublisherName = models.CharField(max_length = 50, blank = False)

    # returns books of an author
    #MUST BE CHANGED
    def getPublisherBooks(self) :
        return Book.objects.get(BookTranslator = self)

    def __str__(self) :
        return self.PublisherName


class Translator(models.Model) :
    TranslatorName = models.CharField(max_length = 50, blank = False)

    # MUST BE CHANGED
    def getTranslatorBooks(self) :
        return Book.objects.get(BookTranslator = self)

    def __str__(self) :
        return self.TranslatorName


class Rate(models.Model) :
    user = models.OneToOneField('user.User')
    value = models.IntegerField(choices = (
        (5, 'Excellent'),
        (4, 'Good'),
        (3, 'Not Bad'),
        (2, 'Bad'),
        (1, "Awful")
    ))

    # RateToBook = models.OneToOneField('Book.Book')

    def __str__(self) :
        return str(self.value)


class Comment(models.Model) :
    user = models.OneToOneField('user.User')
    text = models.TextField(max_length = 500, blank = False)

    CommentOnBook = models.OneToOneField('Book.Book', null = True)

    def __str__(self) :
        return self.text
        # + " on " + str(self.CommentOnBook)


class Book(models.Model) :
    BookName = models.CharField(max_length = 50, null = False, blank = False)
    # BookPublisher = models.OneToOneField(Publisher, null = False, blank = False)
    BookPublisher = models.ForeignKey('Publisher', null = False, blank = False)
    # BookAuthor = models.OneToOneField(Author, blank = False)
    BookAuthor = models.ForeignKey('Author', blank = False)
    # BookTranslator = models.OneToOneField(Translator, blank = True, null = True)
    BookTranslator = models.ForeignKey('Translator', blank = True, null = True)
    BookDateOfPublish = models.DateField(null = True, blank = True)
    BookImage = models.ImageField(null = True, blank = True)
    BookSummary = models.TextField(blank = True, max_length = 1000)
    BookRatesCount = models.IntegerField(default = 0, blank = True)
    BookRatesSum = models.IntegerField(default = 0, blank = True)
    BookComments = models.ForeignKey('Book.Comment', null = True, blank = True)

    def __str__(self) :
        return self.BookName + " By " + str(self.BookAuthor)
