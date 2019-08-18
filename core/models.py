from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from addresses.models import Address
from reviews.models import Review

class TouristSpot(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='tourist_spot', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def test_description_two(self):
        return self.name + ' - ' + self.description

    def __str__(self):
        return self.name