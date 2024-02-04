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
from django.urls import path

from myapp.views import show_index
from polls.views import show_subjects, show_teachers, praise_or_criticize, login, get_captcha, logout, get_teachers_data, show_teacher_charts
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", show_index),
    path('', show_subjects),
    path('teachers/', show_teachers),
    path('praise/', praise_or_criticize),
    path('criticize/', praise_or_criticize),
    path('login/', login),
    path('logout/', logout),
    path('captcha/', get_captcha),
    path('teachers_data/', get_teachers_data),
    path('show_teacher_charts', show_teacher_charts)
]
