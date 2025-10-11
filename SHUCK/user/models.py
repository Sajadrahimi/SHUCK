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
    # books = models.ForeignKey('Book.Book')

    # @receiver(post_save, sender = DjangoUser)
    # def create_user_profile(sender, instance, created, **kwargs) :
    #     if created :
    #         User.objects.create(user = instance)
    #
    # @receiver(post_save, sender = DjangoUser)
    # def create_user_profile(sender, instance, created, **kwargs) :
    #     if created :
    #         User.objects.create(user = instance)

    def save(self, **kwargs):
        super(User, self).save(**kwargs)

    def __str__(self) :
        return str(self.django_user)


