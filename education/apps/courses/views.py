from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from operations.models import UserLoveInfo, UserCourseInfo
from .models import *


# Create your views here.
def course_list(request):
    course_all = CourseInfo.objects.all()
    love_list = course_all.order_by('-love_num')[:3]
    sort = request.GET.get('sort', '')

    if sort:
        if sort == 'hot':
            course_all = course_all.order_by('-click_num')
        elif sort == 'students':
            course_all = course_all.order_by('-stunum')

    page_num = request.GET.get('page', 1)
    paginator = Paginator(course_all, 3)

    try:
        page_list = paginator.page(page_num)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)

    return render(request, 'courses/course-list.html', {'page_list': page_list, 'love_list': love_list})


def course_detail(request, course_id):
    course = CourseInfo.objects.get(pk=course_id)
    rela_course = CourseInfo.objects.all().filter(name__contains=course.name[:5])

    org_love = False
    course_love = False

    if request.user.is_authenticated:
        org_userlove = UserLoveInfo.objects.filter(userinfo=request.user, love_type=1, love_id=course.orginfo.id)
        course_userlove = UserLoveInfo.objects.filter(userinfo=request.user, love_type=3, love_id=course.orginfo.id)
        if org_userlove:
            org_love = org_userlove[0].love_status
        if course_userlove:
            course_love = course_userlove[0].love_status

    return render(request, 'courses/course-detail.html',
                  {'course': course, 'rela_course': rela_course, 'org_love': org_love, 'course_love': course_love})


def course_video(request, course_id):
    course = CourseInfo.objects.get(pk=course_id)
    # 通过课程找用户
    user_course_obj = UserCourseInfo.objects.filter(courseinfo=course)
    # 通过用户找出ID
    userid_list = [user_course.userinfo_id for user_course in user_course_obj]
    # 找用户课程
    user_course_list = UserCourseInfo.objects.filter(Q(userinfo_id__in=userid_list) & ~Q(courseinfo=course))
    # 获得课程
    course_list = [user_course.courseinfo for user_course in user_course_list]
    # 去重
    course_list = list(set(course_list))[:3]
    return render(request, 'courses/course-video.html', {'course': course, 'course_list': course_list})


def course_comment(request, course_id):
    course = CourseInfo.objects.get(pk=course_id)
    user_course_obj = UserCourseInfo.objects.filter(courseinfo=course)
    user_id_list = [user_course.userinfo_id for user_course in user_course_obj]
    user_course_list = UserCourseInfo.objects.filter(Q(userinfo_id__in=user_id_list) & Q(courseinfo=course))
    course_list = [user_course.courseinfo for user_course in user_course_list]
    course_list = list(set(course_list))[0:3]
    return render(request, 'courses/course-comment.html', {'course': course, 'course_list': course_list})
