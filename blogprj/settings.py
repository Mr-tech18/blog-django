

from pathlib import Path
import os
from environ import Env
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env=Env()
Env.read_env(os.path.join(BASE_DIR,'.env'))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=env('SECRET_KEY_NEW')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', '127.0.0.1', 'localhost']



# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    #custom app
    'core',
    'userauth',
    'taggit',
    'author_page',
    'otp',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'author_page.middleware.AuthorMiddleware1',
]

ROOT_URLCONF = 'blogprj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                    os.path.join(BASE_DIR,"templates"),
                    os.path.join(BASE_DIR,"author_page/templates"),
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'core.context_processor.general',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogprj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}
DATABASES = {
  'default': {
  'ENGINE': 'django.db.backends.postgresql_psycopg2',
  'NAME': 'my_db',
  'USER' : 'atain',
  'PASSWORD' : env('DB_PASSWORD'),
  'HOST' : env('HOST'),
  'PORT' : '5432',
  }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
#STATICFILES_STORAGE='django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATIC_URL = 'static/'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS=[os.path.join(BASE_DIR,'core/static')]
MEDIA_URL='media/'
MEDIA_ROOT=os.path.join(BASE_DIR,"media")

# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#custom user models
AUTH_USER_MODEL='userauth.CustomUser'

#jazzmin

JAZZMIN_SETTINGS={
    "site_brand":'Hold the vision',
    'copyright':'Mr-Tech18 dev',
    'site_header':'TG-18 BLOG',
    'site_logo':'static/assets/images/10.jpg'
}

LOGIN_REDIRECT_URL='core:redirection'

# email configuration
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER="techgroupe18@gmail.com"
EMAIL_HOST_PASSWORD=env('EMAIL_HOST_PASSWORD')
EMAIL_PORT=587
EMAIL_USE_TLS=True

AUTHENTICATION_BACKENDS=[
    'django.contrib.auth.backends.ModelBackend',
    'author_page.backend.AuthorAuthenticationEmail',
    'author_page.backend.AuthorAuthenticationName',
]


ACCOUNT_SID=env('ACCOUNT_SID')
AUTH_TOKEN=env('AUTH_TOKEN')
COUNTRY_CODE='+237'
TWILIO_WHATSAPP_NUMBER='+14155238886'
TWILIO_PHONE_NUMBER='+12316254727'

SITE_ID=1


AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'atainsite' 
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERIFY = True
AWS_S3_FILE_OVERWRITE=False
AWS_QUERYSTRING_AUTH=False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

