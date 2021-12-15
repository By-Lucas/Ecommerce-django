import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#NECESSARIO CRIAR ESTA PVARIAVEL DE PROETO
PROECT_DIR = os.path.dirname(os.path.abspath(__file__))

#CRIAR TEMPLATES E STATIC PARA css, js, imagens e demais
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates') #adicionar a pasta de templates

STATIC_DIR = os.path.join(BASE_DIR, 'static')#adicionar a pasta de css,js e demais

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c#7b_ub*3vdb-qb26a))#38e@yf#=7mw4crb6uht!5n7lb5=q='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/inicio/'  #QUANDO FAZER O LOGIN VAI PARA A PAGINA INICIAL

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Host for sending e-mail.
EMAIL_HOST = 'localhost'
# Port for sending e-mail.
EMAIL_PORT = 1025
# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = 'tekertudo@gmail.com'
EMAIL_HOST_PASSWORD = '123'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Epicups Team <admin@epicups.com>'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += [
    'usuarios',
    'produtos',
    'crispy_forms',
    'bootstrapform',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sistema_tk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sistema_tk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

#aqui é para a senha ter uma seguranca a mais, naos er uma senha simpes
AUTH_PASSWORD_VALIDATORS = [
        #{
        #    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        #},
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
        #    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

#liguagem em portugues do brasil
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

#tem que estar exatamente desta forma
STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = (
    STATIC_DIR,
)

# para poder usar arquivsos de media 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"
