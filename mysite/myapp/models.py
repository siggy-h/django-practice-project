from django.db import models

# Create your models here.


class MyModel(models.Model):
    my_name = models.CharField(max_length=255)
