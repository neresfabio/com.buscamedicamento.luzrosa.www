from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from uuid import uuid4
import random

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, phone_number=None, birth_date=None):
        if not email:
            raise ValueError('O campo de e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone_number=phone_number, birth_date=birth_date)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, phone_number=None, birth_date=None):
        user = self.create_user(email, name, password, phone_number, birth_date)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     verbose_name='user permissions',
    #     blank=True,
    #     related_name='customuser_user_permissions',  # Adicione related_name personalizado
    #     related_query_name='customuser_user_permission',
    # )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
