# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Recall(models.Model):
    title = models.CharField(u'标题', max_length=50)
    desc = models.CharField(u'描述', max_length=200)
    thumb = models.URLField(u'缩略图')
    full = models.URLField(u'原始图')
    updated = models.DateTimeField(u'更新时间', auto_now=True)
    created = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'recall'
        verbose_name_plural = 'recalls'
        ordering = ['-updated']


class Profile(models.Model):
    title = models.CharField(u'标题', max_length=500)
    body = models.TextField(u'正文', max_length=2000)
    body1 = models.TextField(u'正文1', max_length=1000)
    body2 = models.TextField(u'正文2', max_length=1000)
    updated = models.DateTimeField(u'更新时间', auto_now=True)
    created = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        ordering = ['-updated']
