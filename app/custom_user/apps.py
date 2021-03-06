from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CustomUserConfig(AppConfig):
    name = 'custom_user'
    verbose_name = _("User")
