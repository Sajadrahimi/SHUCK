"""Book_SocMedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.contrib import admin
from core import views as core
from search import views as search

urlpatterns = [
    url(r'^$', core.home, name = 'home'),
    url(r'^search/$', search.search, name = 'search'),
    url(r'^autocomplete/$', search.get_autocomplete_suggestions, name='autocomplete'),
    url(r'^settings/$', core.settings, name='settings'),
    url(r'^settings/picture/$', core.picture, name = 'picture'),
    url(r'^settings/upload_picture/$', core.upload_picture,
        name = 'upload_picture'),
    url(r'^settings/save_uploaded_picture/$', core.save_uploaded_picture,
        name = 'save_uploaded_picture'),
    url(r'^settings/password/$', core.password, name = 'password'),
    # url(r'^logout', auth_views.logout, {'next_page' : '/'}, name = 'logout'),
    url(r'^(?P<username>[^/]+)/$', core.profile, name='profile'),
    url(r'^network/network/$', core.network, name='network'),
    url(r'^admin/admin/', admin.site.urls),
    url(r'^user/', include('user.url')),
    url(r'^book/', include('Book.url')),
    url(r'^api/', include('api.url')),
    url(r'^feeds/', include('feeds.url')),
    url(r'^messenger/inbox/', include('messenger.url')),

]
