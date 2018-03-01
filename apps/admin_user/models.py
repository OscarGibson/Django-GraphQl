from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class MyUserManager(BaseUserManager):
    use_in_migrations = True
    
    # python manage.py createsuperuser
    def create_superuser(self, email, is_staff, password):
        user = self.model(
                          email = email,                         
                          is_staff = is_staff,
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

class UserModel(AbstractBaseUser):
    sys_id = models.AutoField(primary_key=True, blank=True)        
    email = models.EmailField(_('email'), 
    							max_length=128, unique=True, 
    							null=False, blank=False)
    is_staff = models.BooleanField()
    is_active = models.BooleanField(default=True)
    


    objects = MyUserManager()

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS must contain all required fields on your User model, 
    # but should not contain the USERNAME_FIELD or password as these fields will always be prompted for.
    REQUIRED_FIELDS = ['is_staff']

    class Meta:
        app_label = "accounts"
        db_table = "users"

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_staff
