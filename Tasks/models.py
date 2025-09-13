from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(null=True, blank=True)
    datecompleted = models.DateTimeField(null=True, blank=True) 
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
         return f"{self.title} - {self.user.username}"