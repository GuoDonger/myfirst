import xadmin
from .models import *


class CourseInfoXadmin(object):
    list_display = ['name', 'level', 'category', 'orginfo', 'teacherinfo']
    search_field = ['name', 'level', 'category', 'orginfo', 'teacherinfo']
    list_filter = ['name', 'level', 'category', 'orginfo', 'teacherinfo']


class ChapterInfoXadmin(object):
    list_display = ['name', 'courseinfo']
    search_field = ['name', 'courseinfo']
    list_filter = ['name', 'courseinfo']


class VideoInfoXadmin(object):
    list_display = ['name', 'study_time', 'chapterinfo']
    search_field = ['name', 'study_time', 'chapterinfo']
    list_filter = ['name', 'study_time', 'chapterinfo']


class SourceInfoXadmin(object):
    list_display = ['name', 'file_addr', 'courseinfo']
    search_field = ['name', 'file_addr', 'courseinfo']
    list_filter = ['name', 'file_addr', 'courseinfo']


xadmin.site.register(CourseInfo, CourseInfoXadmin)
xadmin.site.register(ChapterInfo, ChapterInfoXadmin)
xadmin.site.register(VideoInfo, VideoInfoXadmin)
xadmin.site.register(SourceInfo, SourceInfoXadmin)
