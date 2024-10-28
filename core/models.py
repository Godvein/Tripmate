from django.db import models

# Create your models here.
class blogs(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=5000)
    