from django.contrib import admin
from .models import Book, Author, Translator, Publisher, Comment,Rate
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Translator)
admin.site.register(Publisher)
admin.site.register(Comment)
admin.site.register(Rate)
