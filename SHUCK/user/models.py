from django.db import models
from django.contrib.auth.models import User as DjangoUser



# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(models.Model) :
    django_user = models.ForeignKey(DjangoUser, on_delete = models.CASCADE, primary_key = True)
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
    shelves = models.ForeignKey('Shelf', null = True, blank = True)

    def __str__(self) :
        return str(self.django_user)

    def createShelves(self):
        if self is not None:
            self.shelves.objects.create(name = 'Read')
            self.shelves.objects.create(shelf_name = 'Reading')
            self.shelves.objects.create(shelf_name = 'to Read')


class Shelf(models.Model):
    shelf_name = models.CharField(max_length = 30, null = False)
    shelf_books = models.ForeignKey('Book.Book')
    # user = models.ForeignKey(User)
    def __str__(self):
        return self.shelf_name
