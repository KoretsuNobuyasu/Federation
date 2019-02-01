from django.db import models
from django.utils import timezone




class Topics(models.Model):
    """全体に向けてのお知らせ"""
    title = models.CharField('タイトル', max_length=255)
    text = models.TextField("本文")
    created_at = models.DateTimeField('作成日',default=timezone.now)

    def ___str___(self):
        return self.title