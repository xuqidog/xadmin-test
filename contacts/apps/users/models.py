# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(max_length=50, verbose_name="生日", null=True, blank=True)
    gender = models.CharField(choices=(("male", "男"), ("female", "女")), default="female", max_length=6, verbose_name="性别")
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    mobile = models.CharField(max_length=11, verbose_name="手机号", null=True, blank=True)
    image = models.ImageField(verbose_name="头像", upload_to="image/%Y/%m", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
