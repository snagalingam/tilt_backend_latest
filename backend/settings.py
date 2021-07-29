import os

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
# Allowed hosts
################################################################################
ALLOWED_HOSTS = []


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

    # local
    'users.apps.UsersConfig',
    'api.apps.ApiConfig',

    # added
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
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


################################################################################
# Authentication
################################################################################
AUTH_USER_MODEL = 'users.User'


################################################################################
# Password Validation
################################################################################
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


################################################################################
# Internationalization
################################################################################
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True


################################################################################
# Static files (CSS, JavaScript, Images)
################################################################################
STATIC_URL = '/static/'


################################################################################
# Default primary key field type
################################################################################
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
