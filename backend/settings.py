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
    'drfpasswordless',

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
# database for development without SSL
if ENVIRONMENT == 'development':
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

# database for staging and production with SSL
if ENVIRONMENT == 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DATABASE_NAME'),
            'USER': os.environ.get('DATABASE_USER'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
            'HOST': os.environ.get('DATABASE_HOST'),
            'PORT': 5432,
            'OPTIONS':{
                'sslmode':'verify-ca'
            }
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
        'rest_framework.authentication.TokenAuthentication'
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
# Email
################################################################################
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

################################################################################
# Passwordless settings
################################################################################
PASSWORDLESS_AUTH = {
    # Allowed auth types, can be EMAIL, MOBILE, or both.
    'PASSWORDLESS_AUTH_TYPES': ['EMAIL'],

    # URL Prefix for Authentication Endpoints
    'PASSWORDLESS_AUTH_PREFIX': 'code-auth/',

    #  URL Prefix for Verification Endpoints
    'PASSWORDLESS_VERIFY_PREFIX': 'code-auth/verify/',

    # Amount of time that tokens last, in seconds
    'PASSWORDLESS_TOKEN_EXPIRE_TIME': 5 * 60,

    # The user's email field name
    'PASSWORDLESS_USER_EMAIL_FIELD_NAME': 'email',

    # The user's mobile field name
    'PASSWORDLESS_USER_MOBILE_FIELD_NAME': 'mobile',

    # Marks itself as verified the first time a user completes auth via token.
    # Automatically unmarks itself if email is changed.
    'PASSWORDLESS_USER_MARK_EMAIL_VERIFIED': False,
    'PASSWORDLESS_USER_EMAIL_VERIFIED_FIELD_NAME': 'email_verified',

    # Marks itself as verified the first time a user completes auth via token.
    # Automatically unmarks itself if mobile number is changed.
    'PASSWORDLESS_USER_MARK_MOBILE_VERIFIED': False,
    'PASSWORDLESS_USER_MOBILE_VERIFIED_FIELD_NAME': 'mobile_verified',

    # The email the callback token is sent from
    'PASSWORDLESS_EMAIL_NOREPLY_ADDRESS': 'noreply@tiltaccess.com',

    # The email subject
    'PASSWORDLESS_EMAIL_SUBJECT': "Your Login Token",

    # A plaintext email message overridden by the html message. Takes one string.
    'PASSWORDLESS_EMAIL_PLAINTEXT_MESSAGE': "Enter this token to sign in: %s",

    # The email template name.
    'PASSWORDLESS_EMAIL_TOKEN_HTML_TEMPLATE_NAME': "passwordless_default_token_email.html",

    # Your twilio number that sends the callback tokens.
    'PASSWORDLESS_MOBILE_NOREPLY_NUMBER': None,

    # The message sent to mobile users logging in. Takes one string.
    'PASSWORDLESS_MOBILE_MESSAGE': "Use this code to log in: %s",

    # Registers previously unseen aliases as new users.
    'PASSWORDLESS_REGISTER_NEW_USERS': False,

    # Suppresses actual SMS for testing
    'PASSWORDLESS_TEST_SUPPRESSION': False,

    # Context Processors for Email Template
    'PASSWORDLESS_CONTEXT_PROCESSORS': [],

    # The verification email subject
    'PASSWORDLESS_EMAIL_VERIFICATION_SUBJECT': "Your Verification Token",

    # A plaintext verification email message overridden by the html message. Takes one string.
    'PASSWORDLESS_EMAIL_VERIFICATION_PLAINTEXT_MESSAGE': "Enter this verification code: %s",

    # The verification email template name.
    'PASSWORDLESS_EMAIL_VERIFICATION_TOKEN_HTML_TEMPLATE_NAME': "passwordless_default_verification_token_email.html",

    # The message sent to mobile users logging in. Takes one string.
    'PASSWORDLESS_MOBILE_VERIFICATION_MESSAGE': "Enter this verification code: %s",

    # Automatically send verification email or sms when a user changes their alias.
    'PASSWORDLESS_AUTO_SEND_VERIFICATION_TOKEN': False,

    # What function is called to construct an authentication tokens when
    # exchanging a passwordless token for a real user auth token. This function
    # should take a user and return a tuple of two values. The first value is
    # the token itself, the second is a boolean value representating whether
    # the token was newly created.
    'PASSWORDLESS_AUTH_TOKEN_CREATOR': 'drfpasswordless.utils.create_authentication_token',

    # What function is called to construct a serializer for drf tokens when
    # exchanging a passwordless token for a real user auth token.
    'PASSWORDLESS_AUTH_TOKEN_SERIALIZER': 'drfpasswordless.serializers.TokenResponseSerializer',

    # A dictionary of demo user's primary key mapped to their static pin
    'PASSWORDLESS_DEMO_USERS': {},

    # configurable function for sending email
    'PASSWORDLESS_EMAIL_CALLBACK': 'drfpasswordless.utils.send_email_with_callback_token',

    # configurable function for sending sms
    'PASSWORDLESS_SMS_CALLBACK': 'drfpasswordless.utils.send_sms_with_callback_token',

    # Token Generation Retry Count
    'PASSWORDLESS_TOKEN_GENERATION_ATTEMPTS': 3
}


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
        '.herokuapp.com',
        '.tiltaccess.com',
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
