# Generated by Django 3.1.1 on 2020-10-21 21:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20201021_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of creation'),
        ),
    ]
