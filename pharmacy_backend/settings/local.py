from pharmacy_backend.settings.base import *
from decouple import config
# SECURITY WARNING: don't run with debug turned on in production!

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'), 
        'USER': config('DB_USERNAME'),       
        'PASSWORD': config('DB_PASS'), 
        'HOST': config('DB_HOST'),     
        'PORT': config('DB_PORT'),         
    }
}
