from django.db import models
from django.contrib.auth.models import AbstractUser


class Shelf(models.Model):
    shelf_name = models.CharField(max_length = 30, null = False)
    shelf_books = models.ForeignKey('Book.Book', null = True, blank = True)
    # user = models.ForeignKey(User)
    def __str__(self):
        return self.shelf_name

    @staticmethod
    def getReadShelf():
        return Shelf.objects.create(shelf_name = 'Read')

class User(AbstractUser) :
    birth_date = models.DateField(null = True, blank = True)
    bio = models.TextField(max_length = 500, blank = True, null = True)
    location = models.CharField(max_length = 30, blank = True, null = True)
    phone_number = models.IntegerField(blank = True, null = True)
    avatar = models.ImageField(blank = True, null = True, upload_to = 'avatars')
    types = (
        ('SU', 'Super User'),
        ('U', 'User'),
    )
    user_type = models.CharField(max_length = 2,
                                 choices = types,
                                 default = 'U')
    Reads = models.ManyToManyField('Book.Book', null = True, blank = True, related_name = "Read")
    toReads = models.ForeignKey('Book.Book', null = True, blank = True, related_name = "toRead")
    Readings = models.ForeignKey('Book.Book', null = True, blank = True, related_name = "Reading")

    def __str__(self) :
        return str(self.username)


