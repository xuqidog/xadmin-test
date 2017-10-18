# -*- coding: utf-8 -*-
__author__ = 'theme'
__date__ = '2017/9/27 上午11:04'

from activitys.models import Activity
from users.models import UserProfile
from rest_framework import serializers


class activitysSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('url', 'title', 'content')


class Activitys_list_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('title', 'content')


class usersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'username', 'email')