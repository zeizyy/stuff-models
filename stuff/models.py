from django.db import models

class User(models.Model):
    username = models.CharField(max_length=24)
    date_joined = models.DateTimeField()
    f_name = models.CharField(max_length=16)
    l_name = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    is_active = models.BooleanField()

class Thing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    giver = models.ForeignKey('User')
    date_given = models.DateTimeField()
    was_taken = models.BooleanField()

