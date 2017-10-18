# -*- coding: utf-8 -*-
__author__ = 'theme'
__date__ = '2017/9/24 下午12:08'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import UserProfile


class UserProfileAdmin(UserAdmin):
    pass


class BaseSetting(object):
    # enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "Contacts平台"
    site_footer = "theme开发"
    menu_style = "accordion"


xadmin.site.register(views.BaseAdminView, BaseSetting)
# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
