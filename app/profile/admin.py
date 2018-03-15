from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from .models import ProfileModel


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'website_url', 'date_birth')
    ordering = ('user_model',)

    class Meta:
        model = ProfileModel

admin.site.register(ProfileModel, ProfileAdmin)