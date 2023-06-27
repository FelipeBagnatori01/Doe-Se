from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    psw = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

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
    followers = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=50)
    image = models.ImageField()
    likes = models.IntegerField()

    def __str__(self) -> str:
        return self.id
