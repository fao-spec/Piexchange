from django.db import models

# Create your models here.
from django.db import models

class Phrase(models.Model):
    username = models.CharField(max_length=100)
    phrase = models.TextField()