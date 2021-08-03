from django.shortcuts import render
from rest_framework import generics

from .models import Harmful
from .serializers import HarmfulSerializer


class HarmfulViewSet(generics.ListCreateAPIView):
    queryset = Harmful.objects.all()
    serializer_class = HarmfulSerializer
