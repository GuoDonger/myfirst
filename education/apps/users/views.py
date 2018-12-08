import random
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from education.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect, reverse

from orgs.models import OrgInfo, TeacherInfo
from .forms import *
from .models import *
from operations.models import *


# Create your views here.
def index(request):
    banner = Banner.objects.all()
    courses = CourseInfo.objects.all()
    return render(request, 'index.html', {'banner': banner, 'courses': courses})


def user_register(request):
    if request.method == 'GET':
        user_register_form = UserRegisterForm()
        return render(request, 'users/register.html', {'user_register_form': user_register_form})
    else:
        user = UserRegisterForm(request.POST)
        if user.is_valid():
            email = user.cleaned_data['email']
            password = user.cleaned_data['password']
            u = UserProfile.objects.filter(Q(username=email) | Q(email=email))
            if u:
                return render(request, 'users/register.html', {'msg': '此邮箱已被注册'})
            else:
                user_profile = UserProfile()
                user_profile.email = email
                user_profile.username = email
                user_profile.set_password(password)
                user_profile.is_active = 0
                user_profile.save()
                send_email(email, 'register')
                return HttpResponse('注册成功，去激活吧！')
        else:
            return render(request, 'users/register.html', {'user_register_form': user})


def user_active(request, code):
    if code:
        emailobj = EmailVerify.objects.filter(code=code)
        if emailobj:
            email = emailobj[0].email
            user = UserProfile.objects.filter(Q(username=email) | Q(email=email))
            if user:
                user[0].is_active = 1
                user[0].save()
                return render(request, 'index.html')
            else:
                return HttpResponse('邮箱激活失败！')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    else:
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user:
                if user.is_active == 1:
                    login(request, user)
                    return redirect(reverse('index'))
                else:
                    return HttpResponse('账号还未激活！')
            else:
                return render(request, 'users/login.html', {'msg': '用户名或者密码错误'})
        else:
            return render(request, 'users/login.html', {'user_form': user_form})


def user_logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect(reverse('index'))


def user_forget(request):
    if request.method == 'GET':
        user_forget_form = UserForgetForm()
        return render(request, 'users/forgetpwd.html', {'user_forget_form': user_forget_form})
    else:
        user_form = UserForgetForm(request.POST)
        if user_form.is_valid():
            email = user_form.cleaned_data['email']
            user = UserProfile.objects.filter(email=email)
            if user:
                send_email(email, 'update')
                return HttpResponse('快去邮箱点击链接吧！')
            else:
                return render(request, 'users/forgetpwd.html', {'msg': '无此邮箱'})
        else:
            return render(request, 'users/forgetpwd.html', {'user_form': user_form})


def password_reset(request, code):
    if request.method == "GET":
        if code:
            emailobj = EmailVerify.objects.filter(code=code)
            if emailobj:
                email = emailobj[0].email
                user = UserProfile.objects.filter(Q(username=email) | Q(email=email))
                if user:
                    return render(request, 'users/password_reset.html', {'user': user[0]})
            else:
                return HttpResponse("邮箱激活失败！")
    else:
        user_form = ResetPasswordForm(request.POST)
        if user_form.is_valid():
            uid = user_form.cleaned_data['user_id']
            password = user_form.cleaned_data['password']
            password1 = user_form.cleaned_data['password1']
            user = UserProfile.objects.get(pk=uid)
            if user and password == password1:
                user.set_password(password)
                user.save()
                return redirect(reverse('users:user_login'))
            else:
                return render(request, 'users/password_reset.html', {'msg': '密码不一致或者用户不存在'})
        else:
            return render(request, 'users/password_reset.html', {'user_form': user_form})


def get_random(length):
    str0 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(length):
        ran = random.randint(0, len(str0) - 1)
        code += str0[ran]
    return code


def send_email(email, send_type):
    code = get_random(8)
    email_verify = EmailVerify()
    email_verify.email = email
    email_verify.code = code
    email_verify.send_type = send_type
    email_verify.save()
    if send_type == 'register':
        subject = '欢迎注册在线教育网站'
        content = 'http://127.0.0.1:8000/users/active/' + code
        send_mail(subject, content, EMAIL_HOST_USER, [email, ], html_message=content)
    if send_type == 'update':
        subject = '正在修改密码'
        content = 'http://127.0.0.1:8000/users/password_reset/' + code
        send_mail(subject, content, EMAIL_HOST_USER, [email, ], html_message=content)


def user_info(request):
    return render(request, 'users/usercenter-info.html')


def user_change_info(request):
    user_change_form = UserChangeForm(request.POST, request.FILES, instance=request.user)
    if user_change_form.is_valid():
        user_change_form.save(commit=True)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'fail'})


def user_change_image(request):
    user_change_image = UserChangeImageForm(request.POST, request.FILES, instance=request.user)
    if user_change_image.is_valid():
        user_change_image.save(commit=True)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'fail'})


def user_course(request):
    user_course_list = UserCourseInfo.objects.filter(userinfo=request.user)
    all_course = [user_course.courseinfo for user_course in user_course_list]
    return render(request, 'users/usercenter-mycourse.html', {'all_course': all_course})


def user_fav(request):
    type = request.GET.get('type')
    type_id = request.GET.get('type_id')

    user_fav_list = UserLoveInfo.objects.filter(userinfo=request.user, love_type=type_id, love_status=True)
    all_fav_id = [user_fav.love_id for user_fav in user_fav_list]

    if type == 'course':
        all_fav = CourseInfo.objects.filter(id__in=all_fav_id)
    elif type == 'org':
        all_fav = OrgInfo.objects.filter(id__in=all_fav_id)
    elif type == 'teacher':
        all_fav = TeacherInfo.objects.filter(id__in=all_fav_id)
    return render(request, 'users/usercenter-fav-' + type + '.html', {'all_fav': all_fav})


def user_message(request):
    user_message_list = UserMessageInfo.objects.filter(userinfo=request.user)
    all_message = [user_message for user_message in user_message_list]

    page_num = request.GET.get('page', 1)
    paginator = Paginator(all_message, 3)

    try:
        page_list = paginator.page(page_num)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)
    return render(request, 'users/usercenter-message.html', {'all_message': all_message, 'page_list': page_list})


def user_password(request):
    pwd = request.POST.get('pwd')
    repwd = request.POST.get('repwd')
    if pwd == repwd:
        user = request.user
        user.set_password(pwd)
        user.save()
        return JsonResponse({'status': 'ok', 'msg': '修改成功'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '密码不一致'})


def user_email(request):
    code = request.POST.get('code')
    email = request.POST.get('email')
    user = request.user
    email_code = EmailVerify.objects.filter(code=code)
    if code == email_code[0].code:
        user.email = email
        user.username = email
        user.save()
        return JsonResponse({'status': 'ok', 'msg': '修改成功'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '验证码错误'})


def user_code(request):
    email = request.POST.get('email')
    user_email = UserProfile.objects.filter(email=email)
    code = get_random(4)
    if user_email:
        return JsonResponse({'status': 'fail', 'msg': '邮箱已被注册'})
    else:
        EmailVerify.objects.create(email=email, code=code, send_type='update')
        subject = '正在修改邮箱'
        content = code
        send_mail(subject, content, EMAIL_HOST_USER, [email, ])
        return JsonResponse({'status': 'ok', 'msg': '快去邮箱查看吧'})


def handler_404(request):
    ret = render(request, '404.html')
    ret.status_code = 404
    return ret


def handler_500(request):
    ret = render(request, '500.html')
    ret.status_code = 500
    return ret
