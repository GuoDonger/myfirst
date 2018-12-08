from django.http import JsonResponse
from django.shortcuts import render
from .forms import UserAskForm, UserCommentForm
from .models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def user_ask(request):
    user_ask_form = UserAskForm(request.POST)
    if user_ask_form.is_valid():
        user_ask_form.save(commit=True)
        return JsonResponse({'status': 'ok', 'msg': '咨询成功！等待回复！'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '咨询失败！'})


def user_fav(request):
    love_type = request.GET.get('love_type', '')
    id = request.GET.get('id', '')
    if request.user.is_authenticated and love_type and id:
        user_love = UserLoveInfo.objects.filter(userinfo=request.user, love_type=love_type, love_id=id)
        if user_love:
            if user_love[0].love_status:
                user_love[0].love_status = False
                user_love[0].save()
                return JsonResponse({'status': 'ok', 'msg': '收藏'})
            else:
                user_love[0].love_status = True
                user_love[0].save()
                return JsonResponse({'status': 'ok', 'msg': '取消收藏'})
        else:
            UserLoveInfo.objects.create(userinfo=request.user, love_type=love_type, love_id=id, love_status=True)
            return JsonResponse({'status': 'ok', 'msg': '取消收藏'})
    else:
        return JsonResponse({'status': 'ok', 'msg': '用户还未登陆'})


@csrf_exempt
def user_comment(request):
    user_comment = UserCommentForm(request.POST)
    if user_comment.is_valid():
        content = user_comment.cleaned_data['content']
        course_id = user_comment.cleaned_data['course_id']
        if request.user.is_authenticated:
            user_comment_info = UserCommentInfo()
            user_comment_info.userinfo = request.user
            user_comment_info.courseinfo_id = course_id
            user_comment_info.content = content
            user_comment_info.save()
            return JsonResponse({'status': 'ok', 'msg': '评论发表成功！'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '用户未登录！'})
    return JsonResponse({'status': 'fail', 'msg': '评论发表失败！'})
