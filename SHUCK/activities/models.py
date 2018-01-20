from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape
import SHUCK.settings as settings

@python_2_unicode_compatible
class Activity(models.Model):
    FAVORITE = 'F'
    LIKE = 'L'
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPES = (
        (FAVORITE, 'Favorite'),
        (LIKE, 'Like'),
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
        )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    feed = models.IntegerField(null=True, blank=True)
    answer = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

@python_2_unicode_compatible
class Notification(models.Model):
    LIKED = 'L'
    COMMENTED = 'C'
    FAVORITED = 'F'
    ANSWERED = 'A'
    ACCEPTED_ANSWER = 'W'
    EDITED_ARTICLE = 'E'
    ALSO_COMMENTED = 'S'
    NOTIFICATION_TYPES = (
        (LIKED, 'Liked'),
        (COMMENTED, 'Commented'),
        (FAVORITED, 'Favorited'),
        (ANSWERED, 'Answered'),
        (ACCEPTED_ANSWER, 'Accepted Answer'),
        (ALSO_COMMENTED, 'Also Commented'),
        )

    _LIKED_TEMPLATE = '<a href="/{0}/">{1}</a> liked your post: <a href="/feeds/{2}/">{3}</a>'  # noqa: E501
    _COMMENTED_TEMPLATE = '<a href="/{0}/">{1}</a> commented on your post: <a href="/feeds/{2}/">{3}</a>'  # noqa: E501
    _EDITED_ARTICLE_TEMPLATE = '<a href="/{0}/">{1}</a> edited your article: <a href="/article/{2}/">{3}</a>'  # noqa: E501

    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    date = models.DateTimeField(auto_now_add=True)
    feed = models.ForeignKey('feeds.Feed', null=True, blank=True)
    notification_type = models.CharField(max_length=1,
                                         choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ('-date',)

    def __str__(self):
        if self.notification_type == self.LIKED:
            return self._LIKED_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.get_screen_name()),
                self.feed.pk,
                escape(self.get_summary(self.feed.post))
                )
        elif self.notification_type == self.COMMENTED:
            return self._COMMENTED_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.get_screen_name()),
                self.feed.pk,
                escape(self.get_summary(self.feed.post))
                )

        elif self.notification_type == self.EDITED_ARTICLE:
            return self._EDITED_ARTICLE_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.article.slug,
                escape(self.get_summary(self.article.title))
                )
        elif self.notification_type == self.ALSO_COMMENTED:
            return self._ALSO_COMMENTED_TEMPLATE.format(
                escape(self.from_user.username),
                escape(self.from_user.profile.get_screen_name()),
                self.feed.pk,
                escape(self.get_summary(self.feed.post))
                )
        else:
            return 'Ooops! Something went wrong.'

    def get_summary(self, value):
        summary_size = 50
        if len(value) > summary_size:
            return '{0}...'.format(value[:summary_size])

        else:
            return value
