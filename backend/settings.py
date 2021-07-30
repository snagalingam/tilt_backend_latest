import os
import datetime
import dj_database_url

from pathlib import Path


################################################################################
# Standard Variables
################################################################################
DEBUG = os.environ.get('DEBUG', default=0)
ENVIRONMENT = os.environ.get('ENVIRONMENT', default='production')
SECRET_KEY = os.environ.get('SECRET_KEY')


################################################################################
# Build paths inside the project like this: BASE_DIR / 'subdir'.
################################################################################
BASE_DIR = Path(__file__).resolve().parent.parent


################################################################################
# Application definition
################################################################################
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # added
    'django.contrib.sites',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',

    # local
    'users.apps.UsersConfig',
    'api.apps.ApiConfig',
]

MIDDLEWARE = [
    'django_samesite_none.middleware.SameSiteNoneMiddleware', #added
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware', #added
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


################################################################################
# Database
################################################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': 5432,
    }
}

# for heroku
db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)

################################################################################
# Authentication
################################################################################
AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
}

################################################################################
# Password
################################################################################
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8, }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


################################################################################
# Internationalization
################################################################################
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True

################################################################################
# Site information
################################################################################
SITE_ID = 1

################################################################################
# Static files (CSS, JavaScript, Images)
################################################################################
STATIC_URL = '/static/'


################################################################################
# Default primary key field type
################################################################################
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


################################################################################
# Session Cookies
################################################################################
if ENVIRONMENT == 'development':
    SESSION_COOKIE_DOMAIN = 'localhost'
else:
    SESSION_COOKIE_DOMAIN = '.tiltaccess.com'
SESSION_COOKIE_SAMESITE = 'lax'

################################################################################
# Security
################################################################################
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "https://tiltaccess.com",
    "https://www.tiltaccess.com",
    "https://tiltstaging.dev"
]
CSRF_TRUSTED_ORIGINS = [
    "tiltaccess.com",
    "www.tiltaccess.com",
    "tiltstaging.dev",
]

# security for development
if ENVIRONMENT == 'development':
    ALLOWED_HOSTS = [
        '0.0.0.0',
        '127.0.0.1',
        'localhost',
        '.amazonaws.com',
        '.elasticbeanstalk.com',
        '.tiltstaging.dev'
    ]
    CORS_ORIGIN_ALLOW_ALL = True

# security for production
elif ENVIRONMENT == 'production':
    ALLOWED_HOSTS = [
        '0.0.0.0',
        '.amazonaws.com',
        '.elasticbeanstalk.com',
        '.tiltaccess.com',
        '.tiltstaging.com',
        '.tiltstaging.dev',
    ]
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_REFERRER_POLICY = 'same-origin'
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'DENY'
