SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  
]

THIRD_PARTY_APPS = [
    'decouple',
    'rest_framework',
    'corsheaders',
  
]

USER_APPS =[
    'users'
]

INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + USER_APPS