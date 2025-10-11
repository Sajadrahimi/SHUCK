from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addBook$', views.AddBook),
    url(r'^authorBooks/(?P<AuthorName>\w{0,50})/$', views.showAuthorBooks),
]
