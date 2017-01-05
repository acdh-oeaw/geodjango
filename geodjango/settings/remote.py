from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bxhdf4ctlnz9^y2!mqcu0wi-6erde=o3ngm(e(sa-d9!@g+4n+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geodjango',
        'USER': 'geodjango',
        'PASSWORD': '6tXrLEXsqe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
