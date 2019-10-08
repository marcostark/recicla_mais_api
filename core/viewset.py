from rest_framework import generics

from .pagination import CustomPagination
from .models import RecyclingCompany, CollectsNeighborhoods, CollectionPoints
from .serializers import RecyclingCompanySerializer, CollectsNeighborhoodsSerializer, CollectionPointsSerializer


class RecyclingCompanyListView(generics.ListAPIView):
    queryset = RecyclingCompany.objects.all()
    serializer_class = RecyclingCompanySerializer
    #filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = '__all__'
    filter_fields = 'nome'
    search_fields = 'nome'
    pagination_class = CustomPagination


class CollectsNeighborhoodsListView(generics.ListAPIView):
    queryset = CollectsNeighborhoods.objects.all()
    serializer_class = CollectsNeighborhoodsSerializer
    #filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = '__all__'
    filter_fields = 'nome'
    search_fields = 'nome'
    pagination_class = CustomPagination


class CollectionPointsListView(generics.ListAPIView):
    queryset = CollectionPoints.objects.all()
    serializer_class = CollectionPointsSerializer
    #filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = '__all__'
    filter_fields = 'nome'
    search_fields = 'nome'
    pagination_class = CustomPagination