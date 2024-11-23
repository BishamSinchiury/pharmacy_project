# SECURITY WARNING: don't run with debug turned on in production!


from pharmacy_backend.settings.base import *

from decouple import config
# SECURITY WARNING: don't run with debug turned on in production!

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myprojectdb', 
        'USER': 'myuser',       
        'PASSWORD': 'mypassword',
        'HOST': ['localhost','127.0.0.1'],    
        'PORT': '5432',        
    }
}
