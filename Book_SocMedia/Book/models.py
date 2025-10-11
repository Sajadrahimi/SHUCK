from django.db import models


class Author(models.Model) :
    pass


class Publisher(models.Model) :
    pass


class Translator(models.Model) :
    pass


class Book(models.Model) :
    name = models.CharField(max_length = 50, null = False, blank = False)
    publisher = models.OneToOneField(Publisher, null = False, blank = False)
    author = models.OneToOneField(Author, blank = False)
    translator = models.OneToOneField(Translator, blank = True)
    date_of_publish = models.DateField(null = True, blank = True)
    image = models.ImageField(null = True, blank = True)
    about = models.TextField(blank = True, max_length = 1000)

    def __str__(self) :
        return self.name
