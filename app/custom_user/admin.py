from django.contrib import admin, messages
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel


class CustomUserAdmin(UserAdmin):
	fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'modified_at')}),
    )
	list_display = ('email', 'first_name', 'last_name', 'is_staff')
	ordering = ('email',)
	search_fields = ('first_name', 'last_name', 'email')

admin.site.register(CustomUserModel, CustomUserAdmin)