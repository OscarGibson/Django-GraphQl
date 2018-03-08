from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres_2',
        'USER': 'postgres',
        'PASSWORD': 'operationCwal0',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}

TIME_ZONE = 'UTC'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

MEDIA_ROOT = 'media'
MEDIA_URL = 'media/'
STATIC_ROOT = 'static'
STATIC_URL = 'static/'