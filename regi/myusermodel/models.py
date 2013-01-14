# -*- coding: utf-8 -*-
import string
import random

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, address, date_of_birth, activate_sting, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=MyUserManager.normalize_email(email),
            address=address,
            date_of_birth=date_of_birth,
            activate_sting=activate_sting,
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, address, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            address,
            date_of_birth,
            password=password,            
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    username = models.CharField(u'login', max_length=30, unique=True)
    date_create = models.DateField(auto_now=True)
    activate_sting = models.CharField(blank=True, max_length=64)
    address = models.CharField(blank=True, max_length=80)
    email = models.EmailField(u'email', unique=True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','date_of_birth','address']

    # def save(self, force_insert=False, force_update=False, update_fields=True, using=None): # update_fields=True,
        #### if not self.is_active:
        # self.activate_sting = unique_str_generator(10)
        # super(MyUser, self).save()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin