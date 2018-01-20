from django.db import models


class Author(models.Model) :
    AuthorName = models.CharField(max_length = 50, blank = False)
    AuthorBio = models.TextField(max_length = 1000, null = True, blank = True)
    def __str__(self) :
        return self.AuthorName


class Translator(models.Model) :
    TranslatorName = models.CharField(max_length = 50)
    TranslatorBio = models.TextField(max_length = 1000, null = True, blank = True)
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

    # CommentOnBook = models.OneToOneField('Book.Book', null = True, on_delete = models.CASCADE)

    def __str__(self) :
        return self.text
        # + " on " + str(self.CommentOnBook)


class Book(models.Model) :
    BookName = models.CharField(max_length = 50, null = True, blank = False)
    BookPublisher = models.ForeignKey('Publisher', null = True, on_delete = models.CASCADE)
    BookAuthor = models.ForeignKey('Author', null = True,on_delete = models.CASCADE)
    BookTranslator = models.ForeignKey('Translator', blank = True, null = True, on_delete = models.CASCADE)
    BookDateOfPublish = models.DateField(null = True, blank = True)
    BookImage = models.ImageField(null = True, blank = True)
    BookPageCount = models.IntegerField(null = True)
    BookSummary = models.TextField(blank = True, max_length = 1000)
    BookRatesCount = models.IntegerField(default = 0, blank = True, editable = False)
    BookRatesSum = models.IntegerField(default = 0, blank = True, editable = False)
    BookComments = models.ForeignKey\
        ('Book.Comment', null = True, blank = True, editable = False)

    def __str__(self) :
        return self.BookName

class Publisher(models.Model) :
    PublisherName = models.CharField(max_length = 50, blank = False)

    def __str__(self) :
        return self.PublisherName
