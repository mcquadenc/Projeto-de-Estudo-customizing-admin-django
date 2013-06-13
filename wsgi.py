# -*- coding: utf-8 -*-
import os
import sys

paths = [
    os.path.dirname(os.path.abspath(__file__)),
]

for path in paths: sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

def application(environ, start_response):
    _application = django.core.handlers.wsgi.WSGIHandler()
        
    return _application(environ, start_response)
