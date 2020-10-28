from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination

from .models import Ad
from .serializers import AdSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['price', 'create_at']
    pagination_class = PageNumberPagination
