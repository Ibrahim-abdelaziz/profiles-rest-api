from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.



class UserProfileManager(BaseUserManager):

    def create_user(self, email, password):
        if not email:
            raise ValueError('User must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email = email, password=password)

        user.set_password(password)

        user.save(using = self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)

 
class Users(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length = 50, null = False, unique = True)
    is_staff = models.BooleanField(default=False)
    username = None

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']


    def __str__(self):
        return self.email