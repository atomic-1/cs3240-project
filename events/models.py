from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import datetime
from django.utils import timezone

class EventFiller(models.Model):
    date = models.DateTimeField('date')

class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    date = models.DateTimeField(auto_now=True)
    date_of = models.DateTimeField()
    event_description = models.CharField(max_length=500)
