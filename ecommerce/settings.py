#for log
import logging
import logging.config
import os
from datetime import timedelta
from pathlib import Path

from decouple import config
from environs import Env

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = env.str("SECRET_KEY")

# DEBUG =env.bool('DEBUG', default=False)


DEBUG = False


ALLOWED_HOSTS = ['smartsytem.uz']


# Application definition
INSTALLED_APPS = [
#     'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'comment',
    'blog',
    'account',
    'extensions',
    'mptt',
    'clickuz',
    'rest_framework',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'rest_framework_simplejwt',
    'django_filters',
    'corsheaders',
    'django_countries',
    'ckeditor',
    'product',
    'tolov',
    'filter',
    'search',
    'Banner',


]
JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "theme": "slate",
}

JAZZMIN_SETTINGS = {
    "site_title": "HIKVISION Admin",
    "site_header": "HIKVISION",
    "site_brand": "HIKVISION",
}
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_ALLOW_ALL = False
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:3000',
#     'http://localhost:8000'
# )



MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
#     'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CACHE_MIDDLEWARE_SECONDS = 300

ROOT_URLCONF = 'ecommerce.urls'

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

WSGI_APPLICATION = 'ecommerce.wsgi.application'



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTRGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': '5432',
    }
}
# DATABASES = {
#     "default": env.dj_db_url("DATABASE_URL")      
#   } 




# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent' 
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N=True

USE_TZ = True

AUTH_USER_MODEL = 'account.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR.joinpath('static'))
MEDIA_URL = "/media/"

MEDIA_ROOT = str(BASE_DIR.joinpath('media'))
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'permissions.IsSuperUserOrReadOnly',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': [
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer',
    ],
    
    'DEFAULT_THROTTLE_RATES': {
        "authentication": "5/hour",
        "verify_authentication": "8/hour",
    },
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30), 
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1), 
    'ROTATE_REFRESH_TOKENS': False, 
    'BLACKLIST_AFTER_ROTATION': True, 
    'UPDATE_LAST_LOGIN': False, 
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    # # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_PAGINATION_CLASS': 'ecommerce.utils.custom_pagination.CustomPagination',
    'PAGE_SIZE': 12,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
}



SPECTACULAR_SETTINGS = {
    'TITLE': 'Elektron dokon',
    'DESCRIPTION': 'Bu mening birinchi backend yozgan dasturim',
    'VERSION': '1.0',
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
}


EXPIRY_TIME_OTP = 300

SMS_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjgyOCwicm9sZSI6InVzZXIiLCJkYXRhIjp7ImlkIjo4MjgsIm5hbWUiOiJPT08gU01BUlQgVEVDSE5PTE9HWSBTWVNURU1TIiwiZW1haWwiOiJhemFtYXRzYWJpbmExNzk2QG1haWwucnUiLCJyb2xlIjoidXNlciIsImFwaV90b2tlbiI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUp6ZFdJaU9qZ3lPQ3dpY205c1pTSTZJblZ6WlhJaUxDSmtZWFJoSWpwN0ltbGtJam80TWpnc0ltNWhiV1VpT2lKUFQwOGdVMDFCVWxRZ1ZFVkRTRTVQVEU5SFdTQlRXVk5VUlUxVElpd2laVzFoYVd3aU9pSmhlbUZ0WVhSellXSnBibUV4TnprMlFHMWhhV3d1Y25VaUxDSnliMnhsSWpvaWRYTmxjaUlzSW1Gd2FWOTBiMnRsYmlJNmJuVnNiQ3dpYzNSaGRIVnpJam9pWVdOMGFYWmxJaSIsInN0YXR1cyI6ImFjdGl2ZSIsInNtc19hcGlfbG9naW4iOiJlc2tpejIiLCJzbXNfYXBpX3Bhc3N3b3JkIjoiZSQkayF6IiwidXpfcHJpY2UiOjUwLCJ1Y2VsbF9wcmljZSI6NTAsImJhbGFuY2UiOjI4NDY1MCwiaXNfdmlwIjowLCJob3N0Ijoic2VydmVyMSIsImNyZWF0ZWRfYXQiOiIyMDIyLTA0LTI3VDA1OjI1OjM1LjAwMDAwMFoiLCJ1cGRhdGVkX2F0IjoiMjAyMi0wOC0xMlQwNjozNzo1Mi4wMDAwMDBaIn0sImlhdCI6MTY2MDI4NjQ3OCwiZXhwIjoxNjYyODc4NDc4fQ.dM6yrW5JcT8KbHklPom34zWhxBdTv5Bul9Ni1eNDXLU'


CLICK_SETTINGS = {
    'service_id': '23718',
    'merchant_id': '7844',
    'secret_key': 'NMW01rhKZXIjCu',
    'merchant_user_id': '26660'
}


logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
        },
        "handlers": {
            "file": {
                "level": "ERROR",
                "class": "logging.FileHandler",
                "formatter": "file",
                "filename": "debug.log",
            },
        },
        "loggers": {
            "": {"level": "ERROR", "handlers": [ "file"]},
            "django.request": {"level": "INFO", "handlers": [ "file"]},
        },
    }
)

