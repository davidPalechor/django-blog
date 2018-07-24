# Generated by Django 2.0.7 on 2018-07-24 04:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('career', models.CharField(max_length=15, verbose_name='Curricular Project')),
                ('grade_point_average', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Grade Point Average')),
                ('num_enrollments', models.SmallIntegerField(verbose_name='Number of Enrollments')),
                ('state', models.CharField(choices=[('inactive', 'Inactive'), ('active', 'Active')], max_length=8, verbose_name='Student State')),
                ('code', models.IntegerField(unique=True, verbose_name='Student Code')),
                ('social_stratum', models.SmallIntegerField(verbose_name='Social Straum')),
            ],
        ),
    ]
