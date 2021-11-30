from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '../db.sqlite3',
    }
}

# EMAIL_HOST_USER="ti.prefeitura.araquari@gmail.com"
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# DEFAULT_FROM_EMAIL ='Diretoria de TI <sgdti.ti@araquari.sc.gov.br>'
# EMAIL_HOST_PASSWORD = 'Dvb(0@1Tl'
# EMAIL_PORT = 587
# EMAIL_HOST_USER="sgdti.sistema@araquari.sc.gov.br"
# EMAIL_USE_TLS = False
# EMAIL_HOST = 'mail.araquari.sc.gov.br'
# EMAIL_HOST_PASSWORD = 'pma@email7777'


EMAIL_HOST_USER="ti.prefeitura.araquari@gmail.com"
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
DEFAULT_FROM_EMAIL ='Diretoria de TI <sgdti.sistema@araquari.sc.gov.br>'
EMAIL_HOST_PASSWORD = 'Dvb(0@1Tl'
EMAIL_PORT = 587

