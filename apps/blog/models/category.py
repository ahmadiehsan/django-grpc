from django.db import models
from django.utils.translation import gettext_lazy as _
from django_addons.django_helper.models.base import AbstractBaseModel


class Category(AbstractBaseModel):
    name = models.CharField(_('Name'), max_length=250)
    parent = models.ForeignKey('self', verbose_name=_('Parent'), on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta(AbstractBaseModel.Meta):
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
