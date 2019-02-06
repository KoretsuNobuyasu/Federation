from django.db import models
from django.utils import timezone

class Category(models.Model):
    """国内外・カテゴリ"""

    domesticoroverseas = models.CharField('日本？世界？', max_length=30)
    sex = models.CharField('性別', max_length=10)
    which = models.CharField('リンクorロード', max_length=10, blank=True)

    def is_domestic(self):
        """日本人ならTrue"""
        return self.domesticoroverseas == '日本'
    def is_man(self):
        """男ならTrue"""
        return self.sex == '男子'
    def perform(self):
        domestic = self.is_domestic()
        sex = self.is_man()
        if domestic:
            if sex:
                return '男子日本記録'
            else:
                return '女子日本記録'
        else:
            if sex:
                return '男子世界記録'
            else:
                return '女子世界記録'


    def __str__(self):
        return self.domesticoroverseas










class Record(models.Model):
    """トラック男子記録"""
    distance = models.CharField('距離', max_length=40)
    who = models.CharField('記録保持者', max_length=40)
    team = models.CharField('チーム名or出身', max_length=40)
    time = models.CharField('タイム', max_length=40)
    created_at = models.DateTimeField('開催日')
    where = models.CharField('開催地', max_length=40)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)


    def __str__(self):
        return self.distance


class Recordwoman(models.Model):
    """トラック女子記録"""
    distance = models.CharField('距離', max_length=40)
    who = models.CharField('記録保持者', max_length=40)
    team = models.CharField('チーム名or出身', max_length=40)
    time = models.CharField('タイム', max_length=40)
    created_at = models.DateTimeField('開催日')
    where = models.CharField('開催地', max_length=40)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)


    def __str__(self):
        return self.distance

class Recordroadman(models.Model):
    """ロード男子記録"""
    distance = models.CharField('距離', max_length=40)
    who = models.CharField('記録保持者', max_length=40)
    team = models.CharField('チーム名or出身', max_length=40)
    time = models.CharField('タイム', max_length=40)
    created_at = models.DateTimeField('開催日')
    where = models.CharField('開催地', max_length=40)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)


    def __str__(self):
        return self.distance

class Recordroadwoman(models.Model):
    """ロード女子記録"""
    distance = models.CharField('距離', max_length=40)
    who = models.CharField('記録保持者', max_length=40)
    team = models.CharField('チーム名or出身', max_length=40)
    time = models.CharField('タイム', max_length=40)
    created_at = models.DateTimeField('開催日')
    where = models.CharField('開催地', max_length=40)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)


    def __str__(self):
        return self.distance

class Recordtrackworldman(models.Model):
    """トラック男子世界記録"""
    distance = models.CharField('距離', max_length=40)
    who = models.CharField('記録保持者', max_length=40)
    team = models.CharField('チーム名or出身', max_length=40)
    time = models.CharField('タイム', max_length=40)
    created_at = models.DateTimeField('開催日')
    where = models.CharField('開催地', max_length=40)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)


    def __str__(self):
        return self.distance


class Recordtrackworldwoman(models.Model):
    """トラック女子世界記録"""
    distance = models.CharField('距離', max_length=40)
    who = models.CharField('記録保持者', max_length=40)
    team = models.CharField('チーム名or出身', max_length=40)
    time = models.CharField('タイム', max_length=40)
    created_at = models.DateTimeField('開催日')
    where = models.CharField('開催地', max_length=40)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)


    def __str__(self):
        return self.distance


class Recordroadworldman(models.Model):
    """ロード男子世界記録"""
    distance = models.CharField('距離', max_length=40)
    who = models.CharField('記録保持者', max_length=40)
    team = models.CharField('チーム名or出身', max_length=40)
    time = models.CharField('タイム', max_length=40)
    created_at = models.DateTimeField('開催日')
    where = models.CharField('開催地', max_length=40)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)


    def __str__(self):
        return self.distance


class Recordroadworldwoman(models.Model):
    """ロード女子世界記録"""
    distance = models.CharField('距離', max_length=40)
    who = models.CharField('記録保持者', max_length=40)
    team = models.CharField('チーム名or出身', max_length=40)
    time = models.CharField('タイム', max_length=40)
    created_at = models.DateTimeField('開催日')
    where = models.CharField('開催地', max_length=40)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)


    def __str__(self):
        return self.distance
