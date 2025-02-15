from django.apps import AppConfig


class ArduinoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'arduino_app'

    def ready(self):
     import arduino_app.signals  # Import the signals file