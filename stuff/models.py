from django.db import models

class User(models.Model):
    username = models.CharField(max_length=24, unique=True)
    date_joined = models.DateTimeField()
    f_name = models.CharField(max_length=16)
    l_name = models.CharField(max_length=16)
    password = models.CharField(max_length=96)
    is_active = models.BooleanField()

class Thing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    giver = models.ForeignKey('User')
    location = models.CharField(max_length=20)
    date_given = models.DateTimeField()
    was_taken = models.BooleanField()

