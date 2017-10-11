from django.conf.urls import url
from . import views

book_list = views.BookViewSet.as_view({
    'get' : 'list',
    # 'post' : 'create'
        })
book_detail = views.BookViewSet.as_view({
    'get' : 'retrieve',
    # 'put' : 'update',
    # 'patch' : 'partial_update',
    # 'delete' : 'destroy'
        })
user_list = views.UserViewSet.as_view({
    'get' : 'list'
})
user_detail = views.UserViewSet.as_view({
    'get' : 'retrieve',
    # 'post' : 'create'
})
djangoUser_list = views.DjangoUserViewSet.as_view({
    'get' : 'list'
})
urlpatterns = [
    url(r'^getAllBooks/$', book_list),
    url(r'^getBook/(?P<pk>[0-9]+)$', book_detail),
    url(r'^getAllUsers/$', user_list),
    url(r'^getUser/(?P<pk>[0-9]+)$', user_detail)
    ]
