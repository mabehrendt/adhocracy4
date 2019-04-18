from django.conf import settings
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from adhocracy4 import transforms
from adhocracy4.generics import models_to_limit
from adhocracy4.models import base
from adhocracy4.ratings import models as rating_models


class Comment(base.UserGeneratedContentModel):

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=models_to_limit(settings.A4_COMMENTABLES)
    )
    object_pk = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        ct_field="content_type", fk_field="object_pk")
    comment = models.TextField(max_length=4000)
    is_removed = models.BooleanField(default=False)
    is_censored = models.BooleanField(default=False)
    ratings = GenericRelation(rating_models.Rating,
                              related_query_name='comment',
                              object_id_field='object_pk')
    child_comments = GenericRelation('self',
                                     related_query_name='parent_comment',
                                     object_id_field='object_pk')
    comment_categories = models.CharField(blank=True,
                                          max_length=256)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ('created',)
        index_together = [('content_type', 'object_pk')]

    def __str__(self):
        if len(self.comment) > 200:
            return "{} ...".format(self.comment[:200])
        else:
            return "{}".format(self.comment)

    def save(self, *args, **kwargs):
        """
        Change the text of the comment if
        the comment was marked removed or censored
        """

        self.comment = transforms.clean_html_all(
            self.comment)

        if self.is_removed:
            self.comment = _('deleted by creator')
            self.comment_categories = ''
        if self.is_censored:
            self.comment = _('deleted by moderator')
            self.comment_categories = ''
        return super(Comment, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if hasattr(self.content_object, 'get_absolute_url'):
            return "{}#comment_{}".format(
                self.content_object.get_absolute_url(), str(self.id))
        else:
            return "{}#comment_{}".format(
                self.module.get_absolute_url(), str(self.id))

    @property
    def notification_content(self):
        return self.comment

    @property
    def project(self):
        return self.module.project

    @property
    def module(self):
        co = self.content_object
        if isinstance(co, self.__class__):
            co = co.content_object
        return co.module
