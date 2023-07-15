from typing import Any
from django.db import models
from django.contrib.auth import get_user_model
import json

class Institute(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    cep = models.IntegerField()
    uf = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    number = models.IntegerField()
    psw = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.name

class Follows(models.Model):
    follow = models.ForeignKey(Institute, on_delete=models.CASCADE)
    followers = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=50)
    image = models.ImageField()
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.text
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
        super().__init__(*args, **kwargs)

    def get_post(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = json.dumps(
            [
                {
                    'id': obj.id,
                    'user': obj.user,
                    'text': obj.text,
                    'image': obj.image,
                    'likes': obj.likes
                }
                for obj in Post.objects.all()
            ]
        )
        return context

