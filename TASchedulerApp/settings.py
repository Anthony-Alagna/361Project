"""
Django settings for TASchedulerApp project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Determine the environment (development, production, etc.)
env = os.getenv("ENVIRONMENT", "development")

# Load the appropriate dotenv file based on the environment
if env == "production":
    dotenv_path = os.path.join(BASE_DIR, "prod.env")
else:
    dotenv_path = os.path.join(BASE_DIR, ".env")

# Load the environment variables
load_dotenv(dotenv_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "") == "True"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myapp.apps.MyappConfig",
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

ROOT_URLCONF = "TASchedulerApp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "TASchedulerApp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE"),
        "NAME": os.path.join(BASE_DIR, os.getenv("DB_NAME", "db.sqlite3")),
    }
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

if env == "development":
    ALLOWED_HOSTS = [
        '127.0.0.1',
        'localhost',
    ]
    CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8006", "http://localhost:8006"]
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email settings
EMAIL_HOST = os.getenv("MAIL_SERVER")
EMAIL_PORT = '587'
EMAIL_HOST_USER = os.getenv("MAIL_USERNAME")
MAIL_HOST_PASSWORD = os.getenv("MAIL_PASSWORD")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv("MAIL_USERNAME")

# CSRF settings for local development
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# production settings
if env == "production":
    # Set the database configuration for production
    DATABASES = {
        'default': {
            "ENGINE": os.getenv("DB_ENGINE"),
            "NAME": os.path.join(BASE_DIR, os.getenv("DB_NAME")),
        }
    }
    CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS = ["http://204.48.17.50", "204.48.17.50", "http://tascheduler.aalagna.com",
                                            "https://tascheduler.aalagna.com", "tascheduler.aalagna.com"]  # is this bad syntax?

    # Use secure HTTPS connections for cookies and sessions
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
