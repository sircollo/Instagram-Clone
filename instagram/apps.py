from django.apps import AppConfig


class InstagramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'instagram'


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # add this
    def ready(self):
        import instagram.signals 