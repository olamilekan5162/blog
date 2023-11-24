from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    html_tag = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    created_at = models.DateField(default=datetime.now, blank=True)
    body = models.CharField(max_length=1000000)

