from django.db import models


class Author(models.Model) :
    AuthorName = models.CharField(max_length = 50, blank = False)
    #books = models.ForeignKey('Book.Book', blank = True, null = True)

    def __str__(self):
        return self.AuthorName


class Publisher(models.Model) :
    PublisherName = models.CharField(max_length = 50, blank = False)
    #books = models.ForeignKey('Book.Book', blank = True, null = True)

    def __str__(self):
        return self.PublisherName


class Translator(models.Model) :
    TranslatorName = models.CharField(max_length = 50, blank = False)
    #books = models.ForeignKey('Book.Book', blank = True, null = True)

    def __str__(self):
        return self.TranslatorName


class Rate(models.Model) :
    user = models.OneToOneField('user.Profile')
    value = models.IntegerField(choices = (
        (5, 'Excellent'),
        (4, 'Good'),
        (3, 'Not Bad'),
        (2, 'Bad'),
        (1, "Awful")
    ))
    #RateToBook = models.OneToOneField('Book.Book')

    def __str__(self):
        return str(self.value)


class Comment(models.Model):
    user = models.OneToOneField('user.Profile')
    text = models.TextField(max_length = 500, blank = False)
    #CommentOnBook = models.OneToOneField('Book.Book', null = True)

    def __str__(self):
        return self.text
        #+ " on " + str(self.CommentOnBook)


class Book(models.Model) :
    BookName = models.CharField(max_length = 50, null = False, blank = False)
    BookPublisher = models.OneToOneField(Publisher, null = False, blank = False)
    BookAuthor = models.OneToOneField(Author, blank = False)
    BookTranslator = models.OneToOneField(Translator, blank = True)
    BookDateOfPublish = models.DateField(null = True, blank = True)
    BookImage = models.ImageField(null = True, blank = True)
    BookSummary = models.TextField(blank = True, max_length = 1000)
    BookRatesCount = models.IntegerField(default = 0, blank = True)
    BookRatesSum = models.IntegerField(default = 0, blank = True)
    BookCommentsCount = models.IntegerField(default = 0, blank = True)
    BookComments = models.ForeignKey('Book.Comment', null = True, blank = True)

    def __str__(self) :
        return self.BookName + " By " + str(self.BookAuthor)
