from django.shortcuts import render
from rest_framework import permissions, viewsets

from .models import Url
from .serializers import UrlSerializer

class UrlViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated, )

    queryset = Url.objects.all()
    serializer_class = UrlSerializer
