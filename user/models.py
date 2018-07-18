from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager


class PersonUser(AbstractBaseUser, PermissionsMixin):
    CC = 'cc'
    TI = 'ti'
    CE = 'ce'

    ID_CHOICES = [
        (CC, 'CC'),
        (TI, 'TI'),
        (CE, 'CE')
    ]

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'id_type',
        'address'
    ]

    objects = UserManager()

    id = models.IntegerField(
        primary_key=True,
        verbose_name='ID Number',
    )
    first_name = models.CharField(
        max_length=20,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        max_length=20,
        verbose_name='Last Name',
    )
    id_type = models.CharField(
        choices=ID_CHOICES,
        default=CC,
        max_length=2,
        verbose_name='ID type',
    )
    address = models.CharField(
        max_length=30,
        verbose_name='Address',

    )
    telephone = models.IntegerField(
        null=True,
        verbose_name='Telephone',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is Active'
    )
    is_staff = models.BooleanField(
        default=True,
        verbose_name='Is Staff',
    )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
