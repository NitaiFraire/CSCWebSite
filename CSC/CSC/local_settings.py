SECRET_KEY = 'tfdsad=upfdsar8t-q%a&&&70(cqx33$(l88jvh*3c_+8l@&v&_0%w3'

# Production
###############

# DEBUG = False
# ALLOWED_HOSTS = ['64.227.63.169', 'csc-its.com', 'www.csc-its.com']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'csc',
#         'USER': 'cscdatabase',
#         'PASSWORD': 'Arya.stark420',
#         'HOST': 'localhost',
# 	'PORT': '',
#     }
# }

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587    # TLS
EMAIL_HOST_USER = 'nfraire07@gmail.com'
EMAIL_HOST_PASSWORD = 'Arya.stark420'

# Development
#############
DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'csc',
        'USER': 'postgres',
        'PASSWORD': 'Arya.stark420',
        'HOST': 'localhost',
	'PORT': '',
    }
}

# EMAIL_HOST = 'smtp.mailtrap.io'
# EMAIL_HOST_USER = '53f74a7000ec96'
# EMAIL_HOST_PASSWORD = '16501a0ec10fce'
# EMAIL_PORT = '2525'