from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1','*']

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [

]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRIPE_PUBLIC_KEY = 'pk_test_51KxC76LpKpsRBsNSMD5jlyZ8Tg9NKgX2S0wvVu0leP62CWCZhIzrqW8hx9Gb79RUUKBbGJFjUtkeJZAq4eQmhqpP00qAwbkQHF'
STRIPE_SECRET_KEY = 'sk_test_51KxC76LpKpsRBsNSysXiARGFMxQ8EtY18Nk8EVMyqoD0wrGzDHLM5bHhuV4K9611c3PM7vy17NIDy2noge89PLpn00Fpm7ZRTn'


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = 'noreply@platfom.live'
EMAIL_HOST_PASSWORD = '2b0514c657d902a3b137b042834e91ec-4f207195-8d5752bf'