from django.shortcuts import render
from rest_framework import generics

from .models import Pit
from .serializers import PitSerializer


class PitViewSet(generics.ListCreateAPIView):
    queryset = Pit.objects.all()
    serializer_class = PitSerializer