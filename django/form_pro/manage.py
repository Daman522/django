#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# from importlib import import_module
from myapp import utils
from importlib import import_module

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'form_pro.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# try:
#     # Django versions >= 1.9
#     from django.utils.module_loading import import_module
# except ImportError:
#     # Django versions < 1.9
#     from django.utils.importlib import import_module

if __name__ == '__main__':
    main()
