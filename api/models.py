from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission, User
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False, blank=True, null=True)


    def __str__(self):
        return self.title

