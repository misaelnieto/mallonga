"""
WSGI config for mallonga project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import sys
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
print('#'*80)
print('Python interpreter:', sys.executable)
print('Python version:', sys.version)
print('Monkeypatched SQLite version:', sys.modules['sqlite3'].sqlite_version)
print('#'*80)
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mallonga.settings')

application = get_wsgi_application()
