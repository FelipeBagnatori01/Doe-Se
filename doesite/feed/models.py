from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.IntegerField()

    def __str__(self) -> str:
        return self.nome
    
class Post(models.Model):
    text = models.CharField(max_length=50)
    image = models.IntegerField()
    likes = models.IntegerField()

    def __str__(self) -> str:
        return self.nome
