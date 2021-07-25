import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%qq+6@ri#%nvf@gdwh3p!c+qvhh@(ge1u%3j4)kb)dan#yj@*9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'courses.apps.CoursesConfig',
    'telegrambots.apps.TelegrambotsConfig',
    'accounts.apps.AccountsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'brainskill_123.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'brainskill_123.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    BASE_DIR / "courses/static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DATETIME_INPUT_FORMATS = (
    '%d %B %Y - %H:%M:%S.%f',  # '05 March 2014 - 08:07:59.0001'
    '%d %B %Y - %H:%M:%S',     # '05 March 2014 - 08:07:59'
    '%d %B %Y - %H:%M',        # '05 March 2014 - 08:07'
    '%d %B %Y',                # '05 March 2014' <- this line was first before

    '%d/%m/%Y %H:%M:%S.%f',    # '25/10/05 14:30:59.000200'
    '%d/%m/%Y %H:%M:%S',       # '25/10/05 14:30:59'
    '%d/%m/%Y %H:%M',          # '25/10/05 14:30'
    '%d/%m/%Y',                # '25/10/05'

    '%d-%m-%Y %H:%M:%S.%f',    # '25-10-05 14:30:59.000200'
    '%d-%m-%Y %H:%M:%S',       # '25-10-05 14:30:59'
    '%d-%m-%Y %H:%M',          # '25-10-05 14:30'
    '%d-%m-%Y',                # '25-10-05'

    '%Y-%m-%d %H:%M:%S.%f',    # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M:%S',       # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M',          # '2006-10-25 14:30'
    '%Y-%m-%d',                # '2006-10-25'

    '%m/%d/%Y %H:%M:%S.%f',    # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M:%S',       # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M',          # '10/25/2006 14:30'
    '%m/%d/%Y',                # '10/25/2006'

    '%m/%d/%y %H:%M:%S.%f',    # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M:%S',       # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M',          # '10/25/06 14:30'
    '%m/%d/%y',                # '10/25/06'
)