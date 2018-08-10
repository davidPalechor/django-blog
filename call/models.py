from django.db import models
from django.utils import timezone

from user.models import PersonUser
from user.models import StudentUser


class Call(models.Model):
    PERIOD_CHOICES = (
        ('1', 'I'),
        ('2', 'II'),
    )

    class Meta:
        unique_together = ('year', 'period',)

    year = models.CharField(
        max_length=4,
        default=timezone.now().year,
        verbose_name='Year',
    )
    period = models.CharField(
        max_length=1,
        choices=PERIOD_CHOICES,
        verbose_name='Period',
    )
    start_date = models.DateField(
        default=timezone.now,
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        verbose_name='End Date',
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Created At',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At',
    )

    def __str__(self):
        return '{} - {}'.format(self.year, self.period)


class Conditon(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Name',
    )

    def __str__(self):
        return self.name


class Application(models.Model):
    STATUS_CHOICES = (
        ('Processing', 'processing'),
        ('Approved', 'approved'),
        ('Canceled', 'canceled'),
        ('Verified', 'verified'),
        ('Insufficient', 'insufficient'),
    )

    consecutive = models.AutoField(
        primary_key=True,
        verbose_name='Consecutive',
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=12,
        verbose_name='Status',
    )
    received_at = models.DateField(
        default=timezone.now,
        verbose_name="Received at",
    )
    score = models.SmallIntegerField(
        null=True,
        verbose_name="Score",
    )
    call = models.ForeignKey(
        to=Call,
        on_delete=models.CASCADE,
        related_name='call',
        verbose_name='Call',
    )
    student = models.ForeignKey(
        to=StudentUser,
        on_delete=models.CASCADE,
        related_name='student',
        verbose_name='Student'
    )
    admin = models.ForeignKey(
        to=PersonUser,
        on_delete=models.CASCADE,
        related_name='admin',
        verbose_name='Admin',
        null=True,
    )


class ApplicationCondition(models.Model):
    attachment = models.FileField(
        max_length=50,
        upload_to='application/',
        verbose_name='Attachment',
    )
    condition_value = models.CharField(
        max_length=10,
        verbose_name='Condition Value'
    )
    condition_score = models.PositiveSmallIntegerField(
        verbose_name='Condition Score',
        null=True,
    )
    condition_status = models.CharField(
        max_length=10,
        null=True,
        verbose_name='Condition Status',
    )
    application = models.ForeignKey(
        to=Application,
        on_delete=models.CASCADE,
        related_name='application',
        verbose_name='Application',
    )
    condition = models.ForeignKey(
        to=Conditon,
        on_delete=models.CASCADE,
        related_name='condition',
        verbose_name='Condition',
    )
