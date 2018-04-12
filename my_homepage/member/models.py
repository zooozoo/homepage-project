from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
