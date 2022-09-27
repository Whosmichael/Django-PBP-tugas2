from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateTimeField(default=datetime.now())
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    is_finished = models.BooleanField(default=False)
