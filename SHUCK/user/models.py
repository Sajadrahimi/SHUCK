from django.db import models
from django.contrib.auth.models import User as DjangoUser



# Create your models here.

class User(models.Model) :
    django_user = models.OneToOneField(DjangoUser)
    name = models.CharField(max_length = 20, null = False, blank = False)
    family_name = models.CharField(max_length = 30, null = False, blank = False)
    birth_date = models.DateField(null = False, blank = True)
    bio = models.TextField(max_length = 500, blank = True)
    phone_number = models.IntegerField(max_length = 12, blank = True)
    avatar = models.ImageField(blank = True, upload_to = 'avatars')
    location = models.CharField(max_length = 30, blank = True)
    types = (
        ('SU', 'Super User'),
        ('U', 'User'),
    )
    user_type = models.CharField(max_length = 2,
                                 choices = types,
                                 default = 'U')
    # Must be Changed, THIS IS TEMPORARY
    books = models.ForeignKey('Book.Book')

    def __str__(self) :
        return str(self.django_user)


