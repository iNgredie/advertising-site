from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Ad
from .serializers import AdSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [SearchFilter, OrderingFilter]
