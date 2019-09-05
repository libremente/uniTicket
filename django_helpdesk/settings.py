"""
Django settings for django_helpdesk project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import pathlib

from . settingslocal import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOME_PAGE = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
DATA_DIR = os.path.join(BASE_DIR, "data")

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DATA_DIR, 'static')
if not os.path.exists(STATIC_ROOT):
    pathlib.Path(STATIC_ROOT).mkdir(parents=True, exist_ok=True)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
if not os.path.exists(MEDIA_ROOT):
    pathlib.Path(MEDIA_ROOT).mkdir(parents=True, exist_ok=True)

# used for pdf creation and other temporary files
CACHE_DIR='django_helpdesk_cache'
TMP_DIR = os.path.sep.join((BASE_DIR, CACHE_DIR, 'tmp'))
if not os.path.exists(TMP_DIR):
    pathlib.Path(TMP_DIR).mkdir(parents=True, exist_ok=True)

# Application definition
INSTALLED_APPS = [
    'unical_accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'ckeditor',
    'datatables_ajax',
    'sass_processor',
    'bootstrap_italia_template',
    'unical_agid_template',
    'bootstrapform',
    'uni_ticket',
    'django_form_builder',
    'nested_admin',
    'organizational_area',

    # SAML2 SP
    'djangosaml2',
    'saml2_sp',
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

ROOT_URLCONF = 'django_helpdesk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

WSGI_APPLICATION = 'django_helpdesk.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_USER_MODEL = "unical_accounts.User"
LOGIN_URL = '/login'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'it-it'
TIME_ZONE = 'Europe/Rome'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATETIME_FORMAT = '{} %H:%M'.format(DEFAULT_DATE_FORMAT)
DATE_INPUT_FORMATS = [DEFAULT_DATE_FORMAT, '%d/%m/%Y']

CUSTOM_WIDGETS = {
    'BaseDateField': 'bootstrap_italia_template.widgets.BootstrapItaliaDateWidget',
    # 'BaseDateTimeField': 'bootstrap_italia_template.widgets.BootstrapItaliaTimeWidget',
    #'CustomSelectBoxField': 'bootstrap_italia_template.widgets.BootstrapItaliaSelectWidget',
    'CustomRadioBoxField': 'bootstrap_italia_template.widgets.BootstrapItaliaRadioWidget',
    # 'BaseDateField': 'django.forms.widgets.DateInput',
    # 'DateField': 'django.forms.widgets.DateInput',
    # 'CustomSelectBoxField': 'django.forms.widgets.Select',
    # 'CustomRadioBoxField': 'django.forms.widgets.RadioSelect',
}

if 'saml2_sp' in INSTALLED_APPS:
    from saml2_sp.settings import *

# DjangoSAML2 conf
if 'djangosaml2'  in INSTALLED_APPS:
    # from . import sp_pysaml2
    # pySAML2 SP mandatory
    # SESSION_EXPIRE_AT_BROWSER_CLOSE=True

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'djangosaml2.backends.Saml2Backend',
    )

# This parameter defines the roles of users to open ticket
# If True, an employee is a user that has the parameter 'matricola_dipendente' filled
# If False, an employee is a user that is mapped as OrganizationalStructureOfficeEmployee
# IS_UNIVERSITY = True
EMPLOYEE_ATTRIBUTE_NAME = 'matricola_dipendente'
USER_ATTRIBUTE_NAME = 'matricola_studente'
