import django


__version__ = '0.1.0'

if django.VERSION < (3, 2):  # pragma: no cover
    default_app_config = 'dynaconf.apps.DynaconfConfig'
