from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'


#Check this for signals.py
    def ready(self):
        import users.signals
