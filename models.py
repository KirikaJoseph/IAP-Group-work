
from django.db import models

class UserFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField()
    subscribe_newsletter = models.BooleanField(default=False)
