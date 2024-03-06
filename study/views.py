from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class UserPermissionsAPIView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            permissions = [str(permission) for permission in user.get_all_permissions()]
            return Response({'permissions': permissions})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
