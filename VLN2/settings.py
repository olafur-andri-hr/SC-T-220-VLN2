"""
Django settings for VLN2 project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
import django_heroku
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q3z-whmpgbl8p5_$7%ve_9ug!m9$ihoybcjlouw1o_ea4vye^x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["still-stream-97107.herokuapp.com",
                 "vln2.gng.is", "127.0.0.1", "localhost", "*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_countries',
    'phonenumber_field',
    'sass_processor',
    'imagekit',
    'storages',
    'rest_framework',
    'django_extensions',
    'location',
    'castleapartments',
    'apartments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'VLN2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'base/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'VLN2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kzedlyox',
        'USER': 'kzedlyox',
        'PASSWORD': '1e8_H6CaKNrbcCYUnac5YtsZMhSmDc_k',
        'HOST': 'manny.db.elephantsql.com',
        'PORT': '5432',
    }
}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Django',
        'USER': 'django',
        'PASSWORD': 'django_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
pass_val_path = 'django.contrib.auth.password_validation.'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': pass_val_path + 'UserAttributeSimilarityValidator', },
    {'NAME': pass_val_path + 'MinimumLengthValidator', },
    {'NAME': pass_val_path + 'CommonPasswordValidator', },
    {'NAME': pass_val_path + 'NumericPasswordValidator', },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "base/static"),
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
WHITENOISE_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'root')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]


SASS_PROCESSOR_ROOT = STATIC_ROOT

SASS_PRECISION = 8

SASS_OUTPUT_STYLE = 'compressed'

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(PROJECT_DIR, 'base/static/sass'),
]

PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'IS'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# AWS - django-storages
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = "AKIAQ73SZLIINOA3WKUG"
AWS_SECRET_ACCESS_KEY = "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"
AWS_AUTO_CREATE_BUCKET = True
AWS_STORAGE_BUCKET_NAME = "castleapartments2"
AWS_S3_REGION_NAME = "eu-west-1"
AWS_DEFAULT_ACL = "public-read"
AWS_BUCKET_ACL = None
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False

# Heroku
if 'ON_HEROKU' in os.environ:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
django_heroku.settings(locals())
