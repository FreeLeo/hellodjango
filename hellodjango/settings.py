"""
Django settings for hellodjango project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5=!^&q061-2gzig@4=osh2u0)j(smzlfg5r5j)qv9o3*foh_d&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'study',
    'rest_framework',
    "polls",
    'debug_toolbar',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "polls.middlewares.check_login_middleware",
]

# 下面的配置根据项目需要进行设置
REST_FRAMEWORK = {
    # 配置默认页面大小
    'PAGE_SIZE': 2,
    # 配置默认的分页类
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 配置异常处理器
    # 'EXCEPTION_HANDLER': '...',
    # 配置默认解析器
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    #     'rest_framework.parsers.FormParser',
    #     'rest_framework.parsers.MultiPartParser',
    # ),
    # 配置默认限流类
    # 'DEFAULT_THROTTLE_CLASSES': (
    #     '...'
    # ),
    # 配置默认授权类
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     '...',
    # ),
    # 配置默认认证类
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     '...',
    # ),
}

DEBUG_TOOLBAR_CONFIG = {
    # 引入jQuery库
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
    # 工具栏是否折叠
    'SHOW_COLLAPSED': True,
    # 是否显示工具栏
    'SHOW_TOOLBAR_CALLBACK': lambda x: True,
}

ROOT_URLCONF = "hellodjango.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hellodjango.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
    # 'default': {
    #     # 数据库引擎配置
    #     'ENGINE': 'django.db.backends.mysql',
    #     # 数据库的名字
    #     'NAME': 'vote',
    #     # 数据库服务器的IP地址（本机可以写localhost或127.0.0.1）
    #     'HOST': 'localhost',
    #     # 启动MySQL服务的端口号
    #     'PORT': 3306,
    #     # 数据库用户名和口令
    #     'USER': 'hellokitty',
    #     'PASSWORD': 'Hellokitty.618',
    #     # 数据库使用的字符集
    #     'CHARSET': 'utf8',
    #     # 数据库时间日期的时区设定
    #     'TIME_ZONE': 'Asia/Chongqing',
    # }
    'default': {
        # 数据库引擎配置
        'ENGINE': 'django.db.backends.mysql',
        # 数据库的名字
        'NAME': 'test_lizhen',
        # 数据库服务器的IP地址（本机可以写localhost或127.0.0.1）
        'HOST': 'localhost',
        # 启动MySQL服务的端口号
        'PORT': 3306,
        # 数据库用户名和口令
        'USER': 'root',
        'PASSWORD': '123456',
        # 数据库使用的字符集
        'CHARSET': 'utf8',
        # 数据库时间日期的时区设定
        'TIME_ZONE': 'Asia/Chongqing',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = "UTC"
TIME_ZONE = 'Asia/ShangHai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 配置会话的超时时间为1天（86400秒）
SESSION_COOKIE_AGE = 86400

# 设置为True在关闭浏览器窗口时session就过期
SESSION_EXPIRE_AT_BROWSER_CLOSE = True