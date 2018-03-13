from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    
    # python manage.py createsuperuser
    def create_superuser(self, email, is_staff, password):
        user = self.model(
                          email = email,                         
                          is_staff = is_staff,
                          )
        user.set_password(password)
        user.save(using= self._db)
        return user

class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    
    sys_id = models.AutoField(primary_key= True, blank= True)        
    email = models.EmailField(_('email'), 
                                max_length= 128, unique= True, 
                                null= False, blank= False)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default= True)
    is_admin = models.BooleanField(default= False)
    is_superuser = models.BooleanField(default= False)

    first_name = models.CharField(max_length= 256, blank= True)
    last_name = models.CharField(max_length= 256, blank= True)

    created_at = models.DateTimeField(auto_now= True)
    modified_at = models.DateTimeField(editable= True)
    last_login = models.DateTimeField()
    

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS must contain all required fields on your User model, 
    # but should not contain the USERNAME_FIELD or password as these fields will always be prompted for.
    REQUIRED_FIELDS = ['is_staff']

    class Meta:
        app_label = "custom_user"
        db_table = "custom_users"

    def __str__(self):
        return self.email

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name).capitalize()

    def get_short_name(self):
        first_name = self.first_name[0] if self.first_name else ''
        return "{0}{1}".format(first_name, self.last_name).lower()

    @property
    def username(self):
        return self.get_short_name()


    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj= None):
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_staff
