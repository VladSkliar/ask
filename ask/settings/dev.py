from common import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = 'd6%)2hin&dzkai1ycfqd(4q^cx*t(rj7tr+otzl^5g7!g54&@j'
