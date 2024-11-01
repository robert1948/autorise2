import environ
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent


env = environ.Env()
environ.Env.read_env()


SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])


# AWS S3 Settings
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' if AWS_STORAGE_BUCKET_NAME else None
AWS_FILE_OVERWRITE = False


#print("SECRET_KEY:", env('SECRET_KEY', default="Not Set"))
#print("DEBUG:", env('DEBUG', default="Not Set"))
#print("ALLOWED_HOSTS:", env('ALLOWED_HOSTS', default="Not Set"))



STORAGES = {
   'default': {
       'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
   },
   'staticfiles': {
       'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
       'OPTIONS': {
           'location': 'static',
       },
   },
   'media': {
       'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
       'OPTIONS': {
           'location': 'media',
       },
   },
}


# Application definition


INSTALLED_APPS = [
   "django.contrib.admin",
   "django.contrib.auth",
   "django.contrib.contenttypes",
   "django.contrib.sessions",
   "django.contrib.messages",
   "django.contrib.staticfiles",
   "storages",
   "autorise",
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


ROOT_URLCONF = "autorise.urls"


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


WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators


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
#============================================
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


if AWS_STORAGE_BUCKET_NAME:
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:
    STATICFILES_DIRS = [BASE_DIR / "static"]
    STATIC_ROOT = BASE_DIR / "staticfiles"



# If you're using AWS S3 for static files, you should also set these
if AWS_S3_CUSTOM_DOMAIN:
   STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'


# Local storage fallback in case S3 is not used
STATICFILES_DIRS = [
   BASE_DIR / "static",  # You can change this if your static files are located elsewhere
]


# Default static files storage backend when using S3
if AWS_STORAGE_BUCKET_NAME:
   STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/


LANGUAGE_CODE = "en-us"


TIME_ZONE = "UTC"


USE_I18N = True


USE_TZ = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ChatGPT said:
ChatGPT
