from .base import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': ''
    }
}

STRIPE_PUBLIC_KEY = 'pk_test_51KxC76LpKpsRBsNSMD5jlyZ8Tg9NKgX2S0wvVu0leP62CWCZhIzrqW8hx9Gb79RUUKBbGJFjUtkeJZAq4eQmhqpP00qAwbkQHF'
STRIPE_SECRET_KEY = 'sk_test_51KxC76LpKpsRBsNSysXiARGFMxQ8EtY18Nk8EVMyqoD0wrGzDHLM5bHhuV4K9611c3PM7vy17NIDy2noge89PLpn00Fpm7ZRTn'
