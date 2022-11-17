from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

from .manager import MyUserManager
import uuid

class User(AbstractBaseUser):
    email = models.EmailField(max_length=25,unique=True,)
    first_name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Employee_code = models.IntegerField(unique=True,null=True,blank=True)
    soft_delete = models.BooleanField(default=False)
    address=models.CharField( max_length=520)
    phone = models.CharField(max_length=100, null=True, blank=True)

  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()



    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class  Person(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)











#https://python.plainenglish.io/how-to-create-a-custom-user-model-in-django-601b61198bab