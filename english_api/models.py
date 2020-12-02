from django.db import models

# Create your models here.

class Word(models.Model):
    title = models.CharField(max_length=200, unique=True)
    meanings = models.TextField()
    examples = models.TextField()


    def __str__(self):
        return self.title
