# Docker Doccano

This is a fork of https://github.com/doccano/doccano that integrates directly with existing django project. This does not require running a seperate single page application


## Installation

```bash
pip install pip install -e git+https://git@github.com/ajbeach2/doccano@master#egg=django-doccano
```

Ensure the follow appas are installed in settings.py;

```python
# settings.py
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
```python
# urls.py
urlpattersn = [
    path('doccano/', include('doccano.urls')
]
```
