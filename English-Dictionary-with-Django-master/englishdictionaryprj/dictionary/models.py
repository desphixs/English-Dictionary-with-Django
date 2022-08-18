from django.db import models

# Create your models here.class
class SearchedWords(models.Model):
    word = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.word
