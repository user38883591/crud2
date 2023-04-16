from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    author=models.CharField(max_length=100,blank=False,null=False)
    publiction_date=models.DateField()
    genre=models.CharField(max_length=100,blank=False,null=False)

def __str__ (self):
    return self.name