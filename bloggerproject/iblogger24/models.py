from django.db import models

# Create your models here.
class link(models.Model):
    Link = models.CharField(max_length=100)
    User_idx = models.CharField(max_length=50)
    Link_idx = models.CharField(max_length=50)
    Downloads = models.IntegerField()
    shorted_link = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    my_youtube = models.CharField(max_length=100)
    def __str__(self):
        return self.Link
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=10000)
    con_number = models.IntegerField()
class Total_content(models.Model):
    total_content = models.IntegerField()
class Round(models.Model):
    rounds = models.IntegerField()
    rounds_idx = models.CharField(max_length=50)
