# Generated by Django 2.0.7 on 2018-07-31 04:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conditon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
            ],
        ),
        migrations.AlterField(
            model_name='call',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='call',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Start Date'),
        ),
    ]