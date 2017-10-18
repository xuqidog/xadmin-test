# -*- coding: utf-8 -*-
__author__ = 'theme'
__date__ = '2017/9/24 下午12:07'

import xadmin

from .models import Activity


class ActivityAdmin(object):
    list_display = ['title', 'content', 'fav_nums', 'add_time']
    search_fields = ['title', 'content', 'fav_nums']
    list_filter = ['title', 'content', 'fav_nums', 'add_time']
    show_bookmarks = False
    refresh_times = (3, 5)
    list_editable = ['title', 'content']
    show_detail_fields = ['title']
    model_icon = 'fa fa-pencil-square'
    style_fields = {"content": "ueditor"}
    import_excel = True
    # data_charts = {  # 图标
    #     "user_count": {'title': "活动图标", "x-field": "add_time", "y-field": ("fav_nums",)},
    #     # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    # }

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:  # 导入excel后数据处理逻辑
            pass
        return super(ActivityAdmin, self).post(request, args, kwargs)


xadmin.site.register(Activity, ActivityAdmin)
