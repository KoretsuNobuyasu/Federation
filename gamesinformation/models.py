from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    """カテゴリ"""

    name = models.CharField('カテゴリ名',max_length=50)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name


class Gamesinformation(models.Model):
    """大会情報"""

    title = models.CharField('大会名', max_length=200)
    text = models.TextField('本文')
    guidelines = models.FileField('大会要項',blank=True)
    result = models.FileField('結果',blank=True)
    created_at = models.DateTimeField('開催日')
    place = models.CharField('開催地', max_length=50, blank=True)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)

    def is_date_limit(self):
        """大会開催日前であればTrue"""
        now = timezone.now()
        return now <= self.created_at

    def __str__(self):
        return self.title