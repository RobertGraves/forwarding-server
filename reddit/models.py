from django.db import models

# Create your models here.


class Comment(models.Model):
    body        = models.TextField()
    author      = models.CharField(max_length=255,default="Unparsed")
    author_premium = models.BooleanField(default=False)
    url         = models.URLField(default="https://www.reddit.com/r/wallstreetbets")
    created     = models.DateTimeField()
    ups         = models.IntegerField()
    downs       = models.IntegerField()
    name        = models.CharField(max_length=155)
    timestamp   = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Submission(models.Model):
    author          = models.CharField(max_length=255,default="Unparsed")
    author_premium  = models.BooleanField(default=False)
    url             = models.URLField(default="https://www.reddit.com/r/wallstreetbets")
    body            = models.TextField()#selftext
    created         = models.DateTimeField()
    downs           = models.IntegerField()
    ups             = models.IntegerField()
    name            = models.CharField(max_length=155)
    title           = models.CharField(max_length=155)
    timestamp       = models.DateTimeField(auto_now_add=True)
    update          = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name




class Ticker(models.Model):
    comment     = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True,blank=True)
    ticker      = models.CharField(max_length=255)
    timestamp   = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ticker