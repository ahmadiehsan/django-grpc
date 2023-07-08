from django.contrib.admin import register
from django_addons.django_helper.admin.base import BaseAdmin

from apps.blog.models import Article


@register(Article)
class ArticleAdmin(BaseAdmin):
    pass
