from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from versatileimagefield.fields import VersatileImageField

class ProfileModel(models.Model):

    user_model = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    avatar = VersatileImageField(
        _('Avatar'),
        upload_to='media/images/avatart'
    )
    background = VersatileImageField(
        _('Background'),
        upload_to='media/images/background'
    )
    about = models.CharField(max_length= 2048)

    website_url = models.URLField(max_length= 256)

    date_birth = models.DateField()

    # address = ...

    def __str__(self):
    	return self.user_model.full_name

    @property
    def full_name(self):
    	return self.user_model.full_name

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"