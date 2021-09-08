import random

from datetime import datetime


from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from accounts.manager import MyUserManager

# Create your models here.

PATIENT = 'PTNT'
DOCTOR = 'DOCT'
NURSE = 'NURS'
ADMIN = 'ADMN'

USER_TYPE_CHOICES = [
    (PATIENT, 'Patient'),
    (DOCTOR, 'Doctor'),
    (NURSE, 'Nurse'),
    (ADMIN, 'Admin')
]

def get_default_username():
        """create an unique username"""

        return str(datetime.now())


class MyUser(AbstractUser):
    """
    Custom User Model for adding usertype
    """
    username_validator = UnicodeUsernameValidator()


    user_type = models.CharField(max_length=4, choices=USER_TYPE_CHOICES, default=PATIENT) 
    username = models.CharField(
        max_length=150,
        unique=True,
        default=get_default_username(),
        validators=[username_validator]
    )
    email = models.EmailField(unique=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]


    
    