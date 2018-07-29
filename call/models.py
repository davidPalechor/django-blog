from django.db import models
from django.utils import timezone


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
        default=timezone.now(),
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        verbose_name='End Date',
    )
    created_at = models.DateTimeField(
        default=timezone.now(),
        verbose_name='Created At',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At',
    )

    def __str__(self):
        return '{} - {}'.format(self.year, self.period)
