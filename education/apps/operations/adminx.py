import xadmin
from .models import *


class UserAskInfoXadmin(object):
    list_display = ['name', 'phone', 'course', 'add_time']
    search_fields = ['name', 'phone', 'course']
    list_filter = ['name', 'phone', 'course', 'add_time']


class UserLoveInfoXadmin(object):
    list_display = ['userinfo', 'love_id', 'love_type', 'love_status', 'add_time']
    search_fields = ['userinfo', 'love_id', 'love_type', 'love_status']
    list_filter = ['userinfo', 'love_id', 'love_type', 'love_status', 'add_time']


class UserCourseInfoXadmin(object):
    list_display = ['userinfo', 'courseinfo', 'add_time']
    search_fields = ['userinfo', 'courseinfo']
    list_filter = ['userinfo', 'courseinfo', 'add_time']


class UserMessageInfoXadmin(object):
    list_display = ['userinfo', 'message', 'message_status', 'add_time']
    search_fields = ['userinfo', 'message', 'message_status']
    list_filter = ['userinfo', 'message', 'message_status', 'add_time']


class UserCommentInfoXadmin(object):
    list_display = ['userinfo', 'courseinfo', 'content', 'add_time']
    search_fields = ['userinfo', 'courseinfo', 'content']
    list_filter = ['userinfo', 'courseinfo', 'content', 'add_time']


xadmin.site.register(UserAskInfo, UserAskInfoXadmin)
xadmin.site.register(UserLoveInfo, UserLoveInfoXadmin)
xadmin.site.register(UserCourseInfo, UserCourseInfoXadmin)
xadmin.site.register(UserMessageInfo, UserMessageInfoXadmin)
xadmin.site.register(UserCommentInfo, UserCommentInfoXadmin)
