import xadmin
from .models import *
from xadmin import views


class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '在线教育后台管理'
    site_footer = '1074602800@qq.com'
    menu_style = 'accordion'


class EmailVerifyXadmin(object):
    list_display = ['email', 'code', 'send_type', 'add_time']
    search_field = ['email', 'code']
    list_filter = ['email', 'code', 'send_type', 'add_time']


class BannerXadmin(object):
    list_display = ['url', 'add_time']
    search_field = ['url']
    list_filter = ['url', 'add_time']


xadmin.site.register(EmailVerify, EmailVerifyXadmin)
xadmin.site.register(Banner, BannerXadmin)
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
