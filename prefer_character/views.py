from django.shortcuts import render
from rest_framework import generics

from .models import PreferCharacter
from .serializers import PreferCharacterSerializer

class PreferCharacterViewSet(generics.ListCreateAPIView):
    queryset = PreferCharacter.objects.all()
    serializer_class = PreferCharacterSerializer
