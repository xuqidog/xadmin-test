# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField


# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    # content = models.TextField(verbose_name="内容")
    fav_nums = models.IntegerField(default=0, verbose_name="点赞人数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    content = UEditorField(verbose_name="内容", width=600, height=300, imagePath="activitys/ueditor/", filePath="activitys/ueditor/",
                  default='')

    class Meta:
        verbose_name = "活动"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
