from django.db import models

# Create your models here.
class Library(models.Model):
    bid=models.IntegerField()
    bname=models.CharField(max_length=100)
    bauthor=models.CharField(max_length=100)
    bcost=models.IntegerField()
    
