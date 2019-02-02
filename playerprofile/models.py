from django.db import models
from django.utils import timezone

class Info(models.Model):
    """所属県連_カテゴリー"""

    prefecture = models.CharField('所属県連', max_length=50)
    category = models.CharField('カテゴリー', max_length=10)

    def __str__(self):
        return self.prefecture


class Profile(models.Model):
    """プロフィール"""

    title = models.CharField('名前', max_length=30)
    birth = models.DateTimeField('生年月日')
    team = models.CharField('チーム名',max_length=30)
    school = models.CharField('出身校', max_length=255)
    comment = models.TextField('コメント')
    pic = models.TextField('URL')
    info = models.ForeignKey(Info, verbose_name='情報', on_delete=models.PROTECT)


    def __str__(self):
        return self.title