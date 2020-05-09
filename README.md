# Docker Doccano

This is a fork of https://github.com/doccano/doccano that integrates directly with existing django project. This does not require running a seperate single page application


## Installatoin

Ensure the follow appas are installed in settings.py;

```
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'widget_tweaks',
    'polymorphic',
    'django_filters',
    'doccano',
]
```

Add doccano to your urls.py
```
urlpattersn = [
path('/doccano/', include('doccano.urls')
]
```
