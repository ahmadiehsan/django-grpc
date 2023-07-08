from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_addons.django_helper.models.base import AbstractBaseModel

from apps.blog.models.category import Category


class ArticleStatus(models.TextChoices):
    DRAFT = 'DRAFT', _('Draft')
    PUBLISHED = 'PUBLISHED', _('Published')
    DISABLED = 'DISABLED', _('Disabled')


class Article(AbstractBaseModel):
    title = models.CharField(_('Title'), max_length=250, null=True, blank=True)
    content = models.TextField(_('Content'), null=True, blank=True)
    status = models.CharField(_('Status'), max_length=20, choices=ArticleStatus.choices)
    categories = models.ManyToManyField(Category, verbose_name=_('Categories'), blank=True)

    def __str__(self):
        return self.title

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def clean(self):
        self._validate_required_fields()

    def _validate_required_fields(self):
        if self.status not in [ArticleStatus.PUBLISHED, ArticleStatus.DISABLED]:
            return

        if not self.title:
            raise ValidationError(_('`Title` field is required in `{}` status').format(self.status))

        if not self.content:
            raise ValidationError(_('`Content` field is required in `{}` status').format(self.status))

        if not self.categories:
            raise ValidationError(_('`Categories` field is required in `{}` status').format(self.status))
