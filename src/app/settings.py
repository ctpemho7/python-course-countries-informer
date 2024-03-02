"""
Django settings for project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
import sys
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = environ.Path(__file__) - 4

env = environ.Env()
env.read_env(ROOT_DIR(".env"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    "rest_framework",
    "django_celery_beat",
    "geo.apps.GeoConfig",
    "news.apps.NewsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "app.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = "ru-RU"

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
USE_TZ = True
TIME_ZONE = "Europe/Moscow"
DATE_FORMAT = "d E Y"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(ROOT_DIR, "static")

MEDIA_ROOT = os.path.join(ROOT_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# настройки логирования
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "level": "INFO",
            "handlers": ["console"],
        }
    },
}

# настройки кэширования
REDIS_HOST = env("REDIS_HOST")
REDIS_PORT = env("REDIS_PORT")
BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/"

# время актуальности данных о курсах валют (в секундах), по умолчанию – сутки
CACHE_TTL_CURRENCY_RATES: int = int(os.getenv("CACHE_TTL_CURRENCY_RATES", "86_400"))
# время актуальности данных о погоде (в секундах), по умолчанию ~ три часа
CACHE_TTL_WEATHER: int = int(os.getenv("CACHE_TTL_WEATHER", "10_700"))
# время актуальности данных о новостях (в секундах), по умолчанию - час
CACHE_TTL_NEWS: int = int(os.getenv("CACHE_TTL_WEATHER", "3_600"))

CACHE_WEATHER = "cache_weather"
CACHE_CURRENCY = "cache_currency"
CACHE_NEWS = "cache_news"
CACHES = {
    # общий кэш приложения
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": BROKER_URL,
        "OPTIONS": {"db": "0"},
    },
    # кэширование данных о погоде
    CACHE_WEATHER: {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": BROKER_URL,
        "KEY_PREFIX": "weather",
        "OPTIONS": {"db": "1"},
        "TIMEOUT": CACHE_TTL_WEATHER,
    },
    # кэширование данных о курсах валют
    CACHE_CURRENCY: {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": BROKER_URL,
        "KEY_PREFIX": "currency",
        "OPTIONS": {"db": "2"},
        "TIMEOUT": CACHE_TTL_CURRENCY_RATES,
    },
    # кэширование данных о новостях
    CACHE_NEWS: {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": BROKER_URL,
        "KEY_PREFIX": "news",
        "OPTIONS": {"db": "3"},
        "TIMEOUT": CACHE_TTL_NEWS,
    },
}

# настройки для Celery
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_TIMEZONE = TIME_ZONE
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# строка подключения к RabbitMQ
RABBITMQ_URI = os.getenv(
    "RABBITMQ_URI", "amqp://user:secret@countries-informer-rabbitmq:5672"
)
# название очереди для импорта гео-данных
RABBITMQ_QUEUE_PLACES_IMPORT = os.getenv(
    "RABBITMQ_QUEUE_PLACES_IMPORT", "places_import"
)

# токен доступа к API для получения сведений о странах
API_KEY_APILAYER = env("API_KEY_APILAYER")
# токен доступа к API для получения сведений о погоде
API_KEY_OPENWEATHER = env("API_KEY_OPENWEATHER")
# токен доступа к API для получения последних новостей
API_KEY_NEWSAPI = env("API_KEY_NEWSAPI")
# таймаут запросов на внешние ресурсы
REQUESTS_TIMEOUT = env.int("REQUESTS_TIMEOUT")


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
}

if DEBUG:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
    INTERNAL_IPS = [
        "127.0.0.1",
        "localhost",
        "172.20.0.6",
    ]
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ]
