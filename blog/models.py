from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    TITLE = models.CharField(max_length=100)
    CONTENT = models.TextField()
    DATE = models.DateTimeField(default=timezone.now)
    AUTHOR = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.TITLE
