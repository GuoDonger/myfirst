import xadmin
from .models import *


class CityInfoXadmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name']


class OrgInfoXadmin(object):
    list_display = ['name', 'image', 'address', 'detail', 'study_num', 'click_num',
                    'love_num', 'desc', 'add_time', 'cityinfo', 'category']
    search_fields = ['name', 'address', 'cityinfo', 'love_num', 'click_num']
    list_filter = ['name', 'address', 'cityinfo', 'love_num', 'click_num']


class TeacherInfoXadmin(object):
    list_display = ['name', 'icon', 'work_year', 'company', 'click_num', 'job', 'work_style',
                    'orginfo', 'add_time']
    search_fields = ['name', 'icon', 'work_year', 'company', 'click_num', 'job', 'work_style',
                     'orginfo', 'add_time']
    list_filter = ['name', 'icon', 'work_year', 'company', 'click_num', 'job', 'work_style',
                   'orginfo', 'add_time']


xadmin.site.register(CityInfo, CityInfoXadmin)
xadmin.site.register(OrgInfo, OrgInfoXadmin)
xadmin.site.register(TeacherInfo, TeacherInfoXadmin)
