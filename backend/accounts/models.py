from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):
  username = None
  email = models.EmailField(_("email address"), unique=True)

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  def __str__(self):
    return self.email


# class User(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=50)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     object = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'

#     def __str__(self) -> str:
#         return self.email
