# Generated by Django 3.2 on 2020-11-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_post_attendees'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='event_date',
            field=models.DateField(null=True),
        ),
    ]
