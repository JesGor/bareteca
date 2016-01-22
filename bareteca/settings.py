"""
Django settings for bareteca project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import django
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%c9cre=4iq4^1alkvvyi^bqkn)(v!%i1k*ffep-v5#5!b17#26'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bares',
    'registration',
    'easy_maps',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'bareteca.urls'

TEMPLATE_PATH= os.path.join(BASE_DIR,"templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ TEMPLATE_PATH],
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

WSGI_APPLICATION = 'bareteca.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEPLOY_HEROKU = os.environ.get('PORT')
if DEPLOY_HEROKU:
    DATABASE_URL='postgres://zcwonvuwfvvxuz:M8yUboyHfxb5pG7ODgrdVh6PB0@ec2-107-20-222-114.compute-1.amazonaws.com:5432/d8o5mrbg8eealv'
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'
STATIC_ROOT= 'staticfiles'
STATICFILES_DIRS = (
    STATIC_PATH,
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Registration options
# django-registration-redux

REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 0
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'

# Easy maps configuration
# django-easy-maps
if django.VERSION < (1, 7):
    INSTALLED_APPS += (
        'south',
    )
