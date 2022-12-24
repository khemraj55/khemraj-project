from operator import mod
from django.db import models

# Create your models here.

class Snippet(models.Model):
    code=models.TextField()
    language=models.CharField(max_length=50)
