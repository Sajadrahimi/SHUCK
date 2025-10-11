from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
import django.forms as forms

from .models import Book, Author, Translator, Publisher, Comment,Rate
from user.models import User
# Register your models here.

# admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Translator)
admin.site.register(Publisher)
admin.site.register(Comment)
admin.site.register(Rate)
admin.site.register(Book)
