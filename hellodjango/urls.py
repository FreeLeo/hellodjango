"""
URL configuration for hellodjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path

from myapp.views import show_index
from polls import rest_api
from polls.views import show_subjects, show_teachers, praise_or_criticize
from polls.views import get_captcha, logout, get_teachers_data
from polls.views import login, show_teacher_charts, show_subjects_vue
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from study import rest_api as study_api
from study.views import UserPermissionsAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", show_index),
    path('', show_subjects),
    path('subjects/vue/', show_subjects_vue),
    # path('api/subjects/', rest_api.show_subjects_json),
    path('teachers/', show_teachers),
    path('praise/', praise_or_criticize),
    path('criticize/', praise_or_criticize),
    path('login/', login),
    path('logout/', logout),
    path('captcha/', get_captcha),
    path('teachers_data/', get_teachers_data),
    path('show_teacher_charts', show_teacher_charts),

    path('rest/api/', rest_api.show_subjects_json),
    path('rest/api/teachers/', rest_api.show_teachers),

    # path('api/subjects/', rest_api.SubjectView.as_view()),
    
    path('study/permissions/<str:username>', UserPermissionsAPIView.as_view(), name='user_permissions_api'),
    path('study/login', study_api.studyLogin, name='login_api'),
    path('study/logout', study_api.studyLogout, name='logout_api'),
]

router = DefaultRouter()
router.register('api/subjects', rest_api.SubjectViewSet, basename='subject')
urlpatterns += router.urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.insert(0, path('__debug__/', include(debug_toolbar.urls)))
