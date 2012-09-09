from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib import admin
from django import forms

import datetime
import os

class Base(models.Model):
    created_at  = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        abstract = True

# Custom User Profile Model
class UserProfile(Base):
    user = models.OneToOneField(User)
    displayname = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
          return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
User.profile = property(lambda u: u.get_profile() )



# class Data(Base):
#     data = models.CharField(blank=True, null=True, max_length=255)

#     def __unicode__(self):