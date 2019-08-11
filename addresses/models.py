from django.db import models

class Address(models.Model):

    line_one = models.CharField(max_length=150)
    line_two = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.line_one
