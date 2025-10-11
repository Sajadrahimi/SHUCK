import hashlib
import os
import urllib

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
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

class Profile(AbstractUser) :
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
    toReads = models.ManyToManyField('Book.Book', null = True, blank = True, related_name = "toRead")
    Readings = models.ManyToManyField('Book.Book', null = True, blank = True, related_name = "Reading")
    # token = models.OneToOneField(Token, null = True)

    def get_url(self):
        url = self.url
        if "http://" not in self.url and "https://" not in self.url and len(self.url) > 0:  # noqa: E501
            url = "http://" + str(self.url)

        return url

    def get_picture(self):
        no_picture = 'http://trybootcamp.vitorfs.com/static/img/user.png'
        try:
            filename = settings.MEDIA_ROOT + '/profile_pictures/' +\
                self.user.username + '.jpg'
            picture_url = settings.MEDIA_URL + 'profile_pictures/' +\
                self.user.username + '.jpg'
            if os.path.isfile(filename):  # pragma: no cover
                return picture_url
            else:  # pragma: no cover
                gravatar_url = 'http://www.gravatar.com/avatar/{0}?{1}'.format(
                    hashlib.md5(self.user.email.lower()).hexdigest(),
                    urllib.urlencode({'d': no_picture, 's': '256'})
                    )
                return gravatar_url

        except Exception:
            return no_picture

    @receiver(post_save, sender = settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance = None, created = False, **kwargs) :
        if created :
            Token.objects.create(user = instance)

    def __str__(self) :
        return str(self.username)


