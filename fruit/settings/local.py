SECRET_KEY = 'xw6lssnj5lmd2k!#tu543nvacz%!hd@kr)xgrxf5v%+3=+o$76'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fruit_db',
        'USER': 'freeman',
        'PASSWORD': 'my3777',
        'HOST': 'localhost',
    }
}
ALLOWED_HOSTS = ['fruitbag.ru']
