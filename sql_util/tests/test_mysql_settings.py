BACKEND = 'mysql'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sqlutil',
    }
}

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'sql_util.tests',
)

MIGRATION_MODULES = {'tests': None,
                     'contenttypes': None
                     }

SITE_ID = 1,

SECRET_KEY = 'secret'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)
