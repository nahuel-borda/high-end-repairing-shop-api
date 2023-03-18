"""
Django settings for workshop_devices project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w06kf0njgkx21bpj+xd8egf+l018p-p=j+hn8z#f8*9(aeor%q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'admin_shortcuts',
    'devices',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'autocompletefilter',
    'rest_framework',
    'django_extensions',
    'corsheaders',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'workshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'workshop.wsgi.application'

ADMIN_SHORTCUTS_SETTINGS = {
    "show_on_all_pages": False,
    "hide_app_list": True,
    "open_new_window": False,
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

ADMIN_SHORTCUTS_SETTINGS = {
    'show_on_all_pages': True,
    'hide_app_list': False,
    'open_new_window': False,
}

STATIC_URL = '/static/'

ADMIN_SHORTCUTS = [
    {
        "title": "Quick Access",
        "shortcuts": [
            {"title": "Devices", "icon": "wrench", "url": "/admin/devices/device/"},
            {"title": "Brands", "icon": "wrench", "url": "/admin/devices/brand/"},
            {"title": "Models", "icon": "wrench", "url": "/admin/devices/model/"},
            {"title": "Clients", "icon": "user", "url": "/admin/devices/client/"},
            {"title": "Operators", "icon": "user", "url": "/admin/devices/operator/"},
            {"title": "Providers", "icon": "users", "url": "/admin/devices/provider/"},
            {"title": "Services", "icon": "wrench", "url": "/admin/devices/service/"},
            {"title": "Parts", "icon": "cogs", "url": "/admin/devices/part/"},
        ],
    }
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

CORS_ORIGIN_ALLOW_ALL = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/code/django_cache",
    }
}
