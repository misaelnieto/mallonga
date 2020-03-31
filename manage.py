#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
print('#'*80)
print('Python interpreter:', sys.executable)
print('Python version:', sys.version)
print('Monkeypatched SQLite version:', sys.modules['sqlite3'].sqlite_version)
print('#'*80)

def main():
    if 'test' in sys.argv:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mallonga.settings_test')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mallonga.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
