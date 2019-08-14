from rest_framework.viewsets import ModelViewSet
from .models import Attraction
from .serializers import AttractionSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class AttractionViewSet(ModelViewSet):

    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    filterset_fields = ['name']
    #'address__line_one' for foreign key
    search_fields = ['=minimum_age']
    lookup_field = 'name'