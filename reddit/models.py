from django.db import models

# Create your models here.


class Comment(models.Model):
    body        = models.TextField()
    created     = models.DateTimeField()
    ups         = models.IntegerField()
    downs       = models.IntegerField()
    name        = models.CharField(max_length=155)

class Ticker(models.Model):
    comment     = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True,blank=True)
    ticker      = models.CharField(max_length=255)
    timestamp   = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)