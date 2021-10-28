from django.apps import AppConfig


class AppkpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appkp'

class MyappConfig(AppConfig):
    name = 'appkp'
    def ready(self):
        import appkp.signals
