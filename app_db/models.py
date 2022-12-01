from django.db import models

# Create your models here.


class Example(models.Model):
    integer_fielad = models.IntegerField()
    char_fiald = models.CharField(max_length=10)
