from django.conf.urls import url
from . import views

ListAllBooks = views.BookViewSetByPrimaryKey.as_view({
    'get' : 'list',
    # 'post' : 'create'
        })
BookDetailsByPrimaryKey = views.BookViewSetByPrimaryKey.as_view({
    'get' : 'retrieve',
    # 'post' : 'create'
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
UserDetailsByName = views.UserViewSetByName.as_view({
    'get' : 'get'
})


urlpatterns = [
    url(r'^getAllBooks/$', ListAllBooks),
    url(r'^getBook/(?P<pk>[0-9]+)$', BookDetailsByPrimaryKey),
    url(r'^getBook/ByName/(?P<BookName>\w+)$', BookDetailsByBookName),
    url(r'^getBook/ByAuthor/(?P<AuthorName>\w+)$', BookDetailsByBookAuthor),
    url(r'^getBook/ByPublisher/(?P<PublisherName>\w+)$', BookDetailsByBookPublisher),
    url(r'^getUser/(?P<pk>[0-9]+)$', UserDetailsByName)
    ]
