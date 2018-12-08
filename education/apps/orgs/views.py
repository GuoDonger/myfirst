from django.db.models import Count
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def orgs_list(request):
    org_all = OrgInfo.objects.all()
    citys_all = CityInfo.objects.all()
    orgs_sort = org_all.order_by('-click_num')[:3]

    cityid = request.GET.get('city', '')
    if cityid:
        org_all = org_all.filter(cityinfo=cityid)

    category = request.GET.get('ct', '')
    if category:
        org_all = org_all.filter(category=category)

    sort = request.GET.get('sort', '')
    if sort == 'student_num':
        org_all.order_by('-study_num')
    elif sort == 'course_num':
        org_all = OrgInfo.objects.all().annotate(course_num=Count('courseinfo')).order_by('-course_num')

    page_num = request.GET.get('page', 1)
    paginator = Paginator(org_all, 3)
    try:
        page_list = paginator.page(page_num)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)

    data = {'orgs_all': org_all, 'page_list': page_list, 'category': category, 'citys_all': citys_all,
            'cityid': cityid, 'sort': sort, 'orgs_sort': orgs_sort}
    return render(request, 'orgs/org-list.html', data)


def org_detail(request, org_id):
    tag = request.GET.get('tag')
    if tag:
        org = OrgInfo.objects.get(pk=org_id)
    return render(request, 'orgs/org-detail-' + tag + '.html', {'org': org, 'tag': tag})


def teachers_list(request):
    teacher_all = TeacherInfo.objects.all()
    teacher_sort = teacher_all.order_by('-click_num')[:3]
    sort = request.GET.get('sort', '')

    if sort == 'hot':
        teacher_all = teacher_all.order_by('-click_num')

    page_num = request.GET.get('page', 1)
    paginator = Paginator(teacher_all, 3)
    try:
        page_list = paginator.page(page_num)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    return render(request, 'orgs/teachers-list.html',
                  {'teacher_sort': teacher_sort, 'page_list': page_list, 'sort': sort, 'teacher_all': teacher_all})


def teacher_detail(request, teacher_id):
    teacher = TeacherInfo.objects.get(pk=teacher_id)
    teacher_sort = TeacherInfo.objects.filter(orginfo=teacher.orginfo).order_by('click_num')[:3]
    return render(request, 'orgs/teacher-detail.html', {'teacher': teacher, 'teacher_sort': teacher_sort})
