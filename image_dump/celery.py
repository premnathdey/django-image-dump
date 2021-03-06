# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


from celery import Celery
from django.conf import settings  # noqa

app = Celery('django_image_dump')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
