from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserTestCase(TestCase):
    def setUp(self):
        # 在数据库中创建一个用户用于测试
        self.user = User.objects.create_superuser(username='ceshi', password='password123')
    
    def test_get_user(self):
        user = User.objects.get(username='ceshi')
        print(user)
        self.assertEqual(user, self.user)
        
    def test_auth_user(self):
        user = authenticate(username='ceshi', password='password123')
        if user is not None:
            print('authenticate 成功')
        else:
            print('authenticate 失败')
    
    def test_permissions(self):
        user = User.objects.get(username='ceshi')
        permissions = user.user_permissions.all()
        print(f'权限数量：{len(permissions)}')
        for permission in permissions:
            print(permission.codename)