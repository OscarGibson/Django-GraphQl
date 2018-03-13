from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
	user_model = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CACADE)