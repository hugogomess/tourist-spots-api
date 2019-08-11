from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username