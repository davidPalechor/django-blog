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


class StudentUser(models.Model):
    INACTIVE = 'inactive'
    ACTIVE = 'active'

    STATE_CHOICES = (
        (INACTIVE, 'Inactive'),
        (ACTIVE, 'Active'),
    )

    user = models.OneToOneField(
        to=PersonUser,
        verbose_name='User',
        primary_key=True,
        on_delete=models.CASCADE,
    )
    career = models.CharField(
        max_length=15,
        verbose_name='Curricular Project'
    )
    grade_point_average = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Grade Point Average',
    )
    num_enrollments = models.SmallIntegerField(
        verbose_name='Number of Enrollments',
    )
    state = models.CharField(
        choices=STATE_CHOICES,
        max_length=8,
        verbose_name='Student State',
    )
    code = models.IntegerField(
        verbose_name="Student Code",
        unique=True
    )
    social_stratum = models.SmallIntegerField(
        verbose_name="Social Straum",
    )

    def __str__(self):
        return str(self.user)
