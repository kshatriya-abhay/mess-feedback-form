import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hab_portal',
        'USER': 'rajas',
        'PASSWORD': 'rajasB6*3',
        'HOST': 'localhost',
        'PORT': '',
    }
}
DEBUG = True

ALLOWED_HOSTS = ['*',]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR,"static")
MEDIA_DIR = os.path.join(BASE_DIR,"media")

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'
