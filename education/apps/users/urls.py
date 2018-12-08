"""education URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import *
from django.urls import path, re_path
from django.views.static import serve
from education.settings import STATIC_ROOT

app_name = 'users'
urlpatterns = [
    path('user_register/', user_register, name='user_register'),
    path('user_login/', user_login, name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
    path('user_forget/', user_forget, name='user_forget'),
    path('active/<str:code>/', user_active, name='user_active'),
    path('password_reset/<str:code>/', password_reset, name='password_reset'),
    path('user_info/', user_info, name='user_info'),
    path('user_change_info/', user_change_info, name='user_change_info'),
    path('user_change_image/', user_change_image, name='user_change_image'),
    path('user_course/', user_course, name='user_course'),
    path('user_fav/', user_fav, name='user_fav'),
    path('user_message/', user_message, name='user_message'),
    path('user_password/', user_password, name='user_password'),
    path('user_code/', user_code, name='user_code'),
    path('user_email/', user_email, name='user_email'),

    re_path(r'^static/(?P<path>.*)', serve, {'document_root': STATIC_ROOT}),
]
