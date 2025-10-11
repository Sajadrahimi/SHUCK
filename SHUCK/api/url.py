from django.conf.urls import url, include
from . import views
from rest_framework import authentication

ListAllBooks = views.BookViewSetByPrimaryKey.as_view({
    'get' : 'list',
    # 'post' : 'create'
        })
BookDetailsByPrimaryKey = views.BookViewSetByPrimaryKey.as_view({
    'get' : 'retrieve',
    'post' : 'create',
        })
BookDetailsByBookName = views.BookViewSetByBookName.as_view({
    'get' : 'retrieve',
        })
BookDetailsByBookAuthor = views.BookViewSetByBookAuthor.as_view({
    'get' : 'retrieve',
        })
BookDetailsByBookPublisher = views.BookViewSetByBookPublisher.as_view({
    'get' : 'retrieve',
        })
UserDetailsByPrimaryKey = views.UserViewSetByPrimaryKey.as_view({
    'get' : 'retrieve',
    'post' : 'update',
})
Register = views.UserViewSetByUserName.as_view({
    'post' : 'create'
})

Auth = views.UserLoginByToken.as_view({
    'get' : 'retrieve'
})
urlpatterns = [
    url(r'^getAllBooks/$', ListAllBooks),
    url(r'^getBook/(?P<pk>[0-9]+)$', BookDetailsByPrimaryKey),
    url(r'^getBook/ByName/(?P<BookName>\w+)$', BookDetailsByBookName),
    url(r'^getBook/ByAuthor/(?P<AuthorName>\w+)$', BookDetailsByBookAuthor),
    url(r'^getBook/ByPublisher/(?P<PublisherName>\w+)$', BookDetailsByBookPublisher),
    url(r'^getProfile/(?P<pk>[0-9]+)$', UserDetailsByPrimaryKey),
    url(r'^register/$', Register),
    url(r'^auth/(?P<key>\w+)$', Auth)
    ]
