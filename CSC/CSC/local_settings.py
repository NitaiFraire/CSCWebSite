SECRET_KEY = 'tfdsad=upfdsar8t-q%a&&&70(cqx33$(l88jvh*3c_+8l@&v&_0%w3'
DEBUG = False
ALLOWED_HOSTS = ['64.227.63.169']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'csc',
        'USER': 'cscdatabase',
        'PASSWORD': 'Arya.stark420',
        'HOST': 'localhost',
	'PORT': '',
    }
}


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nfraire07@csc-its.com'
EMAIL_HOST_PASSWORD = 'Arya.stark420'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
