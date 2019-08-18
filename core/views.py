from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TouristSpot
from .serializers import TouristSpotSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

class TouristSpotViewSet(ModelViewSet):
    
    serializer_class = TouristSpotSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        queryset = TouristSpot.objects.all()

        if id:
            queryset = queryset.filter(id=id)
        if name:
            queryset = queryset.filter(name=name)

        return queryset

    def list(self, request):
        return super(TouristSpotViewSet, self).list(request)

    def create(self, request):
        return super(TouristSpotViewSet, self).create(request)

    def destry(self, request):
        return super(TouristSpotViewSet, self).destroy(request)

    def retrieve(self, request):
        return super(TouristSpotViewSet, self).retrieve(request)

    def update(self, request):
        return super(TouristSpotViewSet, self).update(request)

    def partial_update(self, request):
        return super(TouristSpotViewSet, self).partial_update(request)

    @action(methods=['get'], detail=True)
    def by_name(self, request, pk=None):
        return Response({'kkk': 'kkk by name'})

    @action(methods=['get'], detail=False)
    def by_seila(self, request):
        return Response({'kkk': 'kkk sei lá doido'})