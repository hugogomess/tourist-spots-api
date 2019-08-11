from django.db import models

class Attraction(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    opening_time = models.TimeField(null=True, blank=True)
    close_time = models.TimeField(null=True, blank=True)
    minimum_age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
