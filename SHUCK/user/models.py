import hashlib
import os
import urllib

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from activities.models import Notification

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
    url = models.CharField(max_length=50, null=True, blank=True)

    def get_url(self):
        url = self.url
        if "http://" not in self.url and "https://" not in self.url and len(self.url) > 0:  # noqa: E501
            url = "http://" + str(self.url)

        return url

    def get_screen_name(self):
        try:
            if self.username:
                return self.username
            else:
                return self.user.username
        except:
            return self.user.username

    def get_avatar(self):
        no_picture = 'http://trybootcamp.vitorfs.com/static/img/user.png'
        try:
            filename = settings.MEDIA_ROOT + '/profile_pictures/' +\
                self.username + '_avatar.jpg'
            picture_url = settings.MEDIA_URL + 'profile_pictures/' +\
                self.username + '.jpg'
            if os.path.isfile(filename):  # pragma: no cover
                print("IS FILE")
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

    def notify_liked(self, feed) :
        print("****** NOTIFY LIKED CALLED")
        print("IN: ", self)
        print("ON: ", feed.user.username)
        if self != feed.user.username :
            Notification(notification_type = Notification.LIKED,
                         from_user = self, to_user = feed.user,
                         feed = feed).save()

    def unotify_liked(self, feed) :
        if self != feed.user.username :
            Notification.objects.filter(notification_type = Notification.LIKED,
                                        from_user = self, to_user = feed.user,
                                        feed = feed).delete()

    def notify_commented(self, feed) :
        print("****** NOTIFY COMMENT CALLED")
        print("IN: ", self)
        print("ON: ", feed.user.username)
        if self != feed.user.username :
            Notification(notification_type = Notification.COMMENTED,
                         from_user = self, to_user = feed.user,
                         feed = feed).save()

    def notify_also_commented(self, feed) :
        comments = feed.get_comments()
        users = []
        for comment in comments :
            if comment.user.username != self.userername and comment.user.username != feed.user.username :
                users.append(comment.user.pk)

        users = list(set(users))
        for user in users :
            Notification(notification_type = Notification.ALSO_COMMENTED,
                         from_user = self,
                         to_user = User(id = user), feed = feed).save()

    def __str__(self) :
        return str(self.username)


