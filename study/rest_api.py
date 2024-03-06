from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from polls.models import Subject, SubjectMapper, Teacher
from polls.pagination import CustomizedPagination
from polls.serializers import SubjectSerializer, TeacherSerializer
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@api_view(('GET', ))
def show_user_permissions(request: HttpRequest):
    user = User.objects.get(username='lisi')
    permissions = user.user_permissions.all()

    for permission in permissions:
        print(permission.codename)
    return Response()

@csrf_exempt
@require_POST
def studyLogin(request):
    # 从请求中获取用户名和密码
    username = request.POST.get('username')
    password = request.POST["password"]

    # 使用 authenticate 函数验证用户
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # 登录用户
        login(request, user)
        return JsonResponse({'status': 'success', 'message': 'Login successful'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid credentials'})

@csrf_exempt
@require_POST
def studyLogout(request):
    # 注销用户
    logout(request)
    return JsonResponse({'status': 'success', 'message': 'Logout successful'})