from django.db import models


class Author(models.Model) :
    AuthorName = models.CharField(max_length = 50, blank = False)
    AuthorBooks = models.ForeignKey('Book', related_name = 'AuthorBooks',null = True)

    @staticmethod
    def getAuthorByName(name) :
        return Author.objects.filter(AuthorName = name)

    @staticmethod
    def getAuthorBooks(name) :
        return Book.objects.filter(BookAuthor = Author.getAuthorByName(name))

    @staticmethod
    def isAuthorExists(name) :
        if Author.objects.filter(AuthorName = name).count() != 0 :
            return True
        else :
            return False

    def __str__(self) :
        return self.AuthorName





class Translator(models.Model) :
    TranslatorName = models.CharField(max_length = 50, blank = False)


    def getTranslatorBooks(self) :
        return Book.objects.get(BookTranslator = self)

    def __str__(self) :
        return self.TranslatorName


class Rate(models.Model) :
    # user = models.OneToOneField('user.models.User')
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
    # user = models.OneToOneField('user.models.User')
    text = models.TextField(max_length = 500, blank = False)

    CommentOnBook = models.OneToOneField('Book.Book', null = True)

    def __str__(self) :
        return self.text
        # + " on " + str(self.CommentOnBook)


class Book(models.Model) :
    BookName = models.CharField(max_length = 50, null = False, blank = False)
    # BookPublisher = models.ManyToOneRel(to = 'Publisher', field = 'BookPublisher',
    #                                     field_name = 'BookPublisher')
    # BookAuthor = models.ManyToOneRel(to = 'Author', field = 'BookAuthor',
    #                                  field_name = 'BookAuthor')
    BookPublisher = models.ForeignKey('Publisher', null = True)
    BookAuthor = models.ForeignKey('Author', null = True)
    BookTranslator = models.ForeignKey('Translator', blank = True, null = True)
    BookDateOfPublish = models.DateField(null = True, blank = True)
    BookImage = models.ImageField(null = True, blank = True)
    BookSummary = models.TextField(blank = True, max_length = 1000)
    # BookRatesCount = models.IntegerField(default = 0, blank = True)
    # BookRatesSum = models.IntegerField(default = 0, blank = True)
    # BookComments = models.ForeignKey('Book.Comment', null = True, blank = True)

    def __init__(self, *args, **kwargs) :
        super(Book, self).__init__(*args, **kwargs)
        self.OldBookPublisher = self.BookPublisher
        self.OldBookAuthor = self.BookAuthor

    def save(self, **kwargs) :

        if self.OldBookPublisher != self.BookPublisher and self.OldBookPublisher is not None :
            print("PUBLISHER CHANGED", "OLD PUB: ", self.OldBookPublisher.PublisherName)
            Publisher.objects.get(PublisherName = \
            self.OldBookPublisher.PublisherName).ChangePublisherBook(self)
        super(Book, self).save(**kwargs)

    def __str__(self) :
        return self.BookName

class Publisher(models.Model) :
    PublisherName = models.CharField(max_length = 50, blank = False)
    PublisherBooks = models.ForeignKey('Book', related_name = 'PublisherBooks', null = True, default = '')

    def getPublisherBooks(self) :
        return Book.objects.get(BookTranslator = self)

    def ChangePublisherBook(self, Book):
        print("CHANGE PUBLISHER CALLED", "BOOK: ", Book)
        self.PublisherBooks = Book
        super(Publisher, self).save()

    def __str__(self) :
        return self.PublisherName
