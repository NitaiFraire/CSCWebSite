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

# Development
#############
DEBUG = True
ALLOWED_HOSTS = []

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