from typing import Any
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    follow = models.ManyToManyField("self",
    related_name="followed_by",
    symmetrical=False,
    blank=True)

    def __str__(self):
        return self.user.username
    

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follow.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile, sender=User)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=250)
    image = models.ImageField(upload_to = "media")
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.text


